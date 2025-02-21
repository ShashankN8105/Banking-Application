# Simple Banking Login System with Logout

# Sample user database (username: password)
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
        dashboard(username)
    else:
        print("\nInvalid username or password. Please try again.")
        login()  # Retry login

def dashboard(username):
    while True:
        print("\n--- Dashboard ---")
        print("1. View Balance")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nYour balance is $10,000 (Demo)")
        elif choice == "2":
            print("\nLogging out... Goodbye, " + username + "!")
            break  # Exit the loop and logout
        else:
            print("\nInvalid choice, please try again.")

# Run the login function
login()
