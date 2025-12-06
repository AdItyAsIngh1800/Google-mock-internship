CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(50),
    created_at DATE
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    transaction_date DATE,
    payment_method VARCHAR(50),
    status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- Q1
SELECT 
    t.transaction_id,
    u.user_name,
    u.country,
    t.transaction_date
FROM transactions t
JOIN users u ON t.user_id = u.user_id;

--Q2
SELECT 
    t.transaction_id,
    u.user_name,
    p.product_name,
    t.quantity,
    (t.quantity * p.price) AS total_amount
FROM transactions t
JOIN users u ON t.user_id = u.user_id
JOIN products p ON t.product_id = p.product_id;

--Q3
SELECT 
    u.country,
    SUM(t.quantity * p.price) AS total_revenue
FROM transactions t
JOIN users u ON t.user_id = u.user_id
JOIN products p ON t.product_id = p.product_id
GROUP BY u.country;

--Q4
SELECT 
    u.user_id,
    u.user_name,
    user_totals.total_spent
FROM users u
JOIN (
    SELECT 
        t.user_id,
        SUM(t.quantity * p.price) AS total_spent
    FROM transactions t
    JOIN products p ON t.product_id = p.product_id
    GROUP BY t.user_id
) AS user_totals
ON u.user_id = user_totals.user_id
WHERE user_totals.total_spent > 1000;

--Q5
SELECT
    t.user_id,
    t.transaction_id,
    t.transaction_date,
    ROW_NUMBER() OVER (
        PARTITION BY t.user_id 
        ORDER BY t.transaction_date DESC
    ) AS txn_rank
FROM transactions t;

--Q6
SELECT 
    transaction_id,
    user_id,
    payment_method,
    status,
    transaction_date
FROM transactions
WHERE status = 'SUCCESS'
  AND payment_method = 'Credit Card'
  AND transaction_date > '2024-01-01';

--Q7
SELECT
    p.product_id,
    p.product_name,
    SUM(t.quantity * p.price) AS total_revenue
FROM transactions t
JOIN products p ON t.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC
LIMIT 3;

--Q8
SELECT
    u.user_id,
    u.user_name,
    AVG(t.quantity * p.price) AS avg_order_value
FROM transactions t
JOIN users u ON t.user_id = u.user_id
JOIN products p ON t.product_id = p.product_id
GROUP BY u.user_id, u.user_name;
