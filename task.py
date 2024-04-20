def display_tasks(tasks: list):
    # iterate through tasks
    for i, task in enumerate(tasks):
        # print each task
        print(i + 1, task)


def edit_task(task: dict):
    print("what do you want to edit?: ")
    fields = [key for key in task.keys()]
    for i, field in enumerate(fields[:-1]):
        print(i + 1, field)

    ch = int(input("Enter choice: ")) - 1

    # edit todo
    if ch == 0:
        task["task"] = input("Enter task: ")
    elif ch == 1:
        task["due"] = input("Enter due date in YYYY-MM-DD format: ")
    else:
        print("invalid input!")


def remove_task(task_list: list):
    print("what task do you want to remove?: ")
    display_tasks(task_list)
    ch = int(input("Enter choice: ")) - 1

    if ch < 0 or ch >= len(task_list):
        print("invalid input!")

    del task_list[ch]
    print("task deleted!")


def add_task(task_list: list):
    task = input("enter task: ")
    due = input("enter due date in YYYY-MM-DD format: ")
    completed = False
    task_list.append({"task": task, "due": due, "completed": completed})
