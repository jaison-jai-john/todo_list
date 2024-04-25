import auth
import database as db
from helper import clear_terminal
from todo_list import add_list, display_lists, fetch_list, list_view, remove_list


def menu(user, database):
    if user["role"] == "user":
        user_menu(user, database)
    elif user["role"] == "admin":
        admin(user, database)


# admin should be able to:
# add,edit and remove users.
# add,edit and remove lists of other users
# add,edit and remove tasks of other users
# give/remove access of lists to specific users
def admin(user, database):
    # welcome message
    print("ADMIN PANEL")
    print(f'welcome {user["username"]}')

    # fetch all the lists in system
    lists = fetch_list(database, user)

    while True:
        # print options
        print(
            "1. display lists \n2. add list \n3. select list \n4. remove list \n5. add user \n6. remove user \n7. edit user \n8. view users \n9. exit \n10. logout and exit"
        )

        # get user choice
        ch = input("Enter choice: ")

        # display lists
        if ch == "1":
            if len(lists) == 0:
                print("Empty!")
            else:
                display_lists(lists)
        # add list
        elif ch == "2":
            lists.append(add_list(database, user))
        # select list
        elif ch == "3":
            if display_lists(lists):
                ch = int(input("Enter choice: ")) - 1
                list_view(lists[ch], user)
        # remove list
        elif ch == "4":
            if display_lists(lists):
                ch = int(input("Enter choice: ")) - 1
                remove_list(database, lists[ch])
        # add user
        elif ch == "5":
            auth.add_user(database)
        # remove user
        elif ch == "6":
            auth.remove_user(database)
        # edit user
        elif ch == "7":
            auth.edit_user(database)
        # view users
        elif ch == "8":
            for i, user in enumerate(database["users"]):
                print(f"{i+1}. {user}")
        # exit
        elif ch == "9":
            break
        # logout and exit
        elif ch == "10":
            database["user"] = None
            break
        # invalid input
        else:
            print("invalid input!")


# user should be able to:
# add,edit and remove lists
# add,edit and remove tasks
# give/remove access of lists to others if the person is the owner
def user_menu(user, database):
    # welcome message
    print(f'Welcome {user["username"]}!')

    # fetch lists which the user owns or has access to
    lists = fetch_list(database, user)
    while True:
        # print options
        print(
            "1. display lists \n2. add list \n3. select list \n4. remove list \n5. exit \n6. logout and exit"
        )

        # get user choice
        ch = input("Enter choice: ")
        clear_terminal()

        # display lists
        if ch == "1":
            display_lists(lists)
        # add list
        elif ch == "2":
            lists.append(add_list(database, user))
        # edit list view
        elif ch == "3":
            if display_lists(lists):
                ch = int(input("enter chocie: ")) - 1
                clear_terminal()
                list_view(lists[ch], user)
        # remove list
        elif ch == "4":
            if display_lists(lists):
                ch = int(input("enter choice: ")) - 1
                remove_list(database, lists[ch])

        # exit
        elif ch == "5":
            break
        # logout and exit
        elif ch == "6":
            database["user"] = None
            break
        # invalid input
        else:
            print("invalid input!")
