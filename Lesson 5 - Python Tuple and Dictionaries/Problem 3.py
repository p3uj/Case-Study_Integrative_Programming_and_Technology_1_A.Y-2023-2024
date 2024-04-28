days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

month = input("Enter a month name: ").capitalize()

if month in days:
    print(f"{month} has {days[month]} days.")
else:
    print(f"Invalid input. {month} is not a month")

sortedKeys = sorted(days.keys())
print("\nAll the keys in alphabetical order:")
for month in sortedKeys:
    print(month)

with31Days = []
for month, monthDays in days.items():
    if monthDays == 31:
        with31Days.append(month)
print("\nMonths with 31 days:")
for month in with31Days:
    print(month)

sortedValue = sorted(days.items(), key=lambda x: x[1])
print("\nMonths sorted by the number of days:")
for month, days in sortedValue:
    print(month, "-", days)