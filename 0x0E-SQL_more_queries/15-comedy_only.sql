-- List all comedy shows in DB
-- Select title from tv_shows natural join tv_show_genres,
-- tv_genres where name is "Comedy"
SELECT title
        FROM tv_shows
        INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
        INNER JOIN tv_genres
        ON tv_show_genres.genre_id = tv_genres.id
        WHERE name = "Comedy"
        ORDER BY title;
