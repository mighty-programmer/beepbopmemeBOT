import os


def read_credentials():
    if "user.txt" in os.listdir():
        with open("user.txt", "r") as user_file:
            user = user_file.readlines()

        username = user[0][10:].replace(r"\n", "").strip()
        password = user[1][10:].replace(r"\n", "").strip()

        print(username)
        print(password)


if __name__ == "__main__":
    read_credentials()
