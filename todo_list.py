from task import add_task, display_tasks, edit_task, remove_task


def fetch_list(database, user):
    # create lists container
    lists = []

    # iterate through lists
    for task_list in database["lists"]:
        # check if the user has access to the list
        if (
            user["username"] == task_list["owner"]
            or user["username"] in task_list["access"]
        ):
            # if user has access to the list then add it to the list of lists
            lists.append(task_list)

    return lists


def add_list(database, user):
    # take title input
    title = input("Enter title: ")

    # create list
    task_list = {
        "owner": user["username"],
        "access": [user["username"]],
        "title": title,
        "tasks": [],
    }

    # add list to database
    database["lists"].append(task_list)

    print("list created!")
    # return the list
    return task_list


def remove_list(database, list_to_remove):
    # iterate through lists
    for pos, task_list in enumerate(database["lists"]):
        # if task list is the list to remove
        if task_list == list_to_remove:
            # remove the list from the database
            del database["lists"][pos]
            print("list removed")


def edit_list(user, list_to_edit: dict):
    options = ["edit title", "edit task", "remove task", "add task"]
    if list_to_edit["owner"] == user["username"]:
        options = options + ["add access", "remove access"]

    print("what would you like to do?: ")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    ch = input("Enter choice: ")
    if ch == "1":
        list_to_edit["title"] = input("Enter title: ")
    elif ch == "2":
        display_tasks(list_to_edit["tasks"])
        ch = int(input("Enter choice: ")) - 1

        edit_task(list_to_edit["tasks"][ch])
    elif ch == "3":
        remove_task(list_to_edit["tasks"])
    elif ch == "4":
        add_task(list_to_edit["tasks"])
    elif user["username"] == list_to_edit["owner"] and ch == "5":
        username = input("enter the username of the user you want to give access to: ")
        list_to_edit["access"].append(username)
    elif user["username"] == list_to_edit["owner"] and ch == "6":
        for i, username in enumerate(list_to_edit["access"]):
            print(i + 1, username)
        ch = int(input("please enter choice: "))
        del list_to_edit["access"][ch - 1]
    else:
        print("invalid input!")


def list_view(list_to_view: dict, user):
    while True:
        print("1. view tasks \n2. edit list \n3.exit")
        ch = input()
        if ch == "1":
            display_tasks(list_to_view["tasks"])
        elif ch == "2":
            edit_list(user, list_to_view)
        elif ch == "3":
            break
        else:
            print("invalid input")
