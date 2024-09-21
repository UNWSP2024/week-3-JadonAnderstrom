# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    ######################
weight = float(input('Enter the weight of the package: '))

if weight <= 2:
    print ('Shipping charge: $1.50')
    
elif 2 < weight <= 6:
    print ('Shipping charge: $3.00')
    
elif 6 < weight <= 10:
    print ('Shipping charge: $4.00')
    
elif weight > 10:
    print ('Shipping charge: $4.75')
    ######################
    
    return shippingCost

