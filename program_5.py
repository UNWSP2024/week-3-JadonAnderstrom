# There are two kinds of hot dogs sold:  
print('Hello, welcome to Quick Eats!')
print('Our menu today consists of two different options\n')
print('Option 1 is a Hot Dog - $3.50')
print('Option 2 is a Chilli Dog - $4.50')

# Hot Dog ($3.50), Chili Dog ($4.50).  
Hot_Dog = 3.5
Chilli_Dog = 4.5
Dog = int(input('Would you like Option 1 or 2? '))
print('\n')
if Dog == 1:
    print('Awsome, Hot Dog it is!')
    hot_dog_cost = Hot_Dog
if Dog == 2:
    print('Awsome, Chilli Dog it is!')
    hot_dog_cost = Chilli_Dog
    
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  e
cheese = input('Would you like cheese($0.50)? y/n:')
peppers = input('Would you like peppers($0.75? y/n:')
grilled_onions = input('Would you like grilled onions($1.00)? y/n:')
print('\n')

#topings calculations
toppings = 0
if cheese == 'y':
    toppings += .5
if peppers == 'y':
    toppings += .75
if grilled_onions == 'y':
    toppings += 1
# Also tax is 7%. 
tax_rate = 0.07
tax = (hot_dog_cost + toppings) * tax_rate
print('tax: $', format(tax, '.2f'))

sub_total = (hot_dog_cost + toppings)
print('Subtotal: $', format(sub_total,'.2f'))
print(' Food: $', format(hot_dog_cost,'.2f'))
print(' Topings: $', format(toppings,'.2f'))
print('\n')

total_cost = (hot_dog_cost + toppings + tax)
print('Total: $', format(total_cost,'.2f'))


# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
