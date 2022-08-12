from Uploader import upload_story
import User

if __name__ == "__main__":
    User.login()
    upload_story(upload_amount=1, folder_name="funnyVideos")


def run():
    upload_story(upload_amount=1, folder_name="funnyVideos")
