# Initialize an empty list.
my_list = []

# Append method to add one per item.
my_list.append(67)
my_list.append(62.9)
my_list.append("hi")
my_list.append(False)

# Concatenation
my_list = my_list + [8]
my_list = my_list + [67]
my_list = my_list + ['apple']
my_list = my_list + [6.5]

# Append banana and 67 to the list.
my_list.append("banana")
my_list.append(67)

# Insert dog at index 3.
my_list.insert(3, "dog")

# Insert 909 at  index 0.
my_list.insert(0, 909)

# Find the index of "hi"
index = my_list.index("hi")
print(f"Index of hi: {index}")

# Count the number of 67s in the list
count_67 = my_list.count(67)
print(f"Count 67: {count_67}")
# Remove the first 67
my_list.remove(67)
# Remove the False using pop() at index 4.
my_list.pop(4)
# Print the list.
print(my_list)
