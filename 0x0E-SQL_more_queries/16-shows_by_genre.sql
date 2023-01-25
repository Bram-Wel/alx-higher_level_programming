-- List all shows in DB and linked genres
-- Select title, name from tv_shows natural join tv_show_genres,
-- tv_genres
SELECT title, name
        FROM tv_shows
        LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
        LEFT JOIN tv_genres
        ON tv_show_genres.genre_id = tv_genres.id
        ORDER BY title, name;
