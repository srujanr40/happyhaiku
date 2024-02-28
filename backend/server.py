from flask import Flask, Response
import reddit
import text_processing

app = Flask(__name__)

@app.route('/')
def health_check():
    return Response('Healthy!', status=200)


@app.route('/<postID>')
def generate_haiku(postID):
    try:
        df = reddit.get_top_50_comments('1b0z9fb')
    except:
        return Response('Error fetching comments', status=500)


    df = filter_haikus(df)
    df['Body'] = df['Body'].apply(preprocess_text)
    df['sentiment'] = df['Body'].apply(get_sentiment)
    df = df[df['sentiment'] == 1]
    df = apply_haiku_transformation(df)
    try:
        for index, row in df.iterrows():
            reddit.reply_as_haiku(row['id'], row['Body'])
    except:
        return Response('Error replying as haiku', status=500)

    return Response('Success!', status=200)

    

