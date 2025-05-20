class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # New attribute

    def describe_user(self):
        print("User Profile")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Login Attempts: {self.login_attempts}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Example usage
User1 = User("Alice", "Smith", 30, "alice@example.com", "New York")

# Simulate login attempts
User1.increment_login_attempts()
User1.increment_login_attempts()
User1.increment_login_attempts()

print("After 3 login attempts:")
User1.describe_user()

# Reset login attempts
User1.reset_login_attempts()
print("\nAfter resetting login attempts:")
User1.describe_user()
