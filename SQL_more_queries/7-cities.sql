-- Database and Table Creation for U.S. Cities and States
-- 
-- This script creates:
--   * A database named 'hbtn_0d_usa' to hold information related to US states and cities.
--   * A table named 'cities' within the 'hbtn_0d_usa' database to store city information.
--
-- The 'cities' table will have the following columns:
--   * id: Unique, auto-incrementing integer to identify each city (primary key)
--   * state_id: Foreign key referencing the 'id' column in the 'states' table (cannot be null)
--   * name: The name of the city (up to 256 characters, not null)
--
-- Note: This script assumes that the 'states' table already exists within the 'hbtn_0d_usa' database. 
--       The 'state_id' in the 'cities' table will reference the 'id' in the 'states' table.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    -- the foreign key
    FOREIGN KEY (state_id) REFERENCES states(id)
);

