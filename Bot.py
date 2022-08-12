import schedule
import time
import MainRedditScraper
import MainInstagramScraper
import MainUploadPost
import MainUploadIgtv
import MainUploadStory
import Menu
import sys
import User
import Growth

if __name__ == "__main__":
    """
    Argument -m prints out a menu for manual actions, 
    argument -a starts an automated Bot with preconfigured repeating actions.
    """
    user = None

    if not (len(sys.argv) > 2 or len(sys.argv) == 1):

        if sys.argv[1] == "-m":
            user = User.login(input("Username: "), input("Password: "))
            Menu.print_menu()
            sys.exit()

        elif sys.argv[1] == "-a":
            # User.login call with no arguments get credentials from user.txt file
            user = User.login()

            schedule.every(6).hours.do(MainRedditScraper.run)
            schedule.every(6).hours.do(MainInstagramScrapper.run)
            schedule.every(6).hours.do(MainUploadPost.run)
            schedule.every(4).hours.do(MainUploadIgtv.run)
            schedule.every().hour.do(MainUploadStory.run)
            schedule.every(10).days.do(Growth.create_bucket)
            schedule.every(2).hours.do(Growth.follow_bucket)

            print(
                '''
                Post uploading every 6H.
                Story uploading every 1H.
                IgTv uploading every 4H.
                ---     Scrapping     ---
                RedditScrapper every 6H.
                InstagramScrapper every 6H.
                ---       Growth      ---
                Growth Bucket every 10 days.
                Following 5 people every 2 hours.
                '''
            )

            while True:
                schedule.run_pending()
                time.sleep(1)

        else:
            print("Wrong argument option.")
            sys.exit()

    else:
        print("Wrong argument option.")
        sys.exit()
