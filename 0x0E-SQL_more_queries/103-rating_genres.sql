-- List all shows by their rating
-- Select title, rate aggregate as rating from tv_shows joined to
-- tv_show_genres, tv_show_ratings and grouped by title
SELECT name, SUM(rate) AS rating
        FROM tv_genres
        INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
        INNER JOIN tv_show_ratings
        ON tv_show_genres.show_id = tv_show_ratings.show_id
        GROUP BY name
        ORDER BY rating DESC;
