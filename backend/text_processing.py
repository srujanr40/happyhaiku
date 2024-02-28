import nltk
nltk.data.path.append('./nltk_data')

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords, cmudict
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

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

def count_total_syllables(text):
    tokens = word_tokenize(text)
    return sum(count_syllables(word) for word in tokens)

def is_haiku(text):
    total_syllables = count_total_syllables(text)
    return total_syllables == 17

def filter_haikus(df):
    """
    Filter comment bodies that can be written as haikus.
    """
    haiku_comments = df[df['Body'].apply(is_haiku)]
    return haiku_comments


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



def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores['pos'] > 0 else 0
    return sentiment


def format_as_haiku(syllables_17):

    words = syllables_17.split()

    line1 = []
    line2 = []
    line3 = []
    
    syllable_count = 0
    line_counts = [5, 7, 5]

    
    for word in words:
        syllable_count += count_syllables(word)
        if syllable_count <= 5:
            line1.append(word)
        elif syllable_count <= 12:
            line2.append(word)
        else:
            line3.append(word)

    
    line1_str = ' '.join(line1)
    line2_str = ' '.join(line2)
    line3_str = ' '.join(line3)

    
    haiku_str = f"{line1_str}\n{line2_str}\n{line3_str}"

    return haiku_str

def apply_haiku_transformation(df):
    transformed_df = df.copy()
    transformed_df['Body'] = transformed_df['Body'].apply(lambda x: format_as_haiku(x) if isinstance(x, str) else x)
    return transformed_df



import reddit
df = reddit.get_top_50_comments('1b0z9fb')

df = filter_haikus(df)
df['Body'] = df['Body'].apply(preprocess_text)
df['sentiment'] = df['Body'].apply(get_sentiment)
df = df[df['sentiment'] == 1]
df = apply_haiku_transformation(df)
for index, row in df.iterrows():
    reddit.reply_as_haiku(row['id'], row['Body'])
print(df)



