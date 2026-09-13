-- Диагностические запросы: каждый должен вернуть 0 строк на корректных данных.
-- Сверка итоговой суммы с позициями заказа (JOIN + GROUP BY + HAVING).
SELECT o.id, o.total_cents, COALESCE(SUM(i.quantity * i.unit_price_cents), 0) AS calculated_cents
FROM orders AS o
LEFT JOIN order_items AS i ON i.order_id = o.id
GROUP BY o.id, o.total_cents
HAVING o.total_cents != calculated_cents;

-- Заказы без покупателя (проверка данных даже при отключённых ограничениях БД).
SELECT o.id FROM orders AS o
LEFT JOIN customers AS c ON c.id = o.customer_id
WHERE c.id IS NULL;

-- Позиции без заказа.
SELECT i.order_id, i.product_id FROM order_items AS i
LEFT JOIN orders AS o ON o.id = i.order_id
WHERE o.id IS NULL;
