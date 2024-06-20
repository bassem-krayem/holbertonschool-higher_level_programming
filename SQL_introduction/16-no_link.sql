-- This script lists all records of the table second_table from the database hbtn_0c_0.
-- It only displays records that have a name value, sorted by score in descending order.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
