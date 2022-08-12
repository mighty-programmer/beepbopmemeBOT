import random
import os
import re
from instagrapi.story import StoryBuilder
from instagrapi import exceptions
from SaveFile import SaveToFile
import User
from ImageProcess import process_image
from PIL import Image


def upload_post(upload_amount, folder_name):
    """
    Uploads instagram post from random file in (folder_name),
    accepted files: .jpg|.JPG or .mp4
    """
    saver = SaveToFile("already_uploaded.txt")
    user = User.user

    print("Uploading please wait...\n")

    uploaded = 0

    with open("already_uploaded.txt") as file:
        already_uploaded = file.read().splitlines()
    with open("descriptions.txt", "r") as file:
        descriptions = file.read().splitlines()

    for filename in os.listdir(f"./{folder_name}/"):
        if re.fullmatch(r".*\.(jpg|JPG)?$", filename):
            if not (filename in already_uploaded) and (uploaded != upload_amount):
                process_image(Image.open(f"./{folder_name}/{filename}")).save(f"./{folder_name}/{filename}")
                user.photo_upload(f"./{folder_name}/{filename}",
                                  descriptions[random.randrange(0, len(descriptions))])
                uploaded = uploaded + 1
                saver.add_line(filename)
                print(f"Uploaded: {filename}")

        elif re.fullmatch(r".*\.(mp4)?$", filename):
            if not (filename in already_uploaded) and (uploaded != upload_amount):
                user.igtv_upload(title=descriptions[random.randrange(0, len(descriptions))],
                                 caption=descriptions[random.randrange(0, len(descriptions))],
                                 path=f"./{folder_name}/{filename}")
                os.remove(f"./{folder_name}/{filename}")
                os.remove(f"./{folder_name}/{filename}.jpg")
                uploaded = uploaded + 1
                saver.add_line(filename)
                print(f"Uploaded: {filename}")

    if uploaded < upload_amount:
        print(f"Not many unique images...  Uploaded {uploaded} posts. Try downloading more images.")

    print("Done uploading.\n")


def upload_story(upload_amount, folder_name):
    """
    Uploads (amount) of instagram stories from random files in (folder_name)
    accepted files: ONLY .mp4 images not implemented yet!
    """
    saver = SaveToFile("already_uploaded.txt")
    user = User.user

    print("Uploading please wait...\n")

    uploaded = 0

    with open("already_uploaded.txt") as file:
        already_uploaded = file.read().splitlines()

    for filename in os.listdir(f"./{folder_name}/"):
        # if re.fullmatch(r".*\.(jpg|JPG|png)", filename):
        #     if not (filename in already_uploaded) and (uploaded != upload_amount):
        #         self.cl.photo_upload_to_story(f"./{folder_name}/{filename}")
        #         uploaded = uploaded + 1
        #         self.saver.add_line(filename)
        #         print(f"Uploaded: {filename}")

        if re.fullmatch(r".*\.(mp4)?$", filename):
            if not (filename in already_uploaded) and (uploaded != upload_amount):

                try:
                    buildout = StoryBuilder(
                        f"./{folder_name}/{filename}"
                    )

                    user.video_upload_to_story(buildout.path)
                    uploaded = uploaded + 1
                    saver.add_line(filename)
                    saver.add_line(fr"{filename}.jpg")
                    os.remove(f"./{folder_name}/{filename}")
                    os.remove(f"./{folder_name}/{filename}.jpg")
                    print(f"Uploaded: {filename}")
                except exceptions.UnknownError:
                    print("Video length too long deleting video...")
                    os.remove(f"./{folder_name}/{filename}")
                    os.remove(f"./{folder_name}/{filename}.jpg")

    if uploaded < upload_amount:
        print(f"Not many unique images...  Uploaded {uploaded} posts. Try downloading more images.")

    print("Done uploading.\n")
