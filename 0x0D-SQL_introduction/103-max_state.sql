-- Scripts that is displaying the maxis temperatured of each stated (ordered by State name)







SELECT state, MAX(value) `max_temp` FROM temperatures GROUP BY state ORDER BY state;
