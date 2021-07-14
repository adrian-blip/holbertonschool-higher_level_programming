-- Create the database hbtn_0d_usa and the table cities

CREATE DATABASE IF NOT EXITS hbtn_0d_usa;
CREATE TABLE If NOT EXITS hbtn_0d_usa.cities
(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY_KEY, state_id INT NOT NULL FOREIGN KEY(state_id), name VARCHAR(256) NOT NULL);