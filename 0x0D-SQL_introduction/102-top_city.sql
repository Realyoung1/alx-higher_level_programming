-- Scripts that displaying the top 3 of cities temperatured durings July and August ordered by temperatured (descending)







SELECT `city`, AVG(value) `avg_temp` FROM `temperatures` WHERE month = 7 OR month = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
