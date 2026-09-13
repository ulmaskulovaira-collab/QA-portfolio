"""Tiny SQLite order service used as a reproducible target for QA checks."""

from pathlib import Path
import sqlite3

SCHEMA = Path(__file__).with_name("schema.sql")


def connect(database=":memory:"):
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript(SCHEMA.read_text(encoding="utf-8"))
    return connection


def seed(connection):
    connection.execute("INSERT INTO customers (id, email) VALUES (?, ?)", (1, "ira@example.test"))
    connection.executemany(
        "INSERT INTO products (id, name, price_cents) VALUES (?, ?, ?)",
        [(1, "Лампа", 129900), (2, "Колонка", 349900)],
    )
    connection.commit()


def create_order(connection, customer_id, lines):
    """Create an order atomically; lines is a list of (product_id, quantity)."""
    if not lines:
        raise ValueError("В заказе должен быть хотя бы один товар")
    if len({product_id for product_id, _ in lines}) != len(lines):
        raise ValueError("Один товар нельзя добавить двумя строками")
    if any(quantity <= 0 for _, quantity in lines):
        raise ValueError("Количество должно быть положительным")

    try:
        with connection:
            if connection.execute("SELECT 1 FROM customers WHERE id = ?", (customer_id,)).fetchone() is None:
                raise ValueError("Покупатель не найден")
            priced_lines = []
            for product_id, quantity in lines:
                product = connection.execute(
                    "SELECT price_cents FROM products WHERE id = ?", (product_id,)
                ).fetchone()
                if product is None:
                    raise ValueError(f"Товар {product_id} не найден")
                priced_lines.append((product_id, quantity, product["price_cents"]))

            total = sum(quantity * price for _, quantity, price in priced_lines)
            cursor = connection.execute(
                "INSERT INTO orders (customer_id, status, total_cents) VALUES (?, 'new', ?)",
                (customer_id, total),
            )
            order_id = cursor.lastrowid
            connection.executemany(
                "INSERT INTO order_items (order_id, product_id, quantity, unit_price_cents) "
                "VALUES (?, ?, ?, ?)",
                [(order_id, product_id, quantity, price) for product_id, quantity, price in priced_lines],
            )
            return order_id
    except Exception:
        connection.rollback()
        raise


def set_status(connection, order_id, status):
    if status not in {"new", "paid", "cancelled"}:
        raise ValueError("Неизвестный статус")
    with connection:
        cursor = connection.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
        if cursor.rowcount == 0:
            raise ValueError("Заказ не найден")
