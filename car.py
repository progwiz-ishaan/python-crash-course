prompt = f'Give the name of the rental car you would would like to rent'
prompt += '\nand I\'ll see if I can find you that car. '
cars = ['duster', 'toyota', 'minia', 'volkswagon', 'honda']
car = input(prompt).lower()

if car in cars:
    print(f'Here is your {car.title()}!')
else:
    print(f'Nope! I cannot give you the car {car.title()}.')