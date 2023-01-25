-- List all shows not of the Comedy genre
-- Select title from tv_shows not in
-- select title from tv_shows join tv_show_genres, tv_shows
-- where genre = Comedy
SELECT title
        FROM tv_shows
        WHERE title NOT IN
        (SELECT title
        FROM tv_shows
        INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
        INNER JOIN tv_genres
        ON tv_show_genres.genre_id = tv_genres.id
        WHERE name = "Comedy")
        ORDER BY title;
