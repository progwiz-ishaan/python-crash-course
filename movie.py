prompt = '\nEnter your age and I\'ll tell you how many $'
prompt += '\nyou\'ll have to pay to watch the movie.'
prompt += '\nPress [ENTER] to end: '

while True:
    age = input(prompt)

    if age == '':
        break

    age = int(age)

    if age < 3:
        print('FREE!!!')
    elif 3 <= age <= 12:
        print('It\'ll be $10')
    else:
        print('It\'ll be $15')