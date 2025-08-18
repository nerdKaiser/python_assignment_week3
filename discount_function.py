#Creating the function to calculate discount and determine whether it is applicable
def calculate_discount(price, discount_percent): 
	if discount_percent >= 20:
		return price * (1 - discount_percent / 100)
	else:
		return price

#Calling the function after user prompt
price= float(input("Enter the price:"))
discount_percent = float(input("Enter the discount percentage:"))
print(f"The final price is: Sh {calculate_discount(price, discount_percent)}")

