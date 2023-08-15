-- Scripts that is displayings the averages temperature (Fahrenheit) by city orderedss by temperature (descending).







SELECT `city`, AVG(value) `avg_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
