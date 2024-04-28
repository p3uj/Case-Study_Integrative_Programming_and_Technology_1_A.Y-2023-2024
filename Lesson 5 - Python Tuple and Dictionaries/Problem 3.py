# Initialize a dictionary
daysInMonths = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 30, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

month = input("Enter name of month: ")

# It will check if the entered month exists in the dictionary.
if month in daysInMonths:
    print(f"There are {daysInMonths[month]} days in {month}")
else:
    print("Please enter the correct month.")

# Print the months in alphabetical order.
print("Months in alphabetical order are: ", sorted(daysInMonths))

# Print the months with 31 days.
print("Months with 31 days:", end=" ")
for i in daysInMonths:
    if daysInMonths[i] == 31:
        print(i, end=" ")

# Create a list containing the number of days and the month.
daysMonthList = []
for i in daysInMonths:
    daysMonthList.append([daysInMonths[i], i])
daysMonthList.sort() # Sort the list by the number of days.

# Create a new list containing the month and the number of days.
monthDayList =[]
for i in daysMonthList:
    monthDayList.append([i[1], i[0]]) # Append a new list; Month: i[1]; Days: i[0]

# Convert the list back into a dictionary.
sortedDaysInMonths = dict(monthDayList)
print("\nMonths sorted by days:", sortedDaysInMonths)