-- Create hbtn_0d_usa DB
-- Create a cities table
-- @id (INT): UNIQUE, AUTO-GENERATED, NOT NULL, PRIMARY KEY
-- @state_id (INT): NOT NULL FOREIGN KEY(states.id)
-- @name (VARCHAR): NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
        id INT UNIQUE AUTO_INCREMENT NOT NULL,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
