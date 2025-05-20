class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
    
    def describe_user(self):
        print("User Profile")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

User1 = User("Alice", "Smith", 30, "alice@example.com", "New York")
print("User1 Profile:")
User1.describe_user()
User1.greet_user()

User2 = User("Bob", "Johnson", 25, "bob@example.com", "Los Angeles")
print("User2 Profile:")
User2.describe_user()
User2.greet_user()

User3 = User("Charlie", "Brown", 35, "charlie@example.com", "Chicago")
print("User3 Profile:")
User3.describe_user()
User3.greet_user()