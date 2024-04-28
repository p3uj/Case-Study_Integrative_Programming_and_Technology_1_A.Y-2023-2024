user_credentials = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
    'user4': 'password4',
    'user5': 'password5',
    'user6': 'password6',
    'user7': 'password7',
    'user8': 'password8',
    'user9': 'password9',
    'user10': 'password10'
}

attempt = 0
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_credentials:
        if password == user_credentials[username]:
            print("\nLogin successful! You are now logged in to the system.")
            break
        else:
            print("Wrong password!\n")
            attempt = attempt + 1
            if(attempt > 3):
                print("Too many failed attempts! The program will now exit.")
                break
    else:
        print("Invalid username! You are not a valid user of the system.")
        break