# I added 2 inputs in line 8 and 9

child_meal = float(input("What is the price of a child's meal?"))
adult_meal = float(input("What is the price of a adult's meal?"))
num_of_childen = int(input("How many children are there?"))
num_of_adult = int(input("How many adults are there?"))
tax_rate = float(input("What is the sales tax rate?"))
drink_price = float(input("What is the price of drinks?"))
appetizer_price = float(input("What is the price of appetizers?"))

subtotal = num_of_childen * child_meal + num_of_adult * adult_meal + drink_price + appetizer_price
sales_taxes = subtotal * tax_rate / 100
total = subtotal + sales_taxes
payment_amount = float(input("What is the payment amount?"))
change = payment_amount - total

print((f"Subtotal is: ${subtotal:.2f}"))
print((f"Sales tax is: ${sales_taxes:.2f}"))
print((f"Total is: ${total:.2f}"))
print(f"Change is: ${change:.2f}")