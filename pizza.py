prompt = '\nEnter the topping you would like on your pizza.'
prompt += '\nEnter \'quit\' if you are done: '

topping = ''
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f'{topping.title()} added on your pizza!')