factors = []
num = int(input("Enter an integer: "))

for x in range(1, num + 1):
    if num % x == 0:
        factors.append(x)

print(f"Factors of {num}: ", end=" ")
print(*factors, sep=',')