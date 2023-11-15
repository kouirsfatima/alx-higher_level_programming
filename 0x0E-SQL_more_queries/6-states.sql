-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table states in the database hbtn_0d_usa
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    `id` INT DEFAULT 1 NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    UNIQUE (`id`)
);
