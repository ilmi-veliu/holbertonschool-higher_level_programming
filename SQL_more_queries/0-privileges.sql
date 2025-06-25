-- Create user_0d_1 only if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Display all privileges granted to user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Create user_0d_2 only if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Display all privileges granted to user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
