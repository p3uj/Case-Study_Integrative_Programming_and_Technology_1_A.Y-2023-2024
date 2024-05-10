"""
Instruction: Create a list with the following six items: 67, 62.9, “hi”, False, 8, 67, 'apple', 6.5.
- Begin with the empty list shown below, and add 8 statements to add each item, one per item.
- The first four statements should use the append method to append the item to the list, and the last four statements should use concatenation.
"""

# Initialize an empty list.
my_list = []

# append() method to add one per item.
my_list.append(67)
my_list.append(62.9)
my_list.append("hi")
my_list.append(False)

# Concatenate the list with elements using "+" operator.
my_list = my_list + [8]
my_list = my_list + [67]
my_list = my_list + ['apple']
my_list = my_list + [6.5]

# Print the content of my_list.
print(my_list)