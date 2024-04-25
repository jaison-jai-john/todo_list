import os


def print_sep(sep=""):
    print(
        f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n{sep}"
    )


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def assert_type(
    value,
    type_=str,
    message="Enter value: ",
    error_message="invalid input",
    take_value=False,
    key=lambda x: x,
):
    while True:
        try:
            if take_value and not value:
                value = type_(input(message))
            else:
                value = type_(value)
            if not key(value):
                raise ValueError
            else:
                clear_terminal()
                break
        except ValueError:
            value = None
            print(error_message)
            choice = input("Do you want to try again? (y/n): ").lower()
            if choice == "n":
                clear_terminal()
                return False
            elif choice == "y":
                pass
    return value
