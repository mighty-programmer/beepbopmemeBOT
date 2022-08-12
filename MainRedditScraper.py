from RedditScraper import RScraper

if __name__ == "__main__":
    scraper = RScraper()
    scraper.start(folder_name="memes", subreddit="memes", is_video=False, posts_to_scan=25, top_of="day")
    scraper.start(folder_name="funnyVideos", subreddit="funnyvideos", is_video=True, posts_to_scan=25, top_of="day")


def run():
    scraper = RScraper()
    scraper.start(folder_name="memes", subreddit="memes", is_video=False, posts_to_scan=25, top_of="day")
    scraper.start(folder_name="funnyVideos", subreddit="funnyvideos", is_video=True, posts_to_scan=25, top_of="day")
