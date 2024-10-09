import sys

# Keep original code after the installation
import praw
import pandas as pd
import os
from dotenv import load_dotenv
def get_top_posts(subreddit_lists='VentureCapital', limit=500, time_filter='all'):

    #Create a Read-only instance
    reddit = praw.Reddit(client_id='',
                    client_secret='',
                      redirect_uri="http://localhost:8080",
                      user_agent=''
    )
    # Fetch top posts
    posts = reddit.subreddit(subreddit_lists).top(time_filter=time_filter, limit=limit)

    # Initialize post dataframe
    posts_df = []

    for post in posts:
        posts_df.append({'post_id': post.id,
                     'subreddit': post.subreddit,
                     'created_utc': post.created_utc,
                     'selftext': post.selftext,
                     'post_url': post.url,
                     'post_title': post.title,
                     'link_flair_text': post.link_flair_text,
                     'score': post.score,
                     'num_comments': post.num_comments,
                     'upvote_ratio': post.upvote_ratio
                     })

    return  pd.DataFrame(posts_df)

#posts arguments corrected
posts_df = get_top_posts(subreddit_lists='VentureCapital+povertyfinance', limit=1500, time_filter='all')
posts_df.to_csv('VS_PV_posts.csv', header=True, index=False)
posts_df


def get_top_posts(subreddit_lists='VentureCapital', limit=500, time_filter='all'):

    # Create a Read-only instance
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         redirect_uri="http://localhost:8080",
                         user_agent='')

    # Fetch top posts
    posts = reddit.subreddit(subreddit_lists).top(time_filter=time_filter, limit=limit)

    # Initialize post dataframe
    posts_df = []

    for post in posts:
        posts_df.append({
            'post_id': post.id,
            'subreddit': post.subreddit.display_name,
            'created_utc': post.created_utc,
            'selftext': post.selftext,
            'post_url': post.url,
            'post_title': post.title,
            'link_flair_text': post.link_flair_text,
            'score': post.score,
            'num_comments': post.num_comments,
            'upvote_ratio': post.upvote_ratio
        })

    return pd.DataFrame(posts_df)

# Fetch posts from the specified subreddits
posts_df = get_top_posts(subreddit_lists='VentureCapital+povertyfinance', limit=1500, time_filter='all')

# Sort the DataFrame by the 'score' column in descending order
sorted_posts_df = posts_df.sort_values(by='score', ascending=False)

# Optionally, filter to keep only the top N posts
top_n_posts = 1000  # Change this number to keep the top N posts you want
top_rated_posts_df = sorted_posts_df.head(top_n_posts)

# Save the top-rated posts to a CSV file
top_rated_posts_df.to_csv('VS_PV_top_rated_posts.csv', header=True, index=False)

# Display the top-rated posts DataFrame
top_rated_posts_df

# creating a dataframe
try:
    # replace all caps placeholders with your snowflake credentials
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user='YOUR_USERNAME', 
        password='password',
        account='YOUR_ACCOUNT',
        warehouse='YOUR_WAREHOUSE', 
        database='YOUR_DATABASE', 
        schema='YOUR_SCHEMA'
    )

    # Write the DataFrame to Snowflake
    top_rated_posts_df.to_sql('TOP_RATED_POSTS', conn, schema='PUBLIC', if_exists='replace', index=False)

    # Close the Snowflake connection
    conn.close()

except snowflake.connector.errors.ProgrammingError as e: 
    print("Connection failed, check your credentials.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    # Check if 'conn' exists in the local symbols table
    if 'conn' in locals():
        conn.close()

# Display the top-rated posts DataFrame
top_rated_posts_df
import praw
import pandas as pd
import snowflake.connector

def get_top_posts(subreddit_lists='VentureCapital', limit=500, time_filter='all'):
    # Create a Read-only instance
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         redirect_uri="",
                         user_agent='')

    # Fetch top posts
    posts = reddit.subreddit(subreddit_lists).top(time_filter=time_filter, limit=limit)

    # Initialize post dataframe
    posts_df = []

    for post in posts:
        posts_df.append({
            'post_id': post.id,
            'subreddit': post.subreddit.display_name,
            'created_utc': post.created_utc,
            'selftext': post.selftext,
            'post_url': post.url,
            'post_title': post.title,
            'link_flair_text': post.link_flair_text,
            'score': post.score,
            'num_comments': post.num_comments,
            'upvote_ratio': post.upvote_ratio
        })

    return pd.DataFrame(posts_df)

