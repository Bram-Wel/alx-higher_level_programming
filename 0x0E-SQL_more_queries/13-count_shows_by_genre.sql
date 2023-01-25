-- List all genres in DB and the no. of linked shows
-- Select name, count show_id from tv_genres, natural join
-- tv_show_genres in groups by genre names sorted in descending
-- no. of shows
SELECT name AS genre, COUNT(show_id) AS number_of_shows
        FROM tv_genres
        INNER JOIN tv_show_genres
        ON id = genre_id
        GROUP BY name
        ORDER BY number_of_shows DESC;
