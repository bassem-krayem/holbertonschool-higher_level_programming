-- Retrieve All TV Shows and Their Genres (Including Shows Without Genres)

-- This query retrieves a list of all TV shows in the 'tv_shows' table, along with their 
-- associated genres from the 'tv_genres' table.

SELECT 
    tv_shows.title,          -- Select the show title from the 'tv_shows' table
    tv_genres.name AS genre  -- Select the genre name (or NULL if not linked)

FROM tv_shows                 -- Start with the 'tv_shows' table to get ALL shows

-- Perform LEFT JOINs to include shows even if they don't have genres:
LEFT JOIN tv_show_genres      
ON tv_shows.id = tv_show_genres.show_id  -- Link shows to their genres (if they exist)

LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id  -- Link show-genre pairs to the genre names

-- Order the results by show title first, then by genre name (NULLs will appear last):
ORDER BY tv_shows.title, tv_genres.name; 
