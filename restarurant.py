class Restarurant:
    """A simple attempt to model a rest.."""

    def __init__(self, restarurant_name, veggi):
        """Initialize restarurant_name & veggi attributts."""
        self.name = restarurant_name
        self.is_veg = veggi

    def describe_restarurant(self):
        """Describe the restarurant."""
        print(f"This is {self.name.title()}!")
        if self.is_veg:
            print(f"{self.name.title()} is veg!")
        else:
            print(f"{self.name.title()} is non-veg!")

    def open_restarurant(self):
        """Print a message that the restarurant has opened."""
        print(f"{self.name.title()} has opened!")

my_restarurant = Restarurant('The BOOM restarurant', False)
my_restarurant.describe_restarurant()
my_restarurant.open_restarurant()