-- Scripts that is listing all records of the tables second_table of the databasesdd hbtn_0c_0 in your MySQL server.







SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL AND `name` != "" ORDER BY `score` DESC;
