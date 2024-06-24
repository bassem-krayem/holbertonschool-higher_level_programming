-- List TV Show Genres and Number of Shows Linked

-- This query lists all genres from the 'tv_genres' table along with the number of shows
-- linked to each genre. Only genres with at least one associated show are displayed, and
-- the results are sorted in descending order by the number of shows.

SELECT 
    tv_genres.name AS genre,         -- Select the genre name (aliased as 'genre')
    COUNT(tv_show_genres.show_id) AS number_of_shows  -- Count the number of linked shows for each genre

FROM tv_genres     -- Start with the table containing genre information

-- Join with 'tv_show_genres' to get the links between shows and genres:
INNER JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id  -- Match genres and show-genre relationships

-- Group the results by genre to calculate the count for each genre:
GROUP BY tv_genres.name 

-- Filter out genres that don't have any linked shows:
HAVING COUNT(tv_show_genres.show_id) > 0 

-- Sort the results in descending order based on the number of shows per genre:
ORDER BY number_of_shows DESC; 
