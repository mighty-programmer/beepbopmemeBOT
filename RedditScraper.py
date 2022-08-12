import os
import praw
import requests
import re
from progress.bar import Bar
from redvid import Downloader


class RScraper:
    # Starting Reddit API
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id="woXAnsOr5ybVDaXc07pRRA",
            client_secret="Gt22tiwMruT6KsTm3nE6mX7FN5JZWA",
            user_agent="USer-Agent : MyApi/0.1"
        )

    def scrap(self, top_of: str, is_video: bool, posts_to_scan: int, subreddit: str):
        """
        This method returns a list of links, each line is a link to an image, gif or video found on the specified subreddit
        filtered by HOT.
        """

        links_to_download = []
        count = 0

        if not top_of:
            list_of_posts = self.reddit.subreddit(subreddit).hot(limit=10000)
        else:
            list_of_posts = self.reddit.subreddit(subreddit).top(top_of)

        with Bar('Locating links: ') as bar:
            for submission in list_of_posts:
                if count < posts_to_scan:
                    if re.fullmatch(r".*\.(jpg|JPG)?$", submission.url) and (not is_video):
                        try:
                            links_to_download.append((submission.url, submission.title))
                            bar.next(100 / posts_to_scan)
                            count = count + 1
                        except:
                            pass

                    elif re.match(r"https:\/\/v\.redd\.it", submission.url) and is_video:
                        try:
                            links_to_download.append((submission.url, submission.title))
                            bar.next(100 / posts_to_scan)
                            count = count + 1
                        except:
                            pass

                    else:
                        bar.next(100 / posts_to_scan)
                        continue

                else:
                    break

            return links_to_download

    def download_from_list(self, links_to_download, folder_name):
        """
        This method downloads images (.jpg|.JPG|.png) and videos/gis (.mp4|.mp4) from a linkList.
        """

        if not (folder_name in os.listdir()):
            os.mkdir(f"./{folder_name}")

        saved_counter = 0
        progress_end = len(links_to_download)

        with Bar("Downloading: ") as bar:
            for submission in links_to_download:

                r = requests.get(submission[0])

                if re.fullmatch(r".*\.(jpg|JPG|png)?$", submission[0]):

                    title = submission[0][19:]
                    file_path = fr"./{folder_name}/" + title
                    saved_counter = saved_counter + 1

                    with open(file_path, "wb") as f:
                        f.write(r.content)

                    bar.next(100 / progress_end)
                    continue

                else:
                    file_path = fr"./{folder_name}/"
                    downloader = Downloader(max_q=True)
                    downloader.log = False
                    downloader.overwrite = True
                    downloader.url = submission[0]
                    downloader.path = file_path
                    downloader.download()
                    bar.next(100 / progress_end)
                    continue

    def start(self, folder_name, subreddit: str, is_video=False, posts_to_scan=100, top_of=None):
        """
        This method scrapes the specified subreddit for the maximum amount of images. Creates linkList
        and passes it to the download from linked list function.
        """

        self.download_from_list(
            links_to_download=self.scrap(top_of=top_of, is_video=is_video, posts_to_scan=posts_to_scan, subreddit=subreddit),
            folder_name=folder_name)
