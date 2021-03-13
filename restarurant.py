class Restarurant:
    """A simple attempt to model a rest.."""

    def __init__(self, restarurunt_name, veggi):
        self.name = restarurunt_name
        self.is_veg = veggi

    def describe_restarurunt(self):
        print(f"This is {self.name.title()} restarurunt!")
        if self.is_veg:
            print("This restarunt is veg!")
        else:
            print("This restrunt is non-veg!")

    def open_restrunt(self):
        print("This restarurunt has opened!")

