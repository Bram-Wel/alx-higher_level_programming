-- List all cities in database
-- Select all from cities where cities.id = states.id
SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE cities.id = states.id;
