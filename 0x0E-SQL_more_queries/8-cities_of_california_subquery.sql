-- Use a subquery
-- Select id and name from cities with California
-- state id
SELECT id, name
        FROM cities
        WHERE state_id = (SELECT id
                FROM states
                WHERE name = "California")
        ORDER BY id;
