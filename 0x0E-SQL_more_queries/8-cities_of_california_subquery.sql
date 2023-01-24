-- Use a subquery
-- Select id and name from cities with California
-- state id
SELECT id, name
        FROM cities
        WHERE (SELECT id
                FROM state
                WHERE name = "California")
        ORDER BY id;
