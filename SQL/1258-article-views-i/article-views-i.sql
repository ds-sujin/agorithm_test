-- Write your PostgreSQL query statement below
SELECT DISTINCT author_id as id -- 중복제거(독립으로 설정)
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id; -- 오름차순으로 기본 설정