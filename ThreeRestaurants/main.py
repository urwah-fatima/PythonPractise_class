class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cusine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
    
Restaurant1 = Restaurant("B&B", "Italian")
print(f"Restaurant 1:")
Restaurant1.describe_restaurant()
Restaurant1.open_restaurant()

Restaurant2 = Restaurant("Saffron Ember", "Indian")
print(f"Restaurant 2:")
Restaurant2.describe_restaurant()
Restaurant2.open_restaurant()

Restaurant3 = Restaurant("Umami Lane", "Japnese Fusion")
print(f"Restaurant 3:")
Restaurant3.describe_restaurant()
Restaurant3.open_restaurant()