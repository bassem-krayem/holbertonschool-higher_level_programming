-- Retrieve scores and names from second_table, filtering by scores greater than 
-- or equal to 10 and sorting by score (highest to lowest) and then name (ascending)

SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC, name;
