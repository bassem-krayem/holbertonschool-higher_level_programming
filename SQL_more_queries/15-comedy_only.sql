-- Retrieve Comedy Shows:
-- This query lists all comedy shows in the 'hbtn_0d_tvshows' database.

-- It achieves this by:

-- 1. Joining tables:
--    - Joining the 'tv_shows', 'tv_show_genres', and 'tv_genres' tables to establish 
--      the relationships between shows, their genres, and genre details.

-- 2. Filtering:
--    - Filtering the results to include only shows where the genre name is 'Comedy'.

-- 3. Selecting and Sorting:
--    - Selecting only the 'title' column from the 'tv_shows' table, representing the show names.
--    - Sorting the results by show title in ascending order.

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
