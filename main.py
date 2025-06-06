import praw
import os
import sqlite3

import discord
from discord import commands
from datetime import datetime
from db import create_table, DB_NAME, insert_post, duplicate_check
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Reddit API
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'), 
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    )

client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Subreddit to scrape
subreddit = reddit.subreddit("todayilearned")

# Creates the database and table if they dont already exist
create_table()

# Get 10 latest posts
for post in subreddit.new():
    if post.score < 100:
        continue
    timestamp = datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
    saved_to = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Check for duplicates
    if duplicate_check(post.id):
        print(f"Duplicate post found: {post.title} (ID: {post.id})")
        continue
        
    # Save to database
    insert_post(post.id, post.title, post.score, timestamp, saved_to)
        
    # Console output
    print(f"{post.title}(Score: {post.score}), created at {timestamp}, saved to database {saved_to}")
    

