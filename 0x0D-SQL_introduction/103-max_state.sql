-- Show max temp by state
-- Select State and compute maximum for groupings
-- by State and provide ordered output
SELECT state, MAX(value) AS max_temp
        FROM temperatures
        GROUP BY state
        ORDER BY state;
