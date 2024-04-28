List = [8, 9, 10]

print("Initial list: ", List)

List[1] = 17
List += [4, 5, 6]
List.pop(0)
List.sort()
List *= 2
List.insert(3, 25)

print("Final list: ", List)