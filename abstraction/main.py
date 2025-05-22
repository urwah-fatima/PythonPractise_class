# Define a Car class with abstract and idle stop engine features
from rich import print

class Car:
    # Proper constructor with double underscores
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._engine_status = False      # Engine is initially off
        self._idling_time = 0            # Time the engine has been idling
        self._traffic_signal = None      # Traffic signal state (Red/Green)

    # Expose a drive method without revealing internal mechanics
    def drive(self):
        if self._engine_status and self._traffic_signal == "Green":
            print(f"You are driving a {self.brand} {self.model}.")
        elif self._traffic_signal == "Red":
            print(f"You stopped at the red light in a {self.brand} {self.model}.")
        else:
            self._start_engine()
            print(f"You are driving a {self.brand} {self.model}.")

    def stop(self):
        if self._engine_status:
            print(f"You stopped the {self.brand} {self.model}.")
            self._engine_status = False
        else:
            print(f"The {self.brand} {self.model} is already stopped.")

    # Expose a set_traffic_signal method to set the traffic signal
    def set_traffic_signal(self, signal):
        self._traffic_signal = signal.capitalize()  # Normalize input
        if self._traffic_signal == "Red":
            print(f"Traffic signal turned red. You stopped in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        elif self._traffic_signal == "Green":
            print(f"Traffic signal turned green. You can drive your {self.brand} {self.model}.")
            if not self._engine_status:
                self._start_engine()

    # Internal method to start the engine (hidden from user)
    def _start_engine(self):
        self._engine_status = True
        self._idling_time = 0
        print("Engine started.")

    # Internal method to stop the engine if idling for 5 seconds (hidden from user)
    def _idle_stop_engine(self):
        import time
        print("Engine is idling....")
        for i in range(5):
            print(f"Idling time: {i+1} seconds")
            time.sleep(1)
            self._idling_time += 1
        if self._idling_time >= 5:
            self._engine_status = False
            print("Engine stopped (idle stop) to save fuel.")


# Create a Car object and use the methods
my_car = Car("Toyota", "Camry")
my_car.set_traffic_signal("green")
my_car.drive()
my_car.set_traffic_signal("red")
my_car.set_traffic_signal("green")
my_car.drive()
