-- Convert the database hbtn_0c_0 to UTF-8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci; 

-- Select the hbtn_0c_0 database for subsequent operations
USE hbtn_0c_0; 

-- Convert the first_table to UTF-8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 

-- Explicitly change the 'name' column to UTF-8mb4, adjusting the size to VARCHAR(191) 
-- (recommended for compatibility with MySQL's indexing limitations)
ALTER TABLE first_table MODIFY name VARCHAR(191) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Additionally, convert the 'id' column and set the default collation for the table
ALTER TABLE first_table DEFAULT COLLATE = utf8mb4_unicode_ci;
