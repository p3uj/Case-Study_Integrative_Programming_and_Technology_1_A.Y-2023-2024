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