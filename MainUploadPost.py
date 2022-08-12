from Uploader import upload_post
import User

if __name__ == "__main__":
    User.login()
    upload_post(upload_amount=1, folder_name="memes")


def run():
    upload_post(upload_amount=1, folder_name="memes")
