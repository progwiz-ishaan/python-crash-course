class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributs to make a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formated name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statment show the car's millage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('duster', 'renualt', '2012-2013')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()