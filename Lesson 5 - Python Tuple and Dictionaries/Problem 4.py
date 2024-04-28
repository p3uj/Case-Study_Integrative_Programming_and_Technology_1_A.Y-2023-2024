# Initialize an empty dictionary.
products = {}

# Loop to add products and their prices.
while True:
    productName = input("Enter product name: ")
    productPrice = float(input(f"Enter price for {productName}: "))
    # Add the product name and price to the dictionary.
    products[productName] = productPrice

# Prompt the user if they want to add another product.
    addMore = input("Do you want to add another product? (Yes or No): ")
    if addMore.lower() == 'no': # If the user input is "no", then break the loop; Converts the user's input into lowercase.
        break

# Loop to search for product prices.
while True:
    query = input("Enter product name to get the price: ")
    # It will check if the product name is in dictionary.
    if query in products:
        print(f"Price of {query}: ${products[query]}")
    else:
        print("Product not found.")

    searchMore = input("Do you want to search another product? (Yes or No): ")
    if searchMore.lower() == 'no':
        break