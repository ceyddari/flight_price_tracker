from database import create_flight, list_flights, add_price, get_latest_price


def main():
    flight_id = create_flight(
        origin="IST",
        destination="AMS",
        departure_date="2025-02-10",
        airline="TestAir",
        url="https://example.com/flight/IST-AMS-2025-02-10",
    )
    print("Created flight id:", flight_id)

    flights = list_flights()
    print("All flights: ")
    for f in flights:
        print(f)

    price_id = add_price(flight_id, 3250.0, "TRY")
    print("Added price id: ", price_id)

    latest = get_latest_price(flight_id)
    print("Latest price record: ", latest)


if __name__ == "__main__":
    main()
