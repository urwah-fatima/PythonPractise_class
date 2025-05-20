class User():
    def __init__(self, first_name, last_name, email, age):
     self.first_name = first_name
     self.last_name = last_name
     self.email = email
     self.age = age

    def describe_user(self):
      print("User Profile")
      print(f"Name: {self.first_name} {self.last_name}")
      print(f"Age: {self.age}")
      print(f"Email: {self.email}")

class Privileges():
   def __init__(self):
      self.privileges =[
         "can add post",
         "can delete post",
         "can be user"
      ]

def show_privileges(self):
    print("Admin Privileges:")
    for privilege in self.privileges:
        print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = Privileges()


admin_user = User("Alice", "Smith", "alice@example.com", 30)
admin_user.describe_user()
admin_user_privileges = Privileges()