"""
Instruction: Start with the list [8,9,10]. Do the following:
- Set the second entry (index 1) to 17
- Add 4, 5, and 6 to the end of the list
- Remove the first entry from the list
- Sort the list
- Double the list f. Insert 25 at index 3
- The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
"""

List = [8, 9, 10]#declares a list with its elements as 8, 9, and 10

print("Initial list: ", List)#prints the initial list

List[1] = 17#sets the second element to 17 turning the list from [8, 9, 10] to [8, 17, 10]
List += [4, 5, 6]#appends 4,5, and 6 to the list [8, 17, 10, 4, 5, 6]
List.pop(0)#removes the first element of the list [17, 10, 4, 5, 6]
List.sort()#sorts the list in ascending order [4, 5, 6, 10, 17]
List *= 2#doubles the list [4, 5, 6, 10, 17, 4, 5, 6, 10, 17]
List.insert(3, 25)#inserts 35 to the 4th position [4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17]

print("Final list: ", List)#prints the final list