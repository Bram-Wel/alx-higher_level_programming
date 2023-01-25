-- List all shows in DB linked by genre
-- Select title, genre_id from tv_shows, Left outer join
-- tv_show_genres odered by title and genre_id
SELECT title, genre_id
        FROM tv_shows
        LEFT JOIN tv_show_genres
        ON tv_shows.id = show_id
        ORDER BY title, genre_id;
