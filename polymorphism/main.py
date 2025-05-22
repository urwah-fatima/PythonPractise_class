# Base class Animal that defines a common interface
class Animal:
    def speak(self):
        # Base method that will be overridden by child classes
        print("Animal speaks")

# Dog class inheriting from Animal
class Dog(Animal):
    def speak(self):
        # Override the speak method to provide dog-specific behavior
        print("Dog barks")

# Cat class inheriting from Animal
class Cat(Animal):
    def speak(self):
        # Override the speak method to provide cat-specific behavior
        print("Cat meows")

# Create a list of different animal objects
# This demonstrates polymorphism as we can treat different animal types uniformly
animals = [Dog(), Cat()]

# Iterate through the list and call speak() on each animal
# Each animal will respond with its own specific implementation
for animal in animals:
    animal.speak()   # Polymorphism in action - same method call, different behaviors
