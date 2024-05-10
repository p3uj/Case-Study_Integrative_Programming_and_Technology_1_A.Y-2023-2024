"""
Instruction: 
Write a program that will ask user to input a list of integer tuples.

- Ask also for another integer value and assign it to K.
- Output the tuple that are divisible by K.
"""

print("Enter numerical values for tuple (separate by space):")
while True:
    try:
        tuple1 = tuple([int(x) for x in input().split()]) # Map to map int() to each element
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")


try:
    k = int(input("Enter an integer: "))


except ValueError:
    print("Invalid input. Please enter an integer.")
   
tuple2 = [x for x in tuple1 if x % k == 0]
print("Elements divisible by", k, "are:", tuple2)