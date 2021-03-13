"""A set of classes that can be used to represent elecric cars."""

from car import Car

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