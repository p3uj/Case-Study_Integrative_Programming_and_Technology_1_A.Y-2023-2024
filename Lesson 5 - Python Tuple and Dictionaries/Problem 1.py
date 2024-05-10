# Initialize the list with the given numbers.
tup = (1, 2, 3)

# Create a list using a for loop to iterate over each element of the tuple, generating a tuple of each element and its square.
output = [(num, num **2) for num in tup]

# Print the content of output.
print(output)
