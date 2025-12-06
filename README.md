-- README.md

-- Flight Price Tracker (Python + PostgreSQL)

-- A simple system for tracking flight prices. 
-- Prices are fetched (currently random), stored in PostgreSQL, 
-- and compared with the previous value.

-- Structure
-- config.py       : DB settings
-- database.py     : Insert/select operations
-- fetch_price.py  : Price generator (placeholder for real scraping)
-- tracker.py      : Fetch price, save history, compare
-- main.py         : Initial database test

-- Database Schema

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR(10) NOT NULL,
    destination VARCHAR(10) NOT NULL,
    departure_date DATE NOT NULL,
    airline VARCHAR(50),
    url TEXT NOT NULL
);

CREATE TABLE price_history (
    id SERIAL PRIMARY KEY,
    flight_id INT NOT NULL REFERENCES flights(id) ON DELETE CASCADE,
    price NUMERIC(10,2) NOT NULL,
    currency VARCHAR(10) NOT NULL,
    checked_at TIMESTAMP DEFAULT NOW()
);

-- How to Run
-- 1) Install packages:
-- pip install psycopg2-binary requests beautifulsoup4

-- 2) Update config.py with DB credentials

-- 3) Create tables using SQL above

-- 4) Test database:
-- python main.py

-- 5) Track prices:
-- python tracker.py

-- Notes
-- - Real scraping can replace fetch_price.py
-- - Email alerts can be added when price drops
