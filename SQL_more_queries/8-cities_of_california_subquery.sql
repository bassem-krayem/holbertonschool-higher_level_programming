-- Retrieve Cities in California
--
-- This SQL query selects the names of all cities located in the state of California from 
-- the 'hbtn_0d_usa' database. It does this by:
--
-- 1. Subquery: 
--    - The inner query finds the unique ID of the state named "California" in the 'states' table.
--
-- 2. Main Query:
--    - The outer query selects the 'name' column from the 'cities' table.
--    - It filters the results to include only cities where the 'state_id' matches the ID of California obtained from the subquery.

SELECT id, name 
FROM cities 
WHERE state_id IN (
    SELECT id 
    FROM states 
    WHERE name = "California"
)
ORDER BY id ASC;
