from string import punctuation

from helper import assert_type, clear_terminal, print_sep


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


def sign_up(database: dict, users: dict, remember=True):
    while True:
        username = assert_type(
            input("Enter username: "),
            str,
            "Enter username: ",
            "username's size should be from 3 to 15. should not contain special characters and should be unique!",
            True,
            key=lambda x: (
                True
                if len(x) >= 3
                and len(x) <= 15
                and not any(char in punctuation for char in x)
                and not users.get(x)
                else False
            ),
        )
        if username:
            break
        else:
            return False
    clear_terminal()

    while True:
        password = assert_type(
            input("Enter new password: "),
            str,
            "Enter new password: ",
            "password size should be between 3 and 15",
            True,
            lambda x: True if len(x) >= 3 and len(x) <= 15 else False,
        )
        if password:
            break
        else:
            return False
    clear_terminal()

    # return user
    if remember:
        remember_me(database, username)
    return {"username": username, "password": password, "role": "user"}


def add_user(database: dict, remember=True):
    # create a user
    user = sign_up(database, database["users"], remember)
    # if user created is valid then add to database
    if user:
        database["users"][user["username"]] = user
        return user
    # else print invalid input
    else:
        print("invalid input!")
        return user


def remove_user(database: dict):
    print_sep("Users")
    print_sep()
    for i, user in enumerate(database["users"]):
        print(f"{i+1}. {user}")
    print_sep()
    # take username as input
    username = input("Enter username: ")
    # if user exists then delete user
    if username in database["users"]:
        del database["users"][username]
    clear_terminal()


def edit_user(database: dict):
    print_sep("Users")
    print_sep()
    for i, user in enumerate(database["users"]):
        print(f"{i+1}. {user}")
    print_sep()
    # take username as input
    username = input("Enter username: ")
    # check if user exists
    if username in database["users"]:
        # edit user
        user = database["users"][username]

        change = input("Do you want to change the username? (y/n): ").lower()
        if change == "y":
            new_username = assert_type(
                input("Enter username: "),
                str,
                "Enter username: ",
                "username's size should be from 3 to 15. should not contain special characters and should be unique!",
                True,
                key=lambda x: (
                    True
                    if len(x) >= 3
                    and len(x) <= 15
                    and not any(char in punctuation for char in x)
                    and not database["users"].get(x)
                    else False
                ),
            )
            if new_username:
                database["users"][new_username] = user
                del database["users"][username]

                username = new_username
                user = database["users"][username]

        change = input("Do you want to change the password? (y/n): ").lower()
        if change == "y":
            password = assert_type(
                input("Enter new password: "),
                str,
                "Enter new password: ",
                "password size should be between 3 and 15",
                True,
                lambda x: True if len(x) >= 3 and len(x) <= 15 else False,
            )
            if password:
                user["password"] = password

        change = input("Do you want to change the role? (y/n): ").lower()
        if change == "y":
            role = assert_type(
                input("Enter new role: "),
                message="Enter new role: ",
                error_message="role has to be user or admin",
                take_value=True,
                key=lambda x: True if x in ["admin", "user"] else False,
            )

            if role:
                user["role"] = role
        clear_terminal()
    # user does not exist
    else:
        clear_terminal()
        print("invalid input!")
