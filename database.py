import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def get_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    return conn


def create_flight(origin, destination, departure_date, airline, url):
    conn = get_connection()
    cur = conn.cursor()
    query = """
        INSERT INTO flights(origin, destination, departure_date, airline, url)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;    
    """
    cur.execute(query, (origin, destination, departure_date, airline, url))
    flight_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return flight_id


def list_flights():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM flights ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def add_price(flight_id, price, currency):
    conn = get_connection()
    cur = conn.cursor()
    query = """
        INSERT INTO price_history (flight_id, price, currency)
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    cur.execute(query, (flight_id, price, currency))
    price_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return price_id


def get_latest_price(flight_id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query = """
        SELECT *
        FROM price_history
        WHERE flight_id = %s
        ORDER BY checked_at DESC
        LIMIT 1;
    """
    cur.execute(query, (flight_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row
