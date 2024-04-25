import datetime

from helper import clear_terminal, print_sep


def display_tasks(tasks: list, sort=True):
    clear_terminal()
    if len(tasks) == 0:
        print("Empty!")
        return False, tasks
    print_sep("Tasks")
    print_sep()
    # iterate through tasks
    if sort:
        tasks.sort(
            key=lambda x: (
                x["completed"] == False
                and datetime.datetime.today()
                < datetime.datetime.strptime(x["due"], "%Y-%m-%d"),
                not x["completed"],
                x["due"],
            ),
        )
    for i, task in enumerate(tasks):
        # print each task
        if task["completed"]:
            completion_status = "completed"
        elif (
            datetime.datetime.strptime(task["due"], "%Y-%m-%d")
            < datetime.datetime.today()
        ):
            completion_status = "overdue"
        else:
            completion_status = "not completed"
        print(f'{i + 1}. {task["task"]} | {task["due"]} | {completion_status}')
    return True, tasks


def edit_task(task: dict):
    # print the fields of the task
    print("what do you want to edit?: ")
    fields = [key for key in task.keys()]
    for i, field in enumerate(fields[:-1]):
        print(f"{i + 1}.", field)

    # take input
    ch = int(input("Enter choice: ")) - 1

    # edit todo
    if ch == 0:
        task["task"] = input("Enter task: ")
    # edit due date
    elif ch == 1:
        task["due"] = input("Enter due date in YYYY-MM-DD format: ")
    else:
        print("invalid input!")


def remove_task(task_list: list):
    # display tasks
    not_empty, task_list = display_tasks(task_list)
    if not_empty:
        print("what task do you want to remove?: ")

        # take input
        ch = int(input("Enter choice: ")) - 1

        # check if input is valid
        if ch < 0 or ch >= len(task_list):
            print("invalid input!")
            return

        # remove task
        del task_list[ch]
        print("task deleted!")


def add_task(task_list: list):
    # take input
    task = input("enter task: ")
    due = input("enter due date in YYYY-MM-DD format: ")
    completed = False
    # add task to list
    task_list.append({"task": task, "due": due, "completed": completed})


def search_task(task_list: list):
    # take input
    search = input("enter due date to search: ")
    # search task
    for task in task_list:
        if task["due"] == search:
            print(task)
