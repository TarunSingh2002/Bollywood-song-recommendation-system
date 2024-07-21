import os
import random
import pickle
import pandas as pd
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='/static', static_folder='static')

df = pd.read_csv(r'data/raw/data.csv')
with open(r'models/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

if not os.path.exists('static/images'):
    os.makedirs('static/images')

for index, row in df.iterrows():
    image_path = f'static/images/{index}.jpg'
    if not os.path.exists(image_path):
        row['thumbnail_image'].save(image_path)

def recommend(song_name):
    song_index = df[df['song_name'] == song_name].index[0]
    distance = similarity[song_index]
    song_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommendations = []
    for i in song_list:
        song_data = df.iloc[i[0]]
        image_url = f'/static/images/{i[0]}.jpg'
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
        
    all_songs = [{'name': row['song_name'], 'thumbnail': f'/static/images/{index}.jpg'} for index, row in df.iterrows()]
    selected_song_image = f'/static/images/{df[df["song_name"] == song_name].index[0]}.jpg'
    return render_template('index.html', song_name=song_name, recommendations=recommendations, all_songs=all_songs, selected_song_image=selected_song_image)

@app.route('/get_image/<song_name>', methods=['GET'])
def get_image(song_name):
    song_index = df[df['song_name'] == song_name].index[0]
    image_url = f'/static/images/{song_index}.jpg'
    return jsonify({'image_url': image_url})

@app.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'css'), filename)

@app.route('/static/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'), filename)

def handler(event, context):
    asgi_app = WsgiToAsgi(app)
    asgi_handler = Mangum(asgi_app)
    return asgi_handler(event, context)