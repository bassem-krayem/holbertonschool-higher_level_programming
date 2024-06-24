-- Retrieve TV Shows and Their Associated Genres (Including Shows Without Genres)

-- This query fetches all TV shows from the 'tv_shows' table, along with their corresponding
-- genre IDs from the 'tv_show_genres' table. The results are ordered alphabetically by 
-- show title, and then by genre ID within each show. If a show doesn't have a genre assigned, 
-- its genre_id will be displayed as NULL.

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
