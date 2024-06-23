-- Retrieve TV Show Titles and Their Corresponding Genre IDs:

-- This query joins the 'tv_shows' and 'tv_show_genres' tables to retrieve a list of all 
-- television show titles along with the unique identification numbers (IDs) of their associated genres. 
-- The results are sorted alphabetically by show title, and then by genre ID within each show.

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
