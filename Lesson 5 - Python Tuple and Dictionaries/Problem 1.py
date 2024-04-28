inputList = []
squaredList = []

while True:
    try:
        listSize = int(input("Enter how many elements the list will have: "))
        if listSize <= 0:
            print("List size must be greater than 0. Please try again.\n")
            continue
        print()
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.\n")

for x in range(listSize):
    while True:
        try:
            userInput = int(input(f"List element #{x+1}: "))
            inputSquare = userInput * userInput
            inputList.append(userInput)
            squaredList.append((userInput, inputSquare))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

print("\nList:", inputList)
print("Output:", squaredList)