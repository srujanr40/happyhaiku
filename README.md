# HappyHaiku

This Python application utilizes the Natural Language Toolkit (NLTK) to analyze the sentiments of comments on Reddit. It detects the sentiment of the comments and checks if they resemble a haiku, a traditional form of Japanese poetry characterized by its structure of three lines with 5, 7, and 5 syllables respectively. If a comment is identified as a haiku and is positive, the application replies to that comment with a message formatted as a haiku.

## Features:

- Analyzes sentiments of Reddit comments using NLTK.
- Identifies comments that resemble a haiku based on syllable count.
- Replies to haiku-like comments with messages formatted as haikus.
- Configurable settings for Reddit API access.
- Containerized with Docker for easy deployment and management.

## Usage: 

1. Install Docker on your machine following the official Docker documentation.
2. Build the Docker image from the provided Dockerfile:
```docker build -t reddit_sentiment_haiku .```
4. Run the Docker container: 
```docker run reddit_sentiment_haiku```

## Dependencies:

NLTK: Natural Language Toolkit for natural language processing tasks.
PRAW: Python Reddit API Wrapper for accessing Reddit’s API.
Docker: 

## Contributing:
Contributions to improve the code, add features, or fix bugs are welcome. Please submit pull requests or raise issues for any enhancements or problems encountered.
