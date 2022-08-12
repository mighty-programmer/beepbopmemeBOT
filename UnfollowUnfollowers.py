import time
import random
import User
from SaveFile import SaveToFile
from progress.bar import Bar


class Unfollower:
    def __init__(self):
        self.cl = User.user

    def find_unfollowers(self):
        """
        Finds and returns non following users by comparing users followers and following.
        """

        followers = self.cl.user_followers(self.cl.user_id)
        following = self.cl.user_following(self.cl.user_id)

        unfollowers = list(set(following) - set(followers))

        print("You have: " + str(len(unfollowers)) + " unfollowers!\n")

        print("Unfollowers are:")
        print("****************************")

        for user_id in unfollowers:
            print(following[str(user_id)].username)

        print("****************************\n")

        return unfollowers

    def unfollow(self, unfollowers, params, logger_name="unfollow_history.txt"):
        """
        Unfollows non-followers from given List (unfollowers), takes parameters using a Dictionary (params). Has the
        ability to ignor verified non-followers and those with the specified following and above.
        Bot anti-detection wait between unfollows,
        based on parameter rate, (3600 / int(rate)) +- 5) wait period.

        """
        logger = SaveToFile(logger_name)
        rate, ignor_verified, minimum_followers_to_ignor = params.values()

        with Bar(f'Unfollowing user every {int(3600/rate)} seconds:') as bar:
            end_of_progress = len(unfollowers)

            for user_id in unfollowers:
                # Random wait limits determined by user inputed action rate per hour

                max_time = int(((3600 / int(rate)) + 5))
                min_time = int(((3600 / int(rate)) - 5))

                time_to_wait = int(random.randrange(min_time, max_time))

                info = self.cl.user_info(user_id)
                followers = info.follower_count
                username = info.username
                is_verified = info.is_verified

                if followers >= int(minimum_followers_to_ignor) or (ignor_verified and is_verified):
                    message = str(f"User famous i do not unfollow: {username}. Has {followers} followers.")
                    logger.add_line(message)
                else:
                    time.sleep(time_to_wait)
                    self.cl.user_unfollow(user_id)
                    message = str(f"Unfollowed: {username}. Has {followers} followers.")
                    logger.add_line(message)

                bar.next(100 / end_of_progress)

        logger.close_file()
        print("\nDone!\n")

    def start(self, params):
        """
        Calls find_unfollowers and unfollow functions to start the Unfollow-Unfollowers routine.
        """
        self.unfollow(unfollowers=self.find_unfollowers(), params=params)

