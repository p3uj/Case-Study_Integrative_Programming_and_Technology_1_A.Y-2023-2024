# Initialize the list.
given_list = [1, 1, 2, 3, 4, 3, 0, 0]

# remove the duplicates from the list using dictionary keys.
given_list = list(dict.fromkeys(given_list))

# Print the list without duplicates.
print(given_list)