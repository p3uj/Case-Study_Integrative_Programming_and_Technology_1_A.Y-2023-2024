# Create an empty list and add items using append method and concatenation
my_list = []
my_list.append(67)
my_list.append(62.9)
my_list.append("hi")
my_list.append(False)
my_list = my_list + [8, 67, 'apple', 6.5]

# a.
my_list.append("banana")
my_list.append(67)
# b.
my_list.insert(3, "dog")
# c.
my_list.insert(0, 909)
# d.
hi_index = my_list.index("hi")
# e.
count_67 = my_list.count(67)
# f.
my_list.remove(67)
# g.
false_index = my_list.index(False)
my_list.pop(false_index)
print(my_list)