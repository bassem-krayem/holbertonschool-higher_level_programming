-- Retrieve Genres of the TV Show 'Dexter'

-- This SQL query lists all genres associated with the television show "Dexter" in the database. 
-- It achieves this by:

-- 1. Joining Tables:
--    - Joining `tv_genres`, `tv_show_genres`, and `tv_shows` tables to establish the relationships
--      between genres, shows, and their genre associations.

-- 2. Filtering:
--    - Filtering the results to include only rows where the show title is "Dexter."

-- 3. Selecting and Sorting:
--    - Selecting only the `name` column from the `tv_genres` table (which now contains only
--      genres linked to 'Dexter').
--    - Sorting the results by genre name in ascending order.

SELECT tv_genres.name 
FROM tv_genres 
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
