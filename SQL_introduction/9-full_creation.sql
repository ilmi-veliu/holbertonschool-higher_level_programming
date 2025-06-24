-- Create the table second_table if it doesn't exist
-- The table will have the columns: id, name, score
CREATE TABLE IF NOT EXISTS second_table (id INT,name VARCHAR(256),score INT);

-- Insert multiple rows into the table
-- Each row represents a user with an id, name, and score
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
