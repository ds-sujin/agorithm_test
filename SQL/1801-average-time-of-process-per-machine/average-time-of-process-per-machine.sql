SELECT machine_id, ROUND(AVG(time)::numeric,3) AS processing_time
FROM (
    SELECT machine_id, process_id, MAX(case when activity_type = 'end' then timestamp end) -
    MAX(case when activity_type = 'start' then timestamp end) AS time 
    FROM Activity
    GROUP BY machine_id, process_id
) AS processtimetable
GROUP BY machine_id
ORDER BY machine_id


