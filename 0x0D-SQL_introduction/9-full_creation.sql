-- Create second_table & insert multiple rows.
-- Create second_table
CREATE TABLE IF NOT EXISTS second_table (
        id INT, name VARCHAR(256), score INT
);

-- Insert multiple records into table
-- @id: Records Id
-- @name: Name value
-- @score: Score value
INSERT INTO second_table ()
VALUES ( 1, "John", 10 ), ( 2, "Alex", 3 ), ( 3, "Bob", 14), ( 4, "George", 8)
