#Creating the function to calculate discount and determine whether it is applicable
def calculate_discount(price, discount_percent): 
	if discount_percent >= 20:
		return price * (1 - discount_percent / 100)
	else:
		return price

#Calling the function with example values
#Example usage case 1
print(calculate_discount(5000, 22))

#Example usage case 2
print(calculate_discount(7000, 12))
