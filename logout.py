users = {
    "user1": "password123",
    "user2": "banking456"
}

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
            break 
        else:
            print("\nInvalid choice, please try again.")

login()
