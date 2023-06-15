-- list number of record with same score from table 'second_score'
SELECT 'score', COUNT(*) AS 'number' 
FROM 'second_table'
GROUP BY 'score'
ORDER BY 'number' DESC;


