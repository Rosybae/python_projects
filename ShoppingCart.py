# I added quantity of items, this will prompt the user to select the quantity of items which will be displayed

print("Welcome to the Shopping Cart Program!")
print()
print("""
    Please select one of the following:
    -----------------------------------
    1. Add item
    2. View Cart
    3. Remove item
    4. Compute total
    5. Quit
    
    """)

shopping_cart = []
prices = []
qntys = []

option = int(input("Please enter an action: "))

while option != 5 and option != "Quit":
    if option == 1:        
        item = input("\nWhat item would you like to add? ")
        shopping_cart.append(item)
        qnty =  int(input(f"\nPlease enter the quantity of '{item}' : "))
        qntys.append(qnty)
        price =  float(input(f"\nWhat is the price of '{item}' ? "))
        prices.append(price)
        print(f"\n'{item}' has been added to the cart.")
   
               
    elif option == 2:        
        print("\nThe contents of the shopping cart are: ")
        for item in range(len(shopping_cart)):
            print(f"\n{item+1}. {shopping_cart[item]} - ${prices[item]:.2f} - {qntys[item]} pieces")
    
    elif option == 3:
        remove_item = int(input("\nPlease, which item would you like to remove? ")) -1
        del(shopping_cart[remove_item] )
        del(prices[remove_item])
        del(qntys[remove_item])        
        print(f"\n{remove_item}. Item removed")
        
    elif option == 4:
        sum = 0       
        for number in prices:
            sum += number
        print(f"\nThe total price of the items in the shopping cart is $ {sum:.2f}")        
  
        
    option = int(input("\nPlease enter an action: "))
else:
    print("\nThank you. Goodbye.")
        
    
