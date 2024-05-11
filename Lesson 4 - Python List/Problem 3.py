"""
Instruction: Starting with the list of the previous exercise, write Python statements to do the following:
- Append “banana” and 67 to the list.
- Insert the value “dog” at position 3.
- Insert the value 909 at the start of the list.
- Find the index of “hi”.
- Count the number of 67s in the list.
- Remove the first occurrence of 67 from the list.
- Remove False from the list using pop and index
"""
from Problem_2 import my_list   # This allow us to access the file of Problem_2 and easily use the my_list variable.

print(" <-- Unchanged list\n")

# a. Append “banana” and 67 to the list.
my_list.append("banana")
my_list.append(67)
print(f"After appending 'banana' and 67: {my_list}")

# b. Insert the value "dog" at position 3.
my_list.insert(2, "dog")
print(f"After inserting the 'dog' at position 3: {my_list}")

# c. Insert the value 909 at the start of the list.
my_list.insert(0, 909)
print(f"After inserting 909 at the start of the list: {my_list}")

# d. Find the index of “hi”.
print("Index of 'hi':", + my_list.index("hi"))

# e. Count the number of 67s in the list.
print(f"Occurrences of 67: {my_list.count(67)}")

# f. Remove the first occurrence of 67 from the list.
my_list.remove(67)
print(f"After removal of the first occurrence of 67: {my_list}")

# g. Remove False from the list using pop and index
my_list.pop(4)
print(f"After removal of False using pop and index: {my_list}")