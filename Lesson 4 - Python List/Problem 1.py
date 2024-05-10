"""
Problem 1: Define the variables x and y as lists of numbers
- x=[1, 2, 3, 4, 5]
- y=[11, 12, 13, 14, 15]
- z=[21, 22, 23, 24, 25]

#3*x multiplies the list x three times
a. What is the value of 3*x?
answer: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

#x+y concatinates the lists x and y
b. What is the value of x+y?
answer: [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]

#x-y is not valid for lists
c. What is the value of x-y?
answer: ERROR.

#x[1]accesses the second element of the list x
d. What is the value of x[1]?
answer: 2

#x[0] accesses the first of the list x
e. What is the value of x[0]?
answer: 1

#x[-1] accesses the last element of the list x
f. What is the value of x[-1]?
answer: 5

#a slice that selects all the elements of the list x
g. What is the value of x[:]?
answer: [1, 2, 3, 4, 5]

#slices the list from index 2 to, but not including, index 4
h. What is the value of x[2:4]?
answer: [3, 4]

#slices the list from index 1, but not including, index 4 with a step size of 2
i. What is the value of x[1:4:2]?
answer: [2, 4]

#slices the list from the first index to, but not including, index 4
j. What is the value of x[:2]?
answer: [1, 2]

#a slice that selects all the elements of the list with a step of 2
k. What is the value of x[::2]?
answer: [1, 3, 5]

#x[3] sets the element in the 4th position to 8
l. What is the result of the following two expressions?
x[3]=8 
print x
answer: [1, 2, 3, 8, 5]
"""