import auth
import database as db
import menu


def main():
    # load database
    database = db.read_database()

    # login/signup
    while True:
        print("1. login \n2. signup \n3. exit")
        ch = input("Enter your choice: ")
        if ch == "1":
            user = auth.login(database["users"])
            break
        elif ch == "2":
            user = auth.sign_up(database["users"])
            break
        elif ch == "3":
            exit()
        else:
            print("Invalid choice")

    menu.menu(user=user, database=database)
    
    db.write_database(database)


# menu

if __name__ == "__main__":
    main()