# Fetch posts from the specified subreddits
posts_df = get_top_posts(subreddit_lists='VentureCapital+povertyfinance', limit=1500, time_filter='all')

# Sort the DataFrame by the 'score' column in descending order
sorted_posts_df = posts_df.sort_values(by='score', ascending=False)

# Optionally, filter to keep only the top N posts
top_n_posts = 1000  # Change this number to keep the top N posts you want
top_rated_posts_df = sorted_posts_df.head(top_n_posts)

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='',
    password='',
    account='',
    warehouse='',
    database='',
    schema=''
)

# Write the DataFrame to Snowflake
top_rated_posts_df.to_sql('TOP_RATED_POSTS', conn, schema='PUBLIC', if_exists='replace', index=False)

# Close the Snowflake connection
conn.close()

# Display the top-rated posts DataFrame
top_rated_posts_df


import praw
import pandas as pd
import snowflake.connector

def get_top_posts(subreddit_lists='VentureCapital', limit=500, time_filter='all'):
    # Create a Read-only instance
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         redirect_uri="",
                         user_agent='')

    # Fetch top posts
    posts = reddit.subreddit(subreddit_lists).top(time_filter=time_filter, limit=limit)

    # Initialize post dataframe
    posts_df = []

    for post in posts:
        posts_df.append({
            'post_id': post.id,
            'subreddit': post.subreddit.display_name,
            'created_utc': post.created_utc,
            'selftext': post.selftext,
            'post_url': post.url,
            'post_title': post.title,
            'link_flair_text': post.link_flair_text,
            'score': post.score,
            'num_comments': post.num_comments,
            'upvote_ratio': post.upvote_ratio
        })

    return pd.DataFrame(posts_df)

# Fetch posts from the specified subreddits
posts_df = get_top_posts(subreddit_lists='VentureCapital+povertyfinance', limit=1500, time_filter='all')

# Sort the DataFrame by the 'score' column in descending order
sorted_posts_df = posts_df.sort_values(by='score', ascending=False)

# Optionally, filter to keep only the top N posts
top_n_posts = 1000  
top_rated_posts_df = sorted_posts_df.head(top_n_posts)

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='',
    password='',
    account='',
    warehouse='Reddit_Data',  
    database='Reddit_Data',   
    schema='Reddit_Data'      
)

# Write the DataFrame to Snowflake
top_rated_posts_df.to_sql('TOP_RATED_POSTS', conn, schema='PUBLIC', if_exists='replace', index=False)

# Close the Snowflake connection
conn.close()

# Display the top-rated posts DataFrame
top_rated_posts_df

import sqlalchemy as sa


# Load environment variables from the .env file.
# Make sure that your .env file path is correctly pointed to.
load_dotenv()

def get_top_posts(subreddit_lists='VentureCapital', limit=500, time_filter='all'):
    # Check that the environment variables have been set.
    if not os.getenv('REDDIT_CLIENT_ID') or not os.getenv('REDDIT_CLIENT_SECRET'):
        raise Exception("Environment variables REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET must be set.")
    
    # Create a Reddit read-only instance with the environment variables set.
    reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                         client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                         user_agent='Round-Two3952')

    # Fetch top posts.
    posts = reddit.subreddit(subreddit_lists).top(time_filter=time_filter, limit=limit)
    posts_df = []
    for post in posts:
        posts_df.append({
            'post_id': post.id,
            'subreddit': post.subreddit.display_name,
            'created_utc': post.created_utc,
            'selftext': post.selftext,
            'post_url': post.url,
            'post_title': post.title,
            'link_flair_text': post.link_flair_text,
            'score': post.score,
            'num_comments': post.num_comments,
            'upvote_ratio': post.upvote_ratio
        })

    return pd.DataFrame(posts_df)

# Fetch top posts, sort them and take the top N posts.
posts_df = get_top_posts(subreddit_lists='VentureCapital+povertyfinance', limit=1500, time_filter='all')
sorted_posts_df = posts_df.sort_values(by='score', ascending=False)
top_n_posts = 1000 
top_rated_posts_df = sorted_posts_df.head(top_n_posts)

# Create SQLAlchemy engine for Snowflake.
engine = sa.create_engine('snowflake://{user}:{password}@{account}/{database}/{schema}'.format(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account='et34745.eu-central-2.aws',
    database='REDDIT_DATA',
    schema='REDDIT_DATA'
))

# Write the DataFrame to Snowflake.
top_rated_posts_df.to_sql('TOP_RATED_POSTS', engine, if_exists='replace', index=False)

