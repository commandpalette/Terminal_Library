CREATE DATABASE terminal_library;
USE terminal_library;
CREATE TABLE users (
name VARCHAR(255) NOT NULL,
contact INT NOT NULL,
id INT AUTO_INCREMENT,
UNIQUE KEY (name),
PRIMARY KEY (id));
CREATE TABLE  books (
id INT NOT NULL AUTO_INCREMENT,
author VARCHAR(255) NOT NULL,
name VARCHAR(255) NOT NULL,
publication VARCHAR(255) NOT NULL,
company VARCHAR(255) NOT NULL,
rented_date DATE, 
rented_user VARCHAR(255),
PRIMARY KEY (id),
FOREIGN KEY (id) REFERENCES users(id)
);

CREATE TABLE  admins (
username VARCHAR(255) NOT NULL,
pasword VARCHAR(255) NOT NULL,
UNIQUE KEY (username)
);
-- Will be used to enter the details at the time of booking
INSERT INTO admins (username, pasword) 
VALUES ('vinay' , 'admin') , ('ashwin' , 'ashwin') , ('admin' , 'admin');

SELECT * FROM admins;
-- Will be used to check the username and password 
SELECT * FROM admins WHERE username = "vinay" AND pasword = "admin";

-- For the null values supply the Null at the time of coding the main app
-- Check for the null values also in the database and make sure the SQL injection doesnot works in my App
DELETE FROM admins WHERE username = NULL;
-- Here the Curd operaton is ompleted

-- Join two diff tables to query the diff points whih are common with one anotehr

-- SELECT * FROM books;
-- JOIN books ON rented_user = users.name;  But the joining column has to be unique.  

-- Some other joins are inner join 
