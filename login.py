def login(username, password):
    """
    A simple login function that checks if the provided username and password
    are correct. This is a mock function for demonstration purposes.
    """
    correct_username = "user1"
    correct_password = "password123"

    if username == correct_username and password == correct_password:
        return "Login successful!"
    else:
        return "Invalid username or password."
