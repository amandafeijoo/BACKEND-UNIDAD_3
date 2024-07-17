from rest_framework import serializers
from .models import Artist, Album

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name','genre', 'popularity']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'artist', 'title', 'release_date', 'popularity']