-- Scripts that is listings the numbers of records with the same scores in the tables second_table of the databased hbtn_0c_0 in your MySQL server







SELECT `score`, COUNT(score) `number` FROM second_table GROUP BY `score` ORDER BY `score` DESC;
