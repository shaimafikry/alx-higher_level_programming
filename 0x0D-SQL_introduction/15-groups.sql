-- script that lists the number of records with the same score in the "second_table"
-- redult should display the score m the number of this score with the lable name
SELECT score, count(score) AS number from second_table where score=score ORDER BY score DESC GRUOP BY score;
