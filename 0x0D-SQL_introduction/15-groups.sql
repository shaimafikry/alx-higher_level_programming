-- script that lists the number of records with the same score in the "second_table"
-- result should display the score m the number of this score with the lable name
SELECT score, count(score) AS number from second_table 
WHERE score=score
GRUOP BY score
ORDER BY score DESC;
