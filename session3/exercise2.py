shopping_cost = float(input('What is the total price of your shopping? '))
discount_applicable = input('Do you have a discount code? y/n ')
if discount_applicable == 'y':
    total_cost = shopping_cost * 0.9
elif shopping_cost == '100':
    total_cost = shopping_cost * 0.05
else:
    total_cost = shopping_cost
print(f'The total cost is {total_cost}')