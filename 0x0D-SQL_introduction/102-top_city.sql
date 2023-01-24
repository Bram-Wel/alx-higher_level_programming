-- Show the top 3 cities temperature in July, August
-- Select city and compute July, August averages for each
-- grouping by city then limit ordered output table to 3
SELECT city, AVG(value) as avg_temp
        FROM temperatures
        WHERE month=7 OR month=8
        GROUP BY (city)
        ORDER BY avg_temp DESC
        LIMIT 3;
