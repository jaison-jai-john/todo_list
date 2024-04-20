import os
import pickle


def read_database():
    if os.path.exists("database.dat"):
        with open("database.dat", "rb") as file:
            return pickle.load(file)
    else:
        return {"users": {}, "lists": []}


def write_database(database):
    print("saving database dont close!")
    with open("database.dat", "wb") as file:
        pickle.dump(database, file)
    print("database saved!")


# {
#     "users": {
#         "username": {"password": int, "role": str},
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
