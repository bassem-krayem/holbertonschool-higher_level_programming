-- Database and Table Creation for U.S. States
-- This script creates a database named 'hbtn_0d_usa' if it doesn't already exist.
-- Within that database, it creates a table named 'states' to store information about US states.

-- Each state record will have:
--   * id: A unique, auto-incrementing integer identifier (primary key)
--   * name: The name of the state (a string up to 256 characters, not allowed to be NULL)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);
