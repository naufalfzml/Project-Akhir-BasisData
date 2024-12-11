CREATE DATABASE EXAMPLE

USE EXAMPLE

SELECT @@servername

-- Single
CREATE TABLE TableA(
    id INT IDENTITY,
    name VARCHAR(32),
)

-- 1 to 1
CREATE TABLE TableBC (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(32),
    id_cb INT UNIQUE
);

CREATE TABLE TableCB (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(32),
    id_bc INT UNIQUE,
    FOREIGN KEY (id_bc) REFERENCES TableBC(id)
);

-- Add the foreign key for TableBC after TableCB is created
ALTER TABLE TableBC
ADD FOREIGN KEY (id_cb) REFERENCES TableCB(id);

-- 1 to many
CREATE TABLE TableDE(
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(32)
);

CREATE TABLE TableEDMany(
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(32),
    id_de INT,
    FOREIGN KEY (id_de) REFERENCES TableDE(id)
);

-- many to many
CREATE TABLE TableFGMany(
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(32)
);

CREATE TABLE TableGFMany(
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(32)
);

CREATE TABLE PivotFG(
    id_fg INT, -- Foreign key to TableFGMany
    id_gf INT, -- Foreign key to TableGFMany
    PRIMARY KEY (id_fg, id_gf), -- Composite primary key to ensure uniqueness
    FOREIGN KEY (id_fg) REFERENCES TableFGMany(id),
    FOREIGN KEY (id_gf) REFERENCES TableGFMany(id)
);

SELECT * FROM TableBC