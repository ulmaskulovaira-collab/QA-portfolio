-- SQL-001. Заказы без существующего пользователя
SELECT o.id, o.user_id, o.created_at
FROM orders AS o
LEFT JOIN users AS u ON u.id = o.user_id
WHERE u.id IS NULL;

-- SQL-002. Позиции заказа без родительского заказа
SELECT oi.id, oi.order_id, oi.product_id
FROM order_items AS oi
LEFT JOIN orders AS o ON o.id = oi.order_id
WHERE o.id IS NULL;

-- SQL-003. Некорректная итоговая сумма
SELECT id, user_id, total_amount, status
FROM orders
WHERE total_amount <= 0;

-- SQL-004. Дублирующиеся email пользователей
SELECT email, COUNT(*) AS duplicates_count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- SQL-005. Значение статуса вне согласованного набора
SELECT id, status
FROM orders
WHERE status NOT IN ('new', 'paid', 'processing', 'shipped', 'cancelled');

-- SQL-006. Сверка суммы заказа со стоимостью позиций
SELECT
  o.id AS order_id,
  o.total_amount AS stored_total,
  COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS calculated_total
FROM orders AS o
LEFT JOIN order_items AS oi ON oi.order_id = o.id
GROUP BY o.id, o.total_amount
HAVING o.total_amount <> COALESCE(SUM(oi.quantity * oi.unit_price), 0);
