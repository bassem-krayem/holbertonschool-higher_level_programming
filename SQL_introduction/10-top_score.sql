-- list the rows of second_table by order
-- order by score and name with the highest value first in score

SELECT score, name 
FROM second_table
ORDER BY score DESC, name ASC;
