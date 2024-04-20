from todo_list import add_list, fetch_list, list_view


def menu(user, database):
    if user["role"] == "user":
        user_menu(user, database)
    ...


# admin should be able to:
# add,edit and remove users.
# add,edit and remove lists of other users
# add,edit and remove tasks of other users
# give/remove access of lists to specific users
def admin(): ...


# user should be able to:
# add,edit and remove lists
# add,edit and remove tasks
# give/remove access of lists to others if the person is the owner
def user_menu(user, database):
    print(f'Welcome {user["username"]}!')
    lists = fetch_list(database, user)
    while True:
        print("1. display lists \n2. add list \n3. select list")

        ch = input("Enter choice: ")
        if ch == "1":
            if len(lists) == 0:
                print("Empty!")
            else:
                for i, task_list in enumerate(lists):
                    print(i + 1, task_list["title"])
        elif ch == "2":
            lists.append(add_list(database, user))
        elif ch == "3":
            for i, task_list in enumerate(lists):
                print(i + 1, task_list["title"])
            ch = int(input("enter chocie: ")) - 1
            list_view(lists[ch], user)

    ...
