-- Retrieve TV Shows Without a Linked Genre

-- This query lists all television shows in the database 'hbtn_0d_tvshows' 
-- that do not have any associated genres. It retrieves the following columns:

--   tv_shows.title: The title of the TV show
--   tv_show_genres.genre_id: The genre ID (will be NULL if the show has no genre)

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows              -- Start with the 'tv_shows' table to get all shows

-- Perform a LEFT JOIN with 'tv_show_genres' to include all shows, even if no genre exists:
LEFT JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.show_id   -- Match shows and genres by ID

-- Filter out shows that DO have a genre linked:
WHERE tv_show_genres.genre_id IS NULL  

-- Sort the results first by show title (ascending), then by genre ID (ascending, but all NULLs):
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
