from helper import assert_type, clear_terminal, print_sep
from task import add_task, display_tasks, edit_task, remove_task, search_task


def display_lists(lists: list):
    clear_terminal()
    # if no lists exist
    if len(lists) == 0:
        print("Empty!")
        return False
    print_sep("Lists")
    print_sep("")
    # print lists
    for i, task_list in enumerate(lists):
        print(f'{i + 1}. {task_list["title"]}')
    print_sep("")
    return True


def fetch_list(database, user):
    if user["role"] == "admin":
        return database["lists"]
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
    clear_terminal()
    # take title input
    title = input("Enter title: ")

    # create list
    task_list = {
        "owner": user["username"],
        "access": [user["username"]],
        "title": title,
        "tasks": [],
    }

    print("list created!")
    clear_terminal()
    # return the list
    return task_list


def remove_list(database, list_to_remove):
    # iterate through lists
    for pos, task_list in enumerate(database["lists"]):
        # if task list is the list to remove
        if task_list == list_to_remove:
            # remove the list from the database
            del database["lists"][pos]
            clear_terminal()
            print("list removed")


def edit_list(user, list_to_edit: dict):
    # dynamically print the options based on the user
    options = [
        "edit title",
        "edit task",
        "remove task",
        "add task",
        "complete a task",
        "search task",
    ]
    if list_to_edit["owner"] == user["username"] or user["role"] == "admin":
        options = options + ["add access", "remove access"]
    options.append("exit")

    # print the options
    print("what would you like to do?: ")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    # get user choice
    ch = input("Enter choice: ")
    clear_terminal()
    # edit title
    if ch == "1":
        list_to_edit["title"] = input("Enter title: ")
    # edit task
    elif ch == "2":
        # display tasks
        not_empty, list_to_edit["tasks"] = display_tasks(list_to_edit["tasks"])
        if not_empty:
            ch = assert_type(
                input("Enter Choice: "),
                int,
                "Enter Choice: ",
                "Please enter an integer!",
                True,
                key=lambda x: (
                    True if x <= len(list_to_edit["tasks"]) and x > 0 else False
                ),
            )
            if ch:
                ch -= 1
                # edit task
                edit_task(list_to_edit["tasks"][ch])
    # remove task
    elif ch == "3":
        remove_task(list_to_edit["tasks"])
    # add task
    elif ch == "4":
        add_task(list_to_edit["tasks"])
    # complete a task
    elif ch == "5":
        not_empty, list_to_edit["tasks"] = display_tasks(list_to_edit["tasks"])
        if not_empty:
            ch = assert_type(
                input("Enter Choice: "),
                int,
                "Enter Choice: ",
                "Please enter an integer!",
                True,
                key=lambda x: (
                    True if x <= len(list_to_edit["tasks"]) and x > 0 else False
                ),
            )
            if ch:
                ch -= 1
                list_to_edit["tasks"][ch]["completed"] = True
    # search task
    elif ch == "6":
        search_task(list_to_edit["tasks"])
    # exit the menu
    elif (ch == "7" and user["role"] == "user") or (
        ch == "9"
        and (user["role"] == "admin" or user["username"] == list_to_edit["owner"])
    ):
        clear_terminal()
    # add access
    elif (
        user["username"] == list_to_edit["owner"] or user["role"] == "admin"
    ) and ch == "7":
        username = input("enter the username of the user you want to give access to: ")
        list_to_edit["access"].append(username)
    # remove access
    elif (
        user["username"] == list_to_edit["owner" or user["role"] == "admin"]
    ) and ch == "8":
        for i, username in enumerate(list_to_edit["access"]):
            print(f"{i + 1}. {username}")
        ch = assert_type(
            input("Enter Choice: "),
            int,
            "Enter Choice: ",
            "Please enter an integer!",
            True,
            key=lambda x: (
                True if x <= len(list_to_edit["access"]) and x > 0 else False
            ),
        )
        if ch:
            ch -= 1
            del list_to_edit["access"][ch - 1]
    else:
        print("invalid input!")


def list_view(list_to_view: dict, user):
    while True:
        print_sep(list_to_view["title"])
        print_sep()
        # print options
        print("1. view tasks \n2. complete a task \n3. edit list \n4. exit")
        # get user choice
        ch = input("Enter choice: ")
        clear_terminal()
        # view tasks
        if ch == "1":
            display_tasks(list_to_view["tasks"])
        elif ch == "2":
            not_empty, list_to_view["tasks"] = display_tasks(list_to_view["tasks"])
            if not_empty:
                ch = assert_type(
                    input("Enter Choice: "),
                    int,
                    "Enter Choice: ",
                    "Please enter an integer!",
                    True,
                    key=lambda x: (
                        True if x <= len(list_to_view["tasks"]) and x > 0 else False
                    ),
                )
                if ch:
                    ch -= 1
                    clear_terminal()
                    list_to_view["tasks"][ch]["completed"] = True
        # edit list
        elif ch == "3":
            edit_list(user, list_to_view)
        # exit
        elif ch == "4":
            clear_terminal()
            break
        else:
            print("invalid input this one?")
