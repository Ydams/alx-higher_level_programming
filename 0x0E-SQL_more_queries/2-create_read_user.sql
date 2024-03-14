-- A script in mysql that creates the database hbtn_0d_2 and the user user_0d_2.
-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user with select privileges on the database
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

