import User
import os


def get_reels(users: list, amount: int):
    """
    Collects and returns a list of (amount) instagram reels from instagram users given as a list argument (users).
    """
    user = User.user
    user_ids = []
    medias = []
    reels_to_download = []

    for index, target in enumerate(users):
        user_ids.append(user.user_id_from_username(username=target))
        # print(f"Id of user: {user} is {user_ids[index]}")

    for userId in user_ids:
        medias.append(user.user_medias(user_id=userId, amount=amount))
        print("Done collecting")

    for media_of_user in medias:
        for media in media_of_user:
            # print(media.media_type)
            # print(media.product_type)
            if media.media_type == 2 and media.product_type == "feed":
                reels_to_download.append(media.pk)

    return reels_to_download


def download_reels(folder_name: str, reels_to_download: list):
    """
    Downloads the reels collected from get_reels function and saves them to (folder_name).
    """
    user = User.user

    for reel in reels_to_download:
        print(f"Downloading: {reel}")
        user.igtv_download(media_pk=reel, folder=f"./{folder_name}")


def start_scraping(users: list, folder_name: str, amount=20):
    """
    Scrapes from (users) (amount) of reels and downloads to (folder_name) for later use.
    """
    if not (folder_name in os.listdir()):
        os.mkdir(f"./{folder_name}")

    download_reels(folder_name=folder_name, reels_to_download=get_reels(users=users, amount=amount))
