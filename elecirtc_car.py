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

    def update_odometer(self, millage):
        if millage >= self.odometer_reading:
            self.odometer_reading = millage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battry:
    """A simple attempt to model a battry for a car."""
    def __init__(self, battry_size=75):
        """Initialize the battry's attributts."""
        self.battry_size = battry_size
    
    def describe_battry(self):
        """Print a statment describing the battry of the car."""
        print(f"This car has a {self.battry_size}-kWh battry.")

    def get_range(self):
        """Print a statment about what range this battry provids."""
        if self.battry_size == 75:
            range = 260
        elif self.battry_size == 100:
            range = 315

        print(f"This car can go {range} on full charge.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent car.
        Then initalze attributs speci. to an ele. car.
        """
        super().__init__(make, model, year)
        self.battry = Battry()