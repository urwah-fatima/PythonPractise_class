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

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = ["can add post", "can delete post", "can be user"]

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

User = User("Alice", "Smith", 30, "alice@example.com", "New York")
print("User1 Profile:")
User.describe_user()
User.greet_user()

Admin = Admin("Charlie", "Brown", 35, "charlie@example.com", "Chicago")
print("\nAdmin Profile:")
Admin.describe_user()