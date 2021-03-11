prompt = f'Tell me how many people are in your group and I can'
prompt += '\ntell you if you can have a seat or you\'ll have to wait. '

people = input(prompt)
people = int(people)

if people >= 8:
    print(f'You\'ll have to wait.')
else:
    print(f'Your seat is ready.')