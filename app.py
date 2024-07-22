import os
import random
import pickle
import pandas as pd
import requests
from io import BytesIO
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)

df = pd.read_csv(r'data/raw/data.csv')
file_ids_df = pd.read_csv(r'data/images/file_ids.csv')
with open(r'models/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

GOOGLE_DRIVE_BASE_URL = "https://drive.google.com/uc?id="

def recommend(song_name):
    song_index = df[df['song_name'] == song_name].index[0]
    distance = similarity[song_index]
    song_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommendations = []
    for i in song_list:
        song_data = df.iloc[i[0]]
        image_url = f'/get_image/{i[0]}'
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
        
    all_songs = [{'name': row['song_name'], 'thumbnail': f'/get_image/{index}'} for index, row in df.iterrows()]
    selected_song_image = f'/get_image/{df[df["song_name"] == song_name].index[0]}'
    return render_template('index.html', song_name=song_name, recommendations=recommendations, all_songs=all_songs, selected_song_image=selected_song_image)

@app.route('/get_image/<int:song_index>', methods=['GET'])
def get_image(song_index):
    google_drive_id = file_ids_df[file_ids_df['numbering id'] == song_index]['google drive id'].values[0]
    image_url = GOOGLE_DRIVE_BASE_URL + google_drive_id
    response = requests.get(image_url)
    return send_file(BytesIO(response.content), mimetype='image/jpeg')

@app.route('/static/css/<path:filename>')
def serve_css(filename):
    css_url = GOOGLE_DRIVE_BASE_URL + '1OBv1C7FI890H9q5lIJ6CFtx7SPmNwX-V'  # Google Drive ID of your style.css file
    response = requests.get(css_url)
    return send_file(BytesIO(response.content), mimetype='text/css')

def handler(event, context):
    asgi_app = WsgiToAsgi(app)
    asgi_handler = Mangum(asgi_app)
    return asgi_handler(event, context)

if __name__ == "__main__":
    app.run(debug=True)