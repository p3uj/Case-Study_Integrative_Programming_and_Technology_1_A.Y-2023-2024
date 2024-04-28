List = []
listSize = int(input("Enter the size of the list: "))
for x in range(listSize):
    List.append(int(input(f"Enter an integer for List[{x}]: ")))

print("\nList: ", List)
print("\nSum of items in the list: ", sum(List))
print("The last item in the list: ", List[-1])
print("The list in reverse order: ", List[::-1])
print("Is 5 on the list?", end=" ")
if 5 in List:
    print("Yes")
else:
    print("No")
lessFive = 0
for num in List:
    if num < 5:
        lessFive += 1
print("Integers less than 5: ", lessFive)

List.remove(List[0])
List.remove(List[-1])
List.sort()

print("\nSorted list without the first and last item: ", List)