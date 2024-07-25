import os
import awsgi
import random
import pickle
import pandas as pd
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

S3_BASE_URL = os.environ.get('S3_BASE_URL', "https://my-bollywood-static-files.s3.amazonaws.com/static")

df = pd.read_csv(r'data/raw/data.csv')
with open(r'models/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

def recommend(song_name):
    song_index = df[df['song_name'] == song_name].index[0]
    distance = similarity[song_index]
    song_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommendations = []
    for i in song_list:
        song_data = df.iloc[i[0]]
        image_url = f'{S3_BASE_URL}/images/{i[0]}.jpg'
        recommendations.append({
            'song_name': song_data['song_name'],
            'spotify_link': song_data['spotify_track_link'],
            'artist_name': song_data['artist_name'],
            'artist_link': song_data['artist_link'],
            'thumbnail': image_url
        })
    return recommendations

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        song_name = request.form['song_name']
        recommendations = recommend(song_name)
    else:
        song_name = random.choice(df['song_name'].tolist())
        recommendations = []  
    all_songs = [{'name': row['song_name'], 'thumbnail': f'{S3_BASE_URL}/images/{index}.jpg'} for index, row in df.iterrows()]
    selected_song_image = f'{S3_BASE_URL}/images/{df[df["song_name"] == song_name].index[0]}.jpg'
    songs_data = df.to_dict(orient='records')
    
    return render_template('index.html', song_name=song_name, recommendations=recommendations, all_songs=all_songs, selected_song_image=selected_song_image, songs_data=songs_data, S3_BASE_URL=S3_BASE_URL)

def handler(event, context):
    return awsgi.response(app, event, context)

# if __name__ == "__main__":
#     app.run(debug=True)