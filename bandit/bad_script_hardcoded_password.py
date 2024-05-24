password = "my_password"


def login(username, entered_password):
    if entered_password == password:
        print("Login successful!")
    else:
        print("Invalid password.")


# Example usage
username = input("Enter your username: ")
entered_password = input("Enter your password: ")
login(username, entered_password)
