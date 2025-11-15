-- Write your PostgreSQL query statement below
-- 고객별(no-trans 방문 수)
WITH no_trans_visits AS (
  SELECT v.customer_id, v.visit_id
  FROM Visits v
  WHERE NOT EXISTS (
    SELECT 1 
    -- transaction_id
    FROM Transactions t
    WHERE t.visit_id = v.visit_id
  )
)
SELECT customer_id, COUNT(*) AS count_no_trans
FROM no_trans_visits
GROUP BY customer_id
ORDER BY customer_id;

-- transction거래 /visit방문 /customer고객 번호, 방문은 했지만 trans가 없는 고객 수
-- 2/5/54
-- 3/5/54
-- 9/5/54, 54번 손님이 한번 방문에 3번 거래함
-- 12/1/23
-- 13/2/9
-- */4/30
-- */6/96
-- */7/54
-- */8/54