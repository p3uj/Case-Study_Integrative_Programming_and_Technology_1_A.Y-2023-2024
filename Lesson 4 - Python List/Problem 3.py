List = []

List.append(67)
List.append(62.9)
List.append("hi")
List.append(False)

List += [8]
List += [67]
List += ['apple']
List += [6.5]

List.append("banana")
List.append(67)

List.insert(3, "dog")
List.insert(0, 909)

print()
print(List)
print('Index of "hi": ', List.index("hi"))
print("Count of 67s in the list: ", List.count(67))

List.remove(67)
List.pop(List.index(False))

print()
print(List)