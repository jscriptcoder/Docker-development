CREATE DATABASE IF NOT EXISTS myapp;

USE myapp;

CREATE TABLE IF NOT EXISTS process (
    id VARCHAR(32) NOT NULL, 
    result VARCHAR(32), 
    PRIMARY KEY (id), 
    CHECK (done IN (0, 1))
);