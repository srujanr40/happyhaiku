import praw
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

   
reddit = praw.Reddit(client_id = os.getenv('CLIENT_ID'),
                     client_secret = os.getenv('CLIENT_SECRET'),
                     user_agent = os.getenv('USER_AGENT'),
                     username = os.getenv('USERNAME'),
                     password = os.getenv('PASSWORD'))

print(reddit.read_only)

subreddit = reddit.subreddit('GRE')
# display the subreddit name
print(subreddit.title)