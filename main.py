import auth
import database as db
import menu
from captcha import captcha_auth
from helper import clear_terminal

# notifications
# error handling


def main():
    # load database
    database = db.read_database()
    clear_terminal()
    # login/signup
    # check if the user is remembered
    if not database.get("user"):
        while True:
            # print out options
            print("1. login \n2. signup \n3. exit")
            # get user choice
            ch = input("Enter your choice: ")
            clear_terminal()
            if ch == "1" or ch == "2":
                # human verification incase of auth
                if captcha_auth():
                    # login
                    if ch == "1":
                        # get user for the session
                        user = auth.login(database, database["users"])
                        # user does not exist so close program
                        if not user:
                            exit("shutting down!")
                        break
                    # signup
                    elif ch == "2":
                        # get user for the session
                        user = auth.add_user(database)
                        # user does not exist so close program
                        if not user:
                            exit("shutting down!")
            # exit
            elif ch == "3":
                exit("shutting down")
            # invalid input
            else:
                print("Invalid choice")
    # user is rememebered so return user
    else:
        user = database["users"][database["user"]]

    # go to respective menu
    menu.menu(user=user, database=database)
    clear_terminal()
    # save database
    db.write_database(database)


# menu

if __name__ == "__main__":
    main()
