-- Script that displays the max temperature of each state (ordered by State name)
SELECT state, MAX(value) `max_temp` FROM temperatures GROUP BY state ORDER BY state;
