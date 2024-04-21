import auth
import database as db
import menu
from helper import clear_terminal

# notifications
# sort
# done
# error handling


def main():
    # load database
    database = db.read_database()
    clear_terminal()
    # login/signup
    if not database.get("user"):
        while True:
            # print out options
            print("1. login \n2. signup \n3. exit")
            # get user choice
            ch = input("Enter your choice: ")
            clear_terminal()
            # login
            if ch == "1":
                # get user for the session
                user = auth.login(database, database["users"])
                if not user:
                    exit("shutting down!")
                break
            # signup
            elif ch == "2":
                # get user for the session
                user = auth.sign_up(database, database["users"])
                # incase user is not returned due to invalid input exit program
                if not user:
                    exit("shutting down!")
                # add user to database
                database["users"][user["username"]] = user
                break
            # exit
            elif ch == "3":
                exit("shutting down")
            else:
                print("Invalid choice")
    else:
        user = database["users"][database["user"]]

    # go to respective menu
    menu.menu(user=user, database=database)
    # save database
    clear_terminal()
    db.write_database(database)


# menu

if __name__ == "__main__":
    main()
