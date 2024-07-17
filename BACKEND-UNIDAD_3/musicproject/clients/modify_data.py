import requests

# actualizar  artista
def update_artist(artist_id, new_data):
    url = f'http://127.0.0.1:8000/music/artist/{artist_id}/'  
    response = requests.put(url, data=new_data)
    if response.status_code == 200:
        print('Artista actualizado:', response.json())
    else:
        print('Error al actualizar el artista:', response.status_code)

#  eliminar un artista
def delete_artist(artist_id):
    url = f'http://127.0.0.1:8000/music/artist/{artist_id}/'  
    response = requests.delete(url)
    if response.status_code == 204:  
        print('Artista eliminado con éxito')
    else:
        print('Error al eliminar el artista:', response.status_code)

# Ejemplo de uso
update_artist(1, {'name': 'Empire Of The Sun', 'genre': 'Rock', 'popularity': 5})
# delete_artist(1)



# actualizar un álbum
def update_album(album_id, new_data):
    url = f'http://127.0.0.1:8000/music/album/{album_id}/'  
    response = requests.put(url, data=new_data)
    if response.status_code == 200:
        print('Álbum actualizado:', response.json())
    else:
        print('Error al actualizar el álbum:', response.status_code)

# eliminar un álbum
def delete_album(album_id):
    url = f'http://127.0.0.1:8000/music/album/{album_id}/'  
    response = requests.delete(url)
    if response.status_code == 204:  
        print('Álbum eliminado con éxito')
    else:
        print('Error al eliminar el álbum:', response.status_code)


# Ejemplo de uso
update_album(1, {'title': 'In the rainbow', 'artist': 1, 'release_date': '2008-08-30', 'popularity': 3})
# delete_album(1)
