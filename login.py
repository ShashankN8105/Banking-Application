users = {
    "user1": "password123",
    "user2": "banking456"
}

def login():
    print("Welcome to the Banking Application")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("\nLogin successful! Welcome,", username)
    else:
        print("\nInvalid username or password. Please try again.")

login()
