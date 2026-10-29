-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- Table: Visits

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | visit_id    | int     |
-- | customer_id | int     |
-- +-------------+---------+
-- visit_id is the column with unique values for this table.
-- This table contains information about the customers who visited the mall.
 

-- Table: Transactions

-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | transaction_id | int     |
-- | visit_id       | int     |
-- | amount         | int     |
-- +----------------+---------+
-- transaction_id is column with unique values for this table.
-- This table contains information about the transactions made during the visit_id.
 

-- Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

-- Return the result table sorted in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Visits
-- +----------+-------------+
-- | visit_id | customer_id |
-- +----------+-------------+
-- | 1        | 23          |
-- | 2        | 9           |
-- | 4        | 30          |
-- | 5        | 54          |
-- | 6        | 96          |
-- | 7        | 54          |
-- | 8        | 54          |
-- +----------+-------------+
-- Transactions
-- +----------------+----------+--------+
-- | transaction_id | visit_id | amount |
-- +----------------+----------+--------+
-- | 2              | 5        | 310    |
-- | 3              | 5        | 300    |
-- | 9              | 5        | 200    |
-- | 12             | 1        | 910    |
-- | 13             | 2        | 970    |
-- +----------------+----------+--------+
-- Output: 
-- +-------------+----------------+
-- | customer_id | count_no_trans |
-- +-------------+----------------+
-- | 54          | 2              |
-- | 30          | 1              |
-- | 96          | 1              |
-- +-------------+----------------+
-- Explanation: 
-- Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
-- Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
-- Customer with id = 30 visited the mall once and did not make any transactions.
-- Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
-- Customer with id = 96 visited the mall once and did not make any transactions.
-- As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.


Select v.customer_id, count(*) as count_no_trans -- WHERE condition ensures t.transaction_id is always NULL. COUNT(column) ignores NULL values
from visits as v
left join transactions as t on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id -- You need to group results by customer_id because the question asks for the number of visits without transactions per customer.

-- Why does this work?

-- Step 1: LEFT JOIN

-- Keeps all visits, including visits without a matching transaction.

-- Step 2: WHERE

-- WHERE t.transaction_id IS NULL

-- Filters out visits that have transactions, leaving only visits without transactions.

-- Step 3: GROUP BY

-- GROUP BY v.customer_id

-- Groups the remaining visits by customer.

-- Step 4: COUNT(*)

-- Counts the number of visits without transactions for each customer.

-- Important: COUNT(*) vs COUNT(column)
-- Expression	Behavior
-- COUNT(*)	Counts all rows, including rows containing NULL values
-- COUNT(column)	Counts only rows where that column is NOT NULL
-- COUNT(DISTINCT column)	Counts unique non-NULL values

-- Example:

-- Suppose customer 23 visits three times, but only makes a transaction during one visit.

-- After the LEFT JOIN and WHERE filter, two rows remain.

-- COUNT(t.transaction_id) returns 0 because both values are NULL.
-- COUNT(*) returns 2, which is what the problem requires.

-- Time complexity: Generally depends on the database's execution plan, indexes, and join strategy.

-- Key takeaway: Whenever you're counting unmatched records using LEFT JOIN ... WHERE right_table.id IS NULL, use COUNT(*) and group by the entity you want to count for.