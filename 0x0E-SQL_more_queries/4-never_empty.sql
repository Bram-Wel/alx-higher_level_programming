-- Create table
-- @id_not_null: Table name
-- Att:
--  id (INT): Record id
--  name (VARCHAR): String value
-- Create force_name if not exists
CREATE TABLE IF NOT EXISTS id_not_null (
        id INT DEFAULT 1, name VARCHAR(256)
);
