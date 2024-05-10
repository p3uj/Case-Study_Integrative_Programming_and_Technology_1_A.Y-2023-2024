factors = []#intializes an empty list
num = int(input("Enter an integer: "))#accepts an integer user input to find its factor

for x in range(1, num + 1):#iterates from 1 to num to check if x is a factor of num
    if num % x == 0:
        factors.append(x)

print(f"Factors of {num}: ", end=" ")
print(*factors, sep=',')#prints the factors of num separated by comma