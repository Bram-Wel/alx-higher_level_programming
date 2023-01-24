-- Show average temperatures by city
-- Select city and compute average temperatures
-- for each grouping by city
SELECT city, AVG(value) as avg_temp
        FROM temperatures
        GROUP BY (city)
        ORDER BY avg_temp DESC;
