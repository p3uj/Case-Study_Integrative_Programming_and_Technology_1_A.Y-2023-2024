products = {}
print("Enter 'done' to the product to finish inputing.")
while True:
    productName = input("\nProduct: ").capitalize()

    if productName == 'Done':
        break
    
    try:
        productPrice = float(input("Price: "))
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        continue

    products[productName] = productPrice


print("\nEnter a product name to check its price (or type 'done' to exit)")
while True:
    userInput = input("\nProduct name: ").capitalize()

    if userInput == 'Done':
        break

    if userInput in products:
        print(f"{userInput} is ₱{products[userInput]:}")
    else:
        print(f"{userInput} is not found in the dictionary.")