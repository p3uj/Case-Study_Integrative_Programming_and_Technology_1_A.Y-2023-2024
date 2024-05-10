List = []#initializes an empty list
listSize = int(input("Enter the size of the list: "))#accepts user input to determine the size of the list
for x in range(listSize):#takes user input and append it to the list for a range based off of the listSize
    List.append(int(input(f"Enter an integer for List[{x}]: ")))

print("\nList: ", List)#prints the list
print("\nSum of items in the list: ", sum(List))#displays the sum of the elements in the list that was added using sum method
print("The last item in the list: ", List[-1])#prints the last item in the list
print("The list in reverse order: ", List[::-1])#prints the list starting from the last element to the first
print("Is 5 on the list?", end=" ")
if 5 in List:#check for the occurence of five in the list
    print("Yes")
else:
    print("No")
lessFive = 0#initilized to 0 to assume there is no 5 in the list
for num in List:#traverses the list to check for numbers less than 5
    if num < 5:
        lessFive += 1
print("Integers less than 5: ", lessFive)
#removes the first and last elements in teh last using remove method
List.remove(List[0])
List.remove(List[-1])
List.sort()#used the sort method to sort the list in ascending order

print("\nSorted list without the first and last item: ", List)# displays the output