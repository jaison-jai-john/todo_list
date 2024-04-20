from string import punctuation


def login(users: dict):
    # get user credentials
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    # check if user exists
    user = users.get(user_name)

    # user does not exist
    if not user:
        ch = input("do you want to retry? (y/n): ").lower()
        if ch == "y":
            return login(users)
        else:
            return

    # user exists
    while True:
        # check if password is correct
        if user["password"] == password:
            # login
            print("Login successful")
            return user
        # password is incorrect
        else:
            # ask the user if he wants to retry
            ch = input("Wrong password. Do you want to retry? (y/n): ").lower()
            if ch == "n":
                break


def sign_up(users: dict):
    while True:
        username = input("Enter your username: ")
        # username length less than 15
        if len(username) > 15:
            print("Username should be less than 15 characters")
        # username length greater than 3
        elif len(username) < 3:
            print("Username should be greater than 3 characters")
        # username should not contain special characters
        elif any(char in username for char in punctuation):
            print("Username should not contain special characters")
        # username already exists
        elif users.get(username):
            print("Username already exists")
        # username is valid
        else:
            break

    while True:
        password = input("Enter your password: ")
        # password length less than 15
        if len(password) > 15:
            print("Password should be less than 15 characters")
        # password length greater than 3
        if len(password) < 3:
            print("Password should be greater than 3 characters")

        # password is valid
        break

    # return user
    return {"username": username, "password": password, "role": "user"}
