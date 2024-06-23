-- List Cities and States:
-- This query retrieves the id, city name, and state name for all cities
-- in the database. The results are ordered by city ID in ascending order.

SELECT cities.id, cities.name, states.name
FROM cities 
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
