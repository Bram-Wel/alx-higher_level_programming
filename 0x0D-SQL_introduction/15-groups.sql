-- List number of records with the same score.
-- Select scores, count score entries(Skip Null) and group
-- them by product name
SELECT score, COUNT(score) AS number
        FROM second_table
        GROUP BY score
        ORDER BY number DESC;
