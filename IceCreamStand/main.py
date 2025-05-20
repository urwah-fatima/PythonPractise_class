class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type}.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Vanilla", "Strawberry", "Blueberry", "Coffee", "Pistachio", "Mango"]

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print("- " + flavor)


# Create an instance
ice_cream_shop = IceCreamStand("Cool Treats", "Ice Cream")

# Test methods
ice_cream_shop.describe_restaurant()
ice_cream_shop.display_flavors()
