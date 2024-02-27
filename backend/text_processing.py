import nltk
nltk.data.path.append('./nltk_data')

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords, cmudict
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import reddit
df = reddit.get_top_50_comments('1b0z9fb')

d = cmudict.dict()


def count_syllables(word):
    """
    Count syllables in a word based on the CMU Pronouncing Dictionary.
    """
    word = word.lower()
    if word in d:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word]][0]
    else:
        return 0  

def count_total_syllables(line):
    """
    Count total syllables in a line of text.
    """
    tokens = word_tokenize(line)
    return sum(count_syllables(word) for word in tokens)

def count_total_syllables(text):
    """
    Count total syllables in the text.
    """
    tokens = word_tokenize(text)
    return sum(count_syllables(word) for word in tokens)

def is_haiku(text):
    """
    Check if the text can be written as a haiku (total syllables == 17).
    """
    total_syllables = count_total_syllables(text)
    return total_syllables == 17

def filter_haikus(df):
    """
    Filter comment bodies that can be written as haikus.
    """
    haiku_comments = df[df['Body'].apply(is_haiku)]
    return haiku_comments

# create preprocess_text function
def preprocess_text(text):

    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text



analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores['pos'] > 0 else 0
    return sentiment

# df['reviewText'] = df['reviewText'].apply(preprocess_text)
# df['sentiment'] = df['reviewText'].apply(get_sentiment)

df = filter_haikus(df)
print(df)



