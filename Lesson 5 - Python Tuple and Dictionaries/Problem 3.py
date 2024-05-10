"""
Instruction: Here is a dictionary of the days in the months of the year:
- days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 
'September':30, 'October':31, 'November':30, 'December':31}

a. Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
b. Print out all of the keys in alphabetical order.
c. Print out all of the months with 31 days.
d. Print out the (key-value) pairs sorted by the number of days in each month
"""

days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31,
        'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31,
        'November': 30, 'December': 31}


month_name = input("Enter a month name: ").capitalize()


if month_name in days:
    print(f"There are {days[month_name]} days in {month_name}.")
else:
    print("Invalid.")


print("\nAll months in alphabetical order: ")
for month in sorted(days.keys()):
    print(month)


print("\nMonths with 31 days: ")
for months, day in days.items(): # months = key, day = value
    if day == 31:
        print(months)


print("\nMonths sorted by the number of days: ")
sorted_months = sorted(days.items(), key=lambda x: x[1]) #key=lambda x: x[1] sort based on days
for month, day in sorted_months:
    print(f"{month}: {day} days")