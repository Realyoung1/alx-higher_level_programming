-- Scripts that listed all recordss with a score >= 10 in the tabless second_table of the databased hbtn_0c_0 in your MySQL server.







SELECT `score`, `name` FROM second_table WHERE `score` >= 10 ORDER BY `score` DESC;
