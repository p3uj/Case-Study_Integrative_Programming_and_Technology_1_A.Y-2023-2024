inputInteger = input("Enter a list of integer tuples separated by commas: ") # Example format: (6, 24, 12), (7, 9, 6), (12, 18, 21)

# Convert the input string to a list of tuples using eval() function.
list = eval("[" + inputInteger + "]")

# Print the original list.
print(f"The original list is : {list}")

# Initialize K with the input value.
K = int(input("Enter the value of K: "))

# Filter the elements using all() method.
result = [sub for sub in list if all(ele % K == 0 for ele in sub)]

print(f"K Multiple elements tuples : {result}")