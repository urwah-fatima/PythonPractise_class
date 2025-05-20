class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.customers_served = 0  # renamed attribute
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cusine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
    
    def number_served(self):
        print(f"{self.restaurant_name} has served {self.customers_served} customers.")
    
    def set_number_served(self,coustomer_served):
        self.customers_served = coustomer_served
        print(f"{self.restaurant_name} has served {self.customers_served} customers.")

    def inc_number_served(self,NoOfCustomers):
        self.customers_served += NoOfCustomers
        print(f"{self.restaurant_name} has served {self.customers_served} customers.")

restaurant = Restaurant("B&B", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served()
restaurant.set_number_served(50)
restaurant.inc_number_served(200)