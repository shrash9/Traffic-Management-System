class TrafficSignalController:
    """
    A simple traffic signal controller that adjusts signal timings based on the number of vehicles detected.
    """

    def __init__(self):
        # Default timings in seconds
        self.green_time = 30
        self.red_time = 20
        self.yellow_time = 5

        # Timing limits
        self.max_green_time = 60
        self.min_green_time = 10

        self.max_red_time = 40
        self.min_red_time = 10

        self.max_yellow_time = 10
        self.min_yellow_time = 3

    def print_signal_timings(self):
        print("\nCurrent Traffic Signal Timings:")
        print(f"Green Signal Time:  {self.green_time} seconds")
        print(f"Red Signal Time:    {self.red_time} seconds")
        print(f"Yellow Signal Time: {self.yellow_time} seconds\n")

    def update_signal_timings(self, vehicle_count):
        # Green time logic
        if vehicle_count > 50:
            self.green_time = min(self.green_time + 5, self.max_green_time)
        elif vehicle_count < 10:
            self.green_time = max(self.green_time - 5, self.min_green_time)

        # Red time logic
        if vehicle_count > 30:
            self.red_time = min(self.red_time + 5, self.max_red_time)
        elif vehicle_count < 20:
            self.red_time = max(self.red_time - 5, self.min_red_time)

        # Yellow time logic
        if vehicle_count > 30:
            self.yellow_time = min(self.yellow_time + 1, self.max_yellow_time)
        elif vehicle_count < 20:
            self.yellow_time = max(self.yellow_time - 1, self.min_yellow_time)


def main():
    print("==== Traffic Signal Timing Adjustment ====\n")

    signal_controller = TrafficSignalController()
    signal_controller.print_signal_timings()

    try:
        vehicle_count = int(input("Enter the current vehicle count at the signal: "))
    except ValueError:
        print("Oops! Please enter a valid number for vehicle count.")
        return

    # Update timings based on input
    signal_controller.update_signal_timings(vehicle_count)

    # Display updated timings
    print("\nUpdated Timings Based on Vehicle Count:")
    signal_controller.print_signal_timings()


if __name__ == "__main__":
    main()
