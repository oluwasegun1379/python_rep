--  In SQL, a relational database is required because the data in the table is related
-- Each table contains row and columns containing data
-- Each column contains column name and column value and each row is called the record
-- The collection of tables in a database is called the schema  so we can say we are scheming when designing a database
-- First, a server is connected to the database management system(DBMS) and we create a database using the cmd CREATE DATABASE and we specify the database name.
CREATE DATABASE social_network;

-- Next, we need to fill the database with some tables, using CREATE TABLE and specify the name of the table and infos in the parenthesis.
CREATE TABLE users (
    user_id int, -- 1st column
    first_name VARCHAR(100), -- 2nd column
    last_name VARCHAR(100), -- 3nd column
    email VARCHAR(255), -- 4th column
); -- SQL command generally ends with semi-colons

-- We can make changes in a previously created tables in a database with the cmd ALTER TABLE and then name of the table
ALTER TABLE users ADD encrypted_password VARCHAR(1000); -- The ALTER TABLE ADD added a new column to the users table

ALTER TABLE users DROP COLUMN encrypted_password; -- The ALTER TABLE DROP delete encrypted_password column from users table

DROP TABLE users; -- The ALTER TABLE DROP users deletes the table 'users'

DROP DATABASE users; -- The DROP DATABASE users deletes the entire database

-- Now we can insert some information into the database variables using the cmd INSERT INTO then the table
-- name followed corresponding variables then the VALUES followed by the corresponding infos

INSERT INTO users (user_id, first_name, last_name, email)
VALUES (1, 'Shakiru', 'Oluwasegun', 'oluwase@gmail.com');

-- To look at the data we have created, we can use the cmd SELECT * FROM users
SELECT * FROM users -- This cmd will display all the users database information

SELECT  first_name FROM users; -- This cmd will display only the first_name infos in the users database
SELECT user_id last_name FROM users; -- This cmd will display the user_id and last_name infos in the users database

-- We can select from the table using particular order with the ORDER followed by one the column name
SELECT user_id, last_name FROM users ORDER BY user_id; -- This will will arrange it in ascending order

SELECT user_id, last_name FROM users ORDER BY user_id DESC; -- This will will arrange it in descending order

-- We can change existing data with the UPDATE statement
UPDATE users SET last_name = Yusuf WHERE user_id = 1; -- This will update the last_name Oluwasegun to Yusuf where user-id = 1

-- To get rid of data, we can use the cmd DELETE FROM statement followed by the table name followed by the
-- WHERE statement followed by the record to delete
DELETE FROM user WHERE last_name = 'Yusuf';

-- Use the SELECT statement to confirm your updates
SELECT * FROM user

-- we can use use >, <, <=, >= and = to select records
SELECT * FROM user WHERE user_id > 0 AND user_id <= 5

-- So far, we can scheme database using the following essential sql cmd; CREATE, ALTER, and DROP

-- and the statement used when working with data; SELECT, INSERT, UPDATE and DELETE