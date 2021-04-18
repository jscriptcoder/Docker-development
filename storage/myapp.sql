CREATE DATABASE IF NOT EXISTS myapp;

USE myapp;

CREATE TABLE IF NOT EXISTS process (
    id VARCHAR(32) NOT NULL, 
	started_on DATETIME, 
	ended_on DATETIME, 
    result VARCHAR(32), 
    PRIMARY KEY (id)
);