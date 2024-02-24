-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table


CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
id INT PRIMARY KEY AUTO_INCREMENT,
state_id INT FOREIGN KEY (id) REFERENCES states(id),
name VARCHAR (256) NOT NULL
);
