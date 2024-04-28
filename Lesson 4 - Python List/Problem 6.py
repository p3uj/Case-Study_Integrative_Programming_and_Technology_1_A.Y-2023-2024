# Prompt the user to input an integer.
integer = int(input("Enter an integer: "))

# Initialize an empty list.
factors = []

# For loop to iterate numbers from 1 to the entered integer.
for i in range(1, integer + 1):
    if integer % i == 0: # Check if the current integer is a factor of the entered integer.
        factors.append(i) # If it is a factor, append it to the list.

# Print the integer and factors.
print(f"The factors of {integer} are: {factors}.")