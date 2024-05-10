"""
Instruction: Write a program that asks the user to enter size of list and input a list of integers. Do the following:
- Print the sum of items in the list.
- Print the last item in the list.
- Print the list in reverse order.
- Print Yes if the list contains a 5 and No otherwise.
- Print how many integers in the list are less than 5.
- Remove the first and last items from the list, sort the remaining items, and print the result.
"""

# Initialize an empty list.
list = []

# Prompt the user to enter the size of the list.
size_integers = int(input("Enter a size of the list: "))

# For loop for the integers to iterate the entered size.
for i in range(0, size_integers):
    integers = int(input("Enter an integer: "))
    list.append(integers)

# Display the list.
print(f"List: {list}")

# Calculate the total sum of the list using sum() function.
total = sum(list)
print(f"Total: {total}")

#  Retrieve and print the last integer stored in the list.
last = list[-1]
print(f"Last integer: {last}")

# Reverse the list using reverse() method.
list.reverse()
print(f"Reversed list: {list}")

# If and else statement for the size of 5.
print("Is 5 on the list?", end=" ")
if size_integers == 5:
    print("Yes")
else:
    print("No")

# For loop to count how many integers that are less than 5.
less_than = len([integers for integers in list if integers < 5])
print(f"Number of integers less than 5: {less_than}")

# Remove the first and last element using slice operator, with "1" indicating the first element and "-1" indicating the last element.
list = list[1:-1]
list.sort() # Sort the list using sort() method.

# Print the content of list.
print(f"Sorted list: {list}.")