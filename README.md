# Flight Price Tracker (Python + PostgreSQL)

A simple project that stores flights in PostgreSQL, fetches prices (currently random),
saves price history, and compares new vs old prices.

## Project Structure
- config.py (DB settings)
- database.py (insert/select operations)
- fetch_price.py (price generator placeholder)
- tracker.py (price checking logic)
- main.py (initial database test)

## Database Schema

-- flights table
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR(10) NOT NULL,
    destination VARCHAR(10) NOT NULL,
    departure_date DATE NOT NULL,
    airline VARCHAR(50),
    url TEXT NOT NULL
);

-- price_history table
CREATE TABLE price_history (
    id SERIAL PRIMARY KEY,
    flight_id INT NOT NULL REFERENCES flights(id) ON DELETE CASCADE,
    price NUMERIC(10,2) NOT NULL,
    currency VARCHAR(10) NOT NULL,
    checked_at TIMESTAMP DEFAULT NOW()
);

## How to Run
1. Install packages:
   pip install psycopg2-binary requests beautifulsoup4

2. Update config.py with your DB credentials.

3. Create the tables using the SQL above.

4. Test database connection:
   python main.py

5. Run the price tracker:
   python tracker.py

## Notes
- fetch_price.py currently returns a random price.
- Ready for real scraping and email alerts in the next step.
