import sqlite3
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from shop import connect, create_order, seed, set_status


class OrderTests(unittest.TestCase):
    def setUp(self):
        self.db = connect()
        seed(self.db)

    def tearDown(self):
        self.db.close()

    def test_order_total_and_items_match(self):
        order_id = create_order(self.db, 1, [(1, 2), (2, 1)])
        order = self.db.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
        self.assertEqual(order["total_cents"], 609700)
        self.assertEqual(order["status"], "new")
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM order_items WHERE order_id = ?", (order_id,)).fetchone()[0], 2)
        self.assertEqual(self._mismatches(), [])

    def test_invalid_lines_do_not_create_partial_order(self):
        for lines in ([], [(1, 0)], [(1, -1)], [(1, 1), (1, 2)], [(1, 1), (999, 1)]):
            with self.subTest(lines=lines), self.assertRaises(ValueError):
                create_order(self.db, 1, lines)
            self.assertEqual(self.db.execute("SELECT COUNT(*) FROM orders").fetchone()[0], 0)

    def test_unknown_customer_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Покупатель"):
            create_order(self.db, 999, [(1, 1)])

    def test_status_change_and_unknown_status(self):
        order_id = create_order(self.db, 1, [(1, 1)])
        set_status(self.db, order_id, "paid")
        with self.assertRaises(ValueError):
            set_status(self.db, order_id, "delivered")
        self.assertEqual(self.db.execute("SELECT status FROM orders WHERE id = ?", (order_id,)).fetchone()[0], "paid")

    def test_foreign_key_blocks_orphan_items(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO order_items VALUES (999, 1, 1, 129900)")

    def test_diagnostic_query_finds_wrong_total(self):
        order_id = create_order(self.db, 1, [(1, 1)])
        self.db.execute("UPDATE orders SET total_cents = 1 WHERE id = ?", (order_id,))
        self.assertEqual([row["id"] for row in self._mismatches()], [order_id])

    def _mismatches(self):
        sql = Path(__file__).resolve().parents[1].joinpath("validation_queries.sql").read_text(encoding="utf-8").split(";")[0]
        return self.db.execute(sql).fetchall()


if __name__ == "__main__":
    unittest.main()
