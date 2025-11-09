# Author: Divyang Parikh
# # Date: 11/08/25
# Problem 6: Modify the given Car class to include 'type' and 'manufacturer' attributes and update methods accordingly.

# Attributes = Variables that store data about an object.
# Methods    = Functions defined inside a class that describe object behaviors.

class car:
    # The __init__() method runs when a new object is created.
    # It initializes all attributes of the class.
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model                # Attribute: model of the car
        self.year = year                  # Attribute: manufacturing year
        self.color = color                # Attribute: color of the car
        self.type = type                  # New attribute: car type (Sedan, SUV, Coupe, etc.)
        self.manufacturer = manufacturer  # New attribute: car manufacturer (like BMW, Toyota)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    # fullspecs() combines all information into a single readable string
    def fullspecs(self):
        return f"{self.model} {self.year} {self.color} {self.type} {self.manufacturer}"


car1 = car("Sports", 2012, "Blue", "Coupe", "BMW")
car2 = car("Sedan", 2020, "Black", "Luxury", "Mercedes")

print(car1.get_color())        # Expected output: Blue
print(car1.get_model())        # Expected output: Sports
print(car2.get_color())        # Expected output: Black

print(car1.fullspecs())        # Output: Sports 2012 Blue Coupe BMW
print(car2.fullspecs())        # Output: Sedan 2020 Black Luxury Mercedes
