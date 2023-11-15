-- Create MySQL server user user_0d_2 if it doesn't exist and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';;

-- Create database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