# Display the top-rated DataFrame.
top_rated_posts_df


# Load environment variables from the .env file.
# Make sure that your .env file path is correctly pointed to.
load_dotenv()

def get_top_posts(subreddit_lists='VentureCapital', limit=500, time_filter='all'):
    # Check that the environment variables have been set.
    if not os.getenv('REDDIT_CLIENT_ID') or not os.getenv('REDDIT_CLIENT_SECRET'):
        raise Exception("Environment variables REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET must be set.")
    
    # Create a Reddit read-only instance with the environment variables set.
    reddit = praw.Reddit(client_id='',
                    client_secret='',
                      redirect_uri="http://localhost:8080",
                      user_agent='')
    
    # ... rest of the code remains unchanged ...
import os
import sqlalchemy as sa
import pandas as pd
import praw

def get_top_posts(subreddit_lists='VentureCapital', limit=500, time_filter='all'):
    # Create a Read-only instance
    client_id = ''
    client_secret = ''
    
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent='Round-Two3952')

    # Fetch top posts
    posts = reddit.subreddit(subreddit_lists).top(time_filter=time_filter, limit=limit)
    posts_df = []
    for post in posts:
        posts_df.append({
            'post_id': post.id,
            'subreddit': post.subreddit.display_name,
            'created_utc': post.created_utc,
            'selftext': post.selftext,
            'post_url': post.url,
            'post_title': post.title,
            'link_flair_text': post.link_flair_text,
            'score': post.score,
            'num_comments': post.num_comments,
            'upvote_ratio': post.upvote_ratio
        })

    return pd.DataFrame(posts_df)

# Fetch top posts, sort them, and take the top N posts
posts_df = get_top_posts(subreddit_lists='VentureCapital+povertyfinance', limit=1500, time_filter='all')
sorted_posts_df = posts_df.sort_values(by='score', ascending=False)
top_n_posts = 1000 
top_rated_posts_df = sorted_posts_df.head(top_n_posts)

# Create SQLAlchemy engine for Snowflake
engine = sa.create_engine('snowflake://{user}:{password}@{account}/{database}/{schema}'.format(
    user='',
    password='',
    account='',
    database='',
    schema=''
))

# Write the DataFrame to Snowflake
top_rated_posts_df.to_sql('TOP_RATED_POSTS', engine, if_exists='replace', index=False)

# Display the top-rated DataFrame
print(top_rated_posts_df)
import os
import sqlalchemy as sa
import pandas as pd
import praw

def get_top_posts(subreddit_lists='VentureCapital', limit=500, time_filter='all'):
    # Create a Read-only instance
    client_id = ''
    client_secret = ''
    
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent='Round-Two3952')

    # Fetch top posts
    posts = reddit.subreddit(subreddit_lists).top(time_filter=time_filter, limit=limit)
    posts_df = []
    for post in posts:
        posts_df.append({
            'post_id': post.id,
            'subreddit': post.subreddit.display_name,
            'created_utc': post.created_utc,
            'selftext': post.selftext,
            'post_url': post.url,
            'post_title': post.title,
            'link_flair_text': post.link_flair_text,
            'score': post.score,
            'num_comments': post.num_comments,
            'upvote_ratio': post.upvote_ratio
        })

    return pd.DataFrame(posts_df)

# Fetch top posts, sort them, and take the top N posts
posts_df = get_top_posts(subreddit_lists='VentureCapital+povertyfinance', limit=1500, time_filter='all')
sorted_posts_df = posts_df.sort_values(by='score', ascending=False)
top_n_posts = 1000 
top_rated_posts_df = sorted_posts_df.head(top_n_posts)

# Create SQLAlchemy engine for Snowflake
engine = sa.create_engine('snowflake://{user}:{password}@{account}/{database}/{schema}'.format(
    user='',
    password='',
    account='',
    database='',
    schema=''
))

# Write the DataFrame to Snowflake
top_rated_posts_df.to_sql('TOP_RATED_POSTS', engine, if_exists='replace', index=False)

# Display the top-rated DataFrame
print(top_rated_posts_df)

# Check the table in Snowflake via Python
import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='',
    password='',
    account='',
    warehouse='',
    database='',
    schema=''
)

# Create a cursor object
cur = conn.cursor()

# Query the table
cur.execute("SELECT * FROM REDDIT_DATA.REDDIT_DATA.TOP_RATED_POSTS LIMIT 10")

# Fetch the results
results = cur.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()