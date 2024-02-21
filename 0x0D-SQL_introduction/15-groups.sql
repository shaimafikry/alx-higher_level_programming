-- script that lists the number of records with the same score in the "second_table"
-- result should display the score m the number of this score with the lable name
SELECT score, COUNT(*) AS number
FROM second_table 
GROUP BY score
ORDER BY score DESC;
