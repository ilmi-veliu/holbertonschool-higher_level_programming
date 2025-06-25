-- List all privileges of user_0d_1 and user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
SHOW GRANTS FOR 'user_0d_1'@'localhost';

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
