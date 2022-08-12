import os
import random

import User
import pickle
from progress.bar import Bar


def create_bucket():
    """
    Creates and saves a file containing a list of instagram Users for the Bot to follow.
    It finds users from the pages Followers. Slow but works for now.
    """
    user = User.user
    my_followers = user.user_followers(user.user_id)
    to_follow_bucket = []

    # TODO Do not add yourself on the to follow list.

    with Bar('Checking my Followers: ') as bar:
        for follower in my_followers:
            print("\n")
            to_follow_bucket.append(user.user_followers(follower))
            bar.next(100 / len(my_followers))

    random.shuffle(to_follow_bucket)

    with open('to_follow_bucket.pickle', 'wb') as filename:
        pickle.dump(to_follow_bucket, filename, protocol=pickle.HIGHEST_PROTOCOL)


def follow_bucket(amount_to_follow=5):
    """
    Opens the file created by created_bucket, and follows (amount_to_follow)
    accounts that are not already following the page in order to force growth.
    """
    user = User.user
    my_followers = user.user_followers(user.user_id)

    accounts_followed = 0

    if "to_follow_bucket.pickle" in os.listdir():
        with open('to_follow_bucket.pickle', 'rb') as filename:
            to_follow_bucket = pickle.load(filename)

        print(to_follow_bucket)

        for follower in to_follow_bucket:
            for account in follower:
                if accounts_followed < amount_to_follow and not (account in my_followers):
                    print(f"Followed {user.username_from_user_id(account)}")
                    accounts_followed = accounts_followed + 1
                    user.user_follow(user_id=account)

        if accounts_followed == amount_to_follow:
            print("Done")
        else:
            print("Not many people to follow from list.")
    else:
        print("No bucket file found.")


if __name__ == "__main__":
    User.login()
    create_bucket()
    follow_bucket()


# def get_users_with_criteria(followers: list):
#     users_with_criteria = []
#
#     for follower in followers:
#         followers_count = len(user.user_followers(follower))
#         # print(f"Folllower count => {followers_count}")
#         following_count = len(user.user_following(follower))
#         # print(f"Following count => {following_count}")
#
#         if followers_count != 0:
#             follow_ratio = following_count / followers_count
#         elif following_count != 0:
#             follow_ratio = float("inf")
#         else:
#             follow_ratio = 0
#
#         if follow_ratio > 0.7:
#             if not (follower in my_followers):
#                 # print(f"Adding {user.username_from_user_id(follower)}")
#                 users_with_criteria.append(follower)
#         else:
#             continue
#
#     return users_with_criteria

