import praw
import pandas as pd
import os
from dotenv import load_dotenv


def get_top_50_comments(post_id):

    load_dotenv()
    try:
        reddit = praw.Reddit(client_id = os.getenv('CLIENT_ID'),
                        client_secret = os.getenv('CLIENT_SECRET'),
                        user_agent = os.getenv('USER_AGENT'),
                        username = os.getenv('USERNAME'),
                        password = os.getenv('PASSWORD'))
    except:
        print('Error authenticating with Reddit API')
        return None

    comments_data = []
    
    post = reddit.submission(id=post_id)
    post.comments.replace_more(limit=None)
    comments = post.comments[:50]

    for comment in comments:
        comments_data.append({
            'Comment ID': comment.id,
            'Author': comment.author.name if comment.author else '[deleted]',
            'Body': comment.body,
            'Score': comment.score,
            'Created UTC': pd.to_datetime(comment.created_utc, unit='s')
        })

    
    comments_df = pd.DataFrame(comments_data)

    return comments_df

def reply_as_haiku(comment_id, reply_text):
    reply_text = "Your comment deserves a haiku! \n" + reply_text
    load_dotenv()
    reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                         client_secret=os.getenv('CLIENT_SECRET'),
                         user_agent=os.getenv('USER_AGENT'),
                         username=os.getenv('USERNAME'),
                         password=os.getenv('PASSWORD'))

    comment = reddit.comment(comment_id)
    comment.reply(reply_text)
