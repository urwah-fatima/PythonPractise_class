# Define a class named Car
class Car:
    # Constructor method to initialize the car's attributes
    def __init__(self, color, speed):
        self.color = color            # Public attribute to store the car's color
        self.__speed = speed          # Private attribute to store the car's speed (not directly accessible from outside)

    # Method to increase the speed of the car by 10
    def accelerate(self):
        self.__speed += 10

    # Method to retrieve the current speed of the car
    def get_speed(self):
        return self.__speed


# Create an instance of the Car class with color "Nissan" and initial speed 0
car = Car("Nissan", 0)

# Print the current speed of the car by calling the get_speed() method
print("Current speed:", car.get_speed())

# Accelerate the car 10 times, each time increasing speed by 10
for i in range(10):
    car.accelerate()

# Print the speed after accelerating 10 times (expected: 100)
print("Speed after acceleration:", car.get_speed())
