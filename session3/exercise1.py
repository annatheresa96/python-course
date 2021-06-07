price = float(input('What is the price of the shirt? '))
budget = price <= 25.00
print(f'Shirt is available within budget: {budget}')
colour = input('What is the colour of the shirt? ')
answer = colour == "Yellow"
print(f'Shirt is available within budget and correct colour: {budget and colour}')