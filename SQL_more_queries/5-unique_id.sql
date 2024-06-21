-- a script that creates the table unique_id on your MySQL server.
-- This script creates a table called 'unique_id' to store records with unique IDs

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
