import requests

BASE_URL = 'http://127.0.0.1:8000/music/'
URL_ARTIST = f'{BASE_URL}artist/'
URL_ALBUM = f'{BASE_URL}album/'

artists = [
    {'name': 'Radiohead', 'genre': 'Rock', 'popularity': 2},
   
]

albums = [
    {'title': 'OK Computer', 'artist': 'Radiohead', 'release_date': '2007-10-10', 'popularity': 1 },
]
artist_ids = {}
album_ids = {}
for artist in artists:
    response = requests.post(URL_ARTIST, data=artist)
    if response.status_code == 201:
        artist_id = response.json()['id']
        artist_ids[artist['name']] = artist_id
    else:
        print(f'Error al crear artista: {response.status_code} {response.text}')

for album in albums:
    artist_name = album['artist']
    if artist_name in artist_ids:
        album['artist'] = artist_ids[artist_name]
        response = requests.post(URL_ALBUM, data=album)
        if response.status_code == 201:
            album_id = response.json()['id']
            album_ids[album['title']] = album_id
        else:
            print(f'Error al crear álbum: {response.status_code} {response.text}')