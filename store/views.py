from django.shortcuts import render
from .models import Artist, Album

def home(request):
    return render(request, 'home.html')

def artist_list(request):
    artists = Artist.objects.all().order_by('debut_year')
    return render(request, 'artist_list.html', {'artists': artists})

def album_list(request):
    albums = Album.objects.all().order_by('release_date')
    return render(request, 'album_list.html', {'albums': albums})
