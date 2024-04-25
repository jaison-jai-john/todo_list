from string import punctuation

from helper import clear_terminal


def login(database: dict, users: dict):
    # get user credentials
    user_name = input("Enter your username: ")

    # check if user exists
    user = users.get(user_name)

    # user does not exist
    if not user:
        # ask the user if he wants to retry
        print("User does not exist")
        ch = input("do you want to retry? (y/n): ").lower()
        # retry
        if ch == "y":
            clear_terminal()
            return login(users)
        # exit
        else:
            clear_terminal()
            return

    # user exists
    while True:
        # get password
        password = input("Enter your password: ")
        # check if password is correct
        if user["password"] == password:
            clear_terminal()
            # login
            print("Login successful")
            remember_me(database, user_name)
            return user
        # password is incorrect
        else:
            # ask the user if he wants to retry
            ch = input("Wrong password. Do you want to retry? (y/n): ").lower()
            if ch == "n":
                break


def remember_me(database: dict, username: str):
    while True:
        # ask user if he wants to be remembered
        ch = input("Do you want to remember your username? (y/n): ").lower()
        # if not then break
        if ch == "n":
            break
        # if yes then save to database
        elif ch == "y":
            database["user"] = username
            break
    clear_terminal()


def sign_up(database: dict, users: dict):
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
    clear_terminal()

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
    clear_terminal()

    # return user
    remember_me(database, username)
    return {"username": username, "password": password, "role": "user"}


def add_user(database: dict):
    # create a user
    user = sign_up(database, database["users"])
    # if user created is valid then add to database
    if user:
        database["users"][user["username"]] = user
        return user
    # else print invalid input
    else:
        print("invalid input!")
        return False


def remove_user(database: dict):
    # take username as input
    username = input("Enter username: ")
    # if user exists then delete user
    if username in database["users"]:
        del database["users"][username]


def edit_user(database: dict):
    # take username as input
    username = input("Enter username: ")
    # check if user exists
    if username in database["users"]:
        # edit user
        user = database["users"][username]
        user["password"] = input("Enter new password: ")
        user["role"] = input("Enter new role: ")
    # user does not exist
    else:
        print("invalid input!")
