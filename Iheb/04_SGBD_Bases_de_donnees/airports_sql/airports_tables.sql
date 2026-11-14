DROP TABLE IF EXISTS Runways;
DROP TABLE IF EXISTS Airports;
DROP TABLE IF EXISTS Regions;
DROP TABLE IF EXISTS Countries;


CREATE TABLE Countries (
    id INT,
    code CHAR(2),
    name VARCHAR,
    continent VARCHAR
);

CREATE TABLE Regions (
    id INT,
    code VARCHAR,
    local_code VARCHAR,
    name VARCHAR,
    country CHAR(2)
);

CREATE TABLE Airports (
    id INT,
    code VARCHAR,
    name VARCHAR,
    type VARCHAR,
    latitude REAL,
    longitude REAL,
    altitude REAL,
    country VARCHAR,
    region VARCHAR,
    city VARCHAR
);



CREATE TABLE Runways (
    id INT,
    airport_id INT,
    type VARCHAR,
    length INT,
    width INT,
    lighted INT,
    closed INT
);

