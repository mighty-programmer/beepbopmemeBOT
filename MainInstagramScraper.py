from InstagramScraper import start_scraping
import User

if __name__ == "__main__":
    User.login(None, None)
    start_scraping(folder_name="instaReels", users=["dailydoseofinternet"])


def run():
    start_scraping(folder_name="instaReels", users=["dailydoseofinternet"])
