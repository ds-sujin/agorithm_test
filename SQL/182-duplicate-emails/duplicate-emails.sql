SELECT e.email as Email
FROM (
    SELECT email, COUNT(id) as cnt
    FROM Person p
    GROUP BY email
) as e
WHERE cnt > 1