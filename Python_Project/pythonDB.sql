CREATE DATABASE PythonSQL;
USE PythonSQL;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

SELECT * FROM users;
