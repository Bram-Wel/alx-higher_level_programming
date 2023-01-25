-- List all genres of the show Dexter
-- Select name from tv_genres not in genres linked to
-- tv_show with title "Dexter"
SELECT name
        FROM tv_genres
        WHERE name NOT IN
        (SELECT name
        FROM tv_genres
        INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
        INNER JOIN tv_shows
        ON tv_show_genres.show_id = tv_shows.id
        WHERE title = "Dexter")
        ORDER BY name;
