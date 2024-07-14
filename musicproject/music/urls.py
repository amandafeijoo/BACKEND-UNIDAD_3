from django.urls import path 
from .views import (
    ArtistListCreate, ArtistRetrieveUpdateDestroy, ArtistByGenreList,
    AlbumListCreate, AlbumRetrieveUpdateDestroy, AlbumByArtistList, PopularArtistsList, PopularAlbumsList, latest_album_by_artist
)

urlpatterns = [
    path('', ArtistListCreate.as_view(), name='home'),  # new
    path('artist/', ArtistListCreate.as_view(), name='artist-list-create'),
    path('artist/<int:pk>/', ArtistRetrieveUpdateDestroy.as_view(), name='artist-retrieve-update-destroy'),
    path('artist/genre/<str:genre>/', ArtistByGenreList.as_view(), name='artist-by-genre'),
    path('album/', AlbumListCreate.as_view(), name='album-list-create'),
    path('album/<int:pk>/', AlbumRetrieveUpdateDestroy.as_view(), name='album-retrieve-update-destroy'),
    path('artist/<int:artist_id>/albums/', AlbumByArtistList.as_view(), name='album-by-artist'),
    path('artists/popular/', PopularArtistsList.as_view(), name='popular-artists'),
    path('albums/popular/', PopularAlbumsList.as_view(), name='popular-albums'),
    path('artist/<int:artist_id>/latest_album/', latest_album_by_artist, name='artist-latest-album'),
]