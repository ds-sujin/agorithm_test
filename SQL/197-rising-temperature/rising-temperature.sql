SELECT w1.id AS Id
FROM Weather AS w1 JOIN Weather AS w2 ON w1.recordDate = w2.recordDate + 1      
-- w1이 w2의 '다음 날'
WHERE w1.temperature > w2.temperature;


-- 이전에 진행한 코드는 바로 하루 전이 아닌 경우에도 포함(이틀전이어도 디비에 전 순서기만 하면 뽑음)
--with total as (
--    SELECT id, LAG(temperature, 1) OVER (ORDER BY recordDate) As prev_temp, temperature
--    FROM Weather w
--    )
--SELECT id as Id
--FROM total
--WHERE temperature > prev_temp


-- LAG ( [컬럼명] , {N번째 행} ) OVER ( PARTITION BY [컬럼명] ORDER BY [컬럼명] )
-- LAG([컬럼명],{N번째 행} ): [컬럼명] 기준으로 N번째 행 이전 값을 출력
-- PARTITION BY [컬럼명] : [컬럼명] 기준으로 그룹핑
-- ORDER BY [컬럼명] : [컬럼명]기준으로 정렬 
-- PARTITION BY의 그룹핑 기능이 필요 없을 경우 생략 가능, 그러나 ORDER BY 쿼리는 반드시 포함해야 한다. 