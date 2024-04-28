size = int(input("Enter the size of the list: "))
user_list = []
for i in range(size):
    user_input = int(input("Enter an integer: "))
    user_list.append(user_input)

# a.
print("Sum of items:", sum(user_list))

# b.
print("Last item:", user_list[-1])

# c.
print("Reversed list:", user_list[::-1])

# d.
if 5 in user_list:
    print("Yes")
else:
    print("No")

# e.
count_less_than_5 = sum(1 for num in user_list if num < 5)
print("Number of integers less than 5:", count_less_than_5)

# f.
user_list.pop(0)
user_list.pop()
user_list.sort()
print("Sorted list after removing first and last items:", user_list)