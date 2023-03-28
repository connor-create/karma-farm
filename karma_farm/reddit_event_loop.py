import praw

import reddit_config
from ai import response

import time
import random


reddit = praw.Reddit(
    client_id=reddit_config.CLIENT_ID,
    client_secret=reddit_config.SECRET,
    password=reddit_config.PASSWORD,
    user_agent="I am not an AI",
    username=reddit_config.USERNAME,
)

askreddit_post_ids_replied_to = set()

def comment_chain_runner():
    while True:
        try:
            subreddit = reddit.subreddit("askreddit")
            submissions = list(subreddit.hot(limit=10))
            submission = submissions[random.randint(0, len(submissions))]
            comments = list(submission.comments)
            comment = comments[random.randint(0, len(comments))]
            print(f"Title: {submission.title}")
            print(f"Comment: {comment.body}")
            my_comment = response.reply_to_comment_chain(submission.title, [comment.body], override_modifier=" as a very nice person who usually agrees with reasonable people")
            print(f"Reply: {my_comment}")
            comment.reply(my_comment)
            time.sleep(int(15.1 * 60))
        except:
            continue

def askreddit_post_runner():
    while True:
        try:
            subreddit = reddit.subreddit("askreddit")
            submissions = list(subreddit.new(limit=10))
            submission = submissions[random.randint(0, len(submissions))]
            if submission.link_flair_text is not None:
                continue
            if submission.id in askreddit_post_ids_replied_to:
                print(f"{submission.id} found in already replied to.")
                continue
            askreddit_post_ids_replied_to.add(submission.id)
            print(f"Title: {submission.title}")
            my_comment = response.reply_to_question_post(submission.title)
            print(f"Reply: {my_comment}")
            submission.reply(my_comment)
            to_sleep_for = 60 * 7 + random.randint(0, 60)
            print(f"Sleeping for {to_sleep_for}...")
            time.sleep(to_sleep_for)
        except:
            continue

def askreddit_writing_prompt_runner():
    while True:
        try:
            subreddit = reddit.subreddit("writingprompts")
            submissions = list(subreddit.new(limit=10))
            submission = submissions[random.randint(0, len(submissions))]
            if submission.id in askreddit_post_ids_replied_to:
                print(f"{submission.id} found in already replied to.")
                continue
            askreddit_post_ids_replied_to.add(submission.id)
            print(f"Title: {submission.title}")
            my_comment = response.reply_to_writing_post(submission.title)
            print(f"Reply: {my_comment}")
            submission.reply(my_comment)
            to_sleep_for = 60 * 30 + random.randint(0, 60)
            print(f"Sleeping for {to_sleep_for}...")
            time.sleep(to_sleep_for)
        except:
            continue

askreddit_post_runner()
