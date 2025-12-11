def expected_elevator_stops(passengers=12, floors=10):
    num_repetitions = 100000
    total_stops = 0
    import random
    for _ in range(num_repetitions):
        stops = set()
        for i in range(passengers):
            stop_floor = random.randint(1, floors)
            stops.add(stop_floor)
        total_stops += len(stops)
    expected_stops = total_stops / (num_repetitions)
    return expected_stops, floors * (1 - ((floors - 1) / floors) ** passengers)

def main():
    expected_simulation, expected_mathematical = expected_elevator_stops()
    print(f"Expected Elevator Stop Floor (Simulation): {expected_simulation}")
    print(f"Expected Elevator Stop Floor (Mathematical): {expected_mathematical}")

if __name__ == "__main__":
    main()