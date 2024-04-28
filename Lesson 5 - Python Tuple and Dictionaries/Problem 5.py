user_with_password = {"User1": "password1", "User2": "password2", "User3": "password3", "User4": "password4", "User5": "password5", "User6": "password6", "User7": "password7", "User8": "password8", "User9": "password9", "User10": "password10"}

username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the entered username is in dictionary.
if username in user_with_password:
    if user_with_password[username] == password:
        print(f"Login successful. Welcome, {username}!") # If the password matches.
    else:
        print("Invalid password.") # If the password is wrong or doesn't match.
else:
    print("User not found.") # If username is not in dictionary.