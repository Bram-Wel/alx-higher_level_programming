-- List all shows by their rating
-- Select title, rate aggregate as rating from tv_shows joined to
-- tv_show_genres, tv_show_ratings and grouped by title
SELECT title, SUM(rate) AS rating
        FROM tv_shows
        LEFT JOIN tv_show_ratings
        ON id = tv_show_ratings.show_id
        GROUP BY title
        ORDER BY rating DESC;
