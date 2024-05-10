#declares a list with its elements as 8, 9, and 10
List = [8, 9, 10]
#prints the initial list
print("Initial list: ", List)
#sets the second element to 17 turning the list 
#from [8, 9, 10] to [8, 17, 10]
List[1] = 17
#appends 4,5, and 6 to the list [8, 17, 10, 4, 5, 6]
List += [4, 5, 6]
#removes the first element of the list [17, 10, 4, 5, 6]
List.pop(0)
#sorts the list in ascending order [4, 5, 6, 10, 17]
List.sort()
#doubles the list [4, 5, 6, 10, 17, 4, 5, 6, 10, 17]
List *= 2
#inserts 35 to the 4th position [4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17]
List.insert(3, 25)
#prints the final list
print("Final list: ", List)
