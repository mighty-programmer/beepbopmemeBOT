from instagrapi import Client
import os


user = Client()


def login(username=None, password=None):
    """
    An all-in-one method to log-in instagram user. If user has already been loged-in once
    it loads the previous sessions cookies. Holds this session's user as a global variable
    for all classes to access (user).
    """
    if username is None and password is None:
        username, password = read_credentials()

    print(f"Username: {username}")
    print(f"Password: {password}")

    if f"{username}_settings.json" in os.listdir("./"):
        print("Loaded settings")
        user.load_settings(f"./{username}_settings.json")
        user.login(username=username, password=password)
        print("Logged")
    else:
        print("First time login")
        user.login(username=username, password=password)
        user.dump_settings(f"./{username}_settings.json")
        print("Logged")


def read_credentials():
    if "user.txt" in os.listdir():
        with open("user.txt", "r") as user_file:
            credentials = user_file.readlines()

        username = credentials[0][10:].replace(r"\n", "").strip()
        password = credentials[1][10:].replace(r"\n", "").strip()

        return username, password
