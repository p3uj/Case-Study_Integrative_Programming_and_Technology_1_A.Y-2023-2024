list = []

# Prompt the user to enter the size of the list.
size_integers = int(input("Enter a size of the list: "))

# For loop for the integers to iterate the entered size.
for i in range(0, size_integers):
    integers = int(input("Enter an integer: "))
    list.append(integers)

# Display the list
print(f"List: {list}")

# Sum of the list.
total = sum(list)
print(f"Total: {total}")

# Last item in the list.
last = list[-1]
print(f"Last integer: {last}")

# Reverse the list.
list.reverse()
print(f"Reversed list: {list}")

# If and else statement for the size of 5.
if size_integers == 5:
    print("Yes")
else:
    print("No")

# For loop to count how many integers that are less than 5.
less_than = len([integers for integers in list if integers < 5])
print(f"Number of integers less than 5: {less_than}")

# Remove the first and last element using slice operator.
list = list[1:-1]
list.sort() # Sort the list.

# Print the list.
print(f"Sorted list: {list}.")