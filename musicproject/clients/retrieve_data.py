import requests


# GET a los artistas por género
url = 'http://127.0.0.1:8000/music/artist/genre/Rock/'  
response = requests.get(url)
if response.status_code == 200:
    print('Artistas por género:', response.json())
else:
    print('Error:', response.status_code)

# GET a los artistas más populares
url = 'http://127.0.0.1:8000/music/artists/popular/'  
response = requests.get(url)
if response.status_code == 200:
    print('Artistas más populares:', response.json())
else:
    print('Error:', response.status_code)

# GET a los álbumes por artista
url = 'http://127.0.0.1:8000/music/artist/1/albums/' 
response = requests.get(url)
if response.status_code == 200:
    print('Álbumes por artista:', response.json())
else:
    print('Error:', response.status_code)

# GET a los álbumes más populares

url = 'http://127.0.0.1:8000/music/albums/popular/'  
response = requests.get(url)
if response.status_code == 200:
    print('Álbumes más populares:', response.json())
else:
    print('Error:', response.status_code)

# GET al álbum más reciente de un artista
url = 'http://127.0.0.1:8000/music/artist/1/latest_album/'  
response = requests.get(url)
if response.status_code == 200:
    print('Álbum más reciente del artista:', response.json())
else:
    print('Error:', response.status_code)
