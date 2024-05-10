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