import datetime

from win10toast import ToastNotifier

toaster = ToastNotifier()


def show_reminders(tasks: list):
    for task in tasks:
        if task["due"] == datetime.datetime.now().strftime("%Y-%m-%d"):
            print(task["task"])
            toaster.show_toast("Reminder", task["task"], duration=5, threaded=True)
