from RedditScraper import RScraper
from Uploader import upload_post, upload_story
from UnfollowUnfollowers import Unfollower
from InstagramScraper import start_scraping as reelScrape


def print_menu():
    scraper = RScraper()
    unfollower = Unfollower()

    user_choice = 0

    while not (user_choice == 6):
        print("Select action\n")
        print("1 -- Reddit Scrapper")
        print("2 -- Instagram reel scrapper")
        print("3 -- Instagram post from folder")
        print("4 -- Instagram story from folder")
        print("5 -- Unfollow Unfollowers")
        print("6 -- EXIT")

        user_choice = int(input("Select Action (ex. 1): "))

        if user_choice == 1:
            is_video = input("Scan for images or videos (IMG/VID): ")
            if is_video == "IMG":
                is_video = False
            elif is_video == "VID":
                is_video = True
            else:
                print("Wrong input defaulting to images")
                is_video = False

            subreddit = input("Name of subreddit: ")
            top_or_hot = input("Scrap from hot or form top posts (HOT/TOP): ")
            posts_to_scan = int(input("Amount of posts to scan: "))
            folder_name = input("Folder name to save downloads: ")

            if top_or_hot == "HOT":
                scraper.start(folder_name=folder_name, is_video=is_video, posts_to_scan=posts_to_scan,
                               subreddit=subreddit)
            elif top_or_hot == "TOP":
                time_filter = input("Select time filter (all, day, hour, month, week, yeer): ")
                scraper.start(folder_name=folder_name, is_video=is_video, posts_to_scan=posts_to_scan,
                               subreddit=subreddit, top_of=time_filter)
            else:
                print(f"Wrong input =>{top_or_hot} try again.")

        if user_choice == 2:
            pages = []
            pages_amount = int(input("Amount of pages to scrape: "))

            for idx in range(pages_amount):
                pages.append(str(input(f"Page number {idx+1} name:")))

            folder_name = input("Folder name to save reels: ")
            reelScrape(folder_name=folder_name, users=pages)

        if user_choice == 3:
            upload_amount = int(input("How many posts to make: "))
            folder_name = input("Post media source folder: ")
            upload_post(upload_amount=upload_amount, folder_name=folder_name)

        if user_choice == 4:
            upload_amount = int(input("How many stories to make: "))
            folder_name = input("Media source folder: ")
            upload_story(upload_amount=upload_amount, folder_name=folder_name)

        if user_choice == 5:

            rate = int(input("Give unfollow rate (req. = 50): "))
            ignor_verified = input("Do you want to keep verified unfollowers (YES/n): ")
            minimum_followers_to_ignor = input("How much followers should someone have to not unfollow (ex. 10000): ")

            if ignor_verified == "YES":
                ignor_verified = True
            elif ignor_verified == "n":
                ignor_verified = False
            else:
                print("Wrong input! (Defaulting to YES)")
                ignor_verified = True

            parameters = {
                "rate": rate,
                "ignor_verified": ignor_verified,
                "minimum_followers_to_ignor": minimum_followers_to_ignor,
            }

            unfollower.start(params=parameters)

