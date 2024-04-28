userInput = input("Enter a list of integer tuples separated by commas (example: (1,2),(3,4),(5,6)):\n")

tupleList = eval(userInput)

k = int(input("\nEnter the value of K: "))

result = [sub for sub in tupleList if all(ele % k == 0 for ele in sub)]

if result:
    print("\nTuples divisible by", k, ":", result)
else:
    print("\nNo tuples divisible by", k)