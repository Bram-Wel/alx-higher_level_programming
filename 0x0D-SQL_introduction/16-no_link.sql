-- List table record except where name has no value
-- Select score, name records when name has a value
SELECT score, name
        FROM second_table
        WHERE name IS NOT NULL
        ORDER BY score DESC;
