class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cusine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
    
Restaurant1 = Restaurant("B&B", "Italian")
Restaurant1.describe_restaurant()
Restaurant1.open_restaurant()