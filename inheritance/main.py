# Base class representing a generic vehicle
class Vehicle:
    def __init__(self, color, speed):
        # Initialize vehicle properties
        self.color = color
        self.speed = speed

    def drive(self):
        # Method to display current driving speed
        print("Driving speed =", self.speed)

    def accelerate(self):
        # Method to increase speed by 10 units
        self.speed += 10


# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, color, speed):
        # Call parent class constructor using super()
        super().__init__(color, speed)


# Truck class inheriting from Vehicle
class Truck(Vehicle):
    def __init__(self, color, speed):
        # Call parent class constructor using super()
        super().__init__(color, speed)


# Create instances of Car and Truck
car = Car("Red", 120)  # Red car with initial speed 120
truck = Truck("Blue", 80)  # Blue truck with initial speed 80

# Display initial speed of the car
print("The speed of the car is")
car.drive()

# Accelerate the car 6 times (increasing speed by 10 each time)
for i in range(6):
    car.accelerate()

# Display final speed of the car after acceleration
print("The speed of the car after acceleration is")
car.drive()

# Display speed of the truck (unchanged since we didn't accelerate it)
print("The speed of the truck is")
truck.drive()