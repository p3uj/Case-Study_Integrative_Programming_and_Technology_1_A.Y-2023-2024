"""
Instruction: Write a program that repeatedly asks the user to enter product names and prices.

- Store all of these in a dictionary whose keys are the product names and whose values are the prices.
- When the user is done entering products and prices, allow them to repeatedly enter a product name
and print the corresponding price or a message if the product is not in the dictionary.
"""

products = {}


while True:
    product_name = input("Enter product name (Type 'done' to stop adding): ")
    if product_name.lower() == 'done':
        break
    price = float(input("Enter price for {}: ".format(product_name)))
    products[product_name] = price


while True:
    product_to_find = input("Enter a product name to find its price (or 'done' to exit): ")
    if product_to_find.lower() == 'done':
        break
    if product_to_find in products:
        print("Price of {} is ${:.2f}".format(product_to_find, products[product_to_find]))
    else:
        print("Product '{}' not found in the dictionary.".format(product_to_find))