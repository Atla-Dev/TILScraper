import praw
import os
import sqlite3

from datetime import datetime
from connect import create_table, database


# Load environment variables

from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect('reddit_posts.db')



# Reddit API

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'), 
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    )


# Subreddit to scrape
subreddit = reddit.subreddit("todayilearned")

# Get 10 latest posts
for post in subreddit.new(limit=10):
    if post.score < 100:
        continue
    else:
        timestamp = datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{post.title}(Score: {post.score}), created at {timestamp}")
    
