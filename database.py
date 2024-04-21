import os
import pickle


def read_database():
    # check if the file exists
    if os.path.exists("database.dat"):
        # read file
        print("loading database dont close!")
        with open("database.dat", "rb") as file:
            return pickle.load(file)
    # if file does not exist return empty database
    else:
        return {
            "users": {
                "admin": {"username": "admin", "password": "admin1234", "role": "admin"}
            },
            "lists": [],
        }


def write_database(database):
    # write to file
    print("saving database dont close!")
    with open("database.dat", "wb") as file:
        pickle.dump(database, file)
    print("database saved!")


# database structure
# {
#     "users": {
#         "username": {"password": str, "role": str},
#     },
#     "lists": [
#         {
#             "owner": str,
#             "access": [str],
#             "title": str,
#             "tasks": [{"task": str, "due": str, "completed": bool}],
#         }
#     ],
# }
