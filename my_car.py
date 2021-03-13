from car import Car
from electric_car import ElectricCar

my_duster = Car('duster', 'renualt', '2019')
print(my_duster.get_descriptive_name())

my_telesa = ElectricCar('telesa', 'roadster', 2021)
print(my_telesa.get_descriptive_name())