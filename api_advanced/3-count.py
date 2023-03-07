#!/usr/bin/python3
""""Doc"""

import praw

def count_words(subreddit, word_list, count_dict=None):
    if count_dict is None:
        count_dict = {}
    reddit = praw.Reddit(user_agent='Counting Keywords Bot (by /u/YourRedditUsername)',
                         client_id='YourClientID', client_secret='YourClientSecret')
    try:
        hot_posts = reddit.subreddit(subreddit).hot(limit=100)
    except Exception:
        return None
    for post in hot_posts:
        words = post.title.lower().split()
        for word in word_list:
            if word.lower() in words:
                if word.lower() in count_dict:
                    count_dict[word.lower()] += words.count(word.lower())
                else:
                    count_dict[word.lower()] = words.count(word.lower())
    if not count_dict:
        return None
    sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for item in sorted_count:
        print("{}: {}".format(item[0], item[1]))

        # Recursive call
    count_words(subreddit, word_list, count_dict)
