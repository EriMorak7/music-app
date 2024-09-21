# store/populate.py
from .models import Artist, Album

def populate():
    artists_data = [
        ("The Beatles", 1960),
        ("Taylor Swift", 2006),
        ("Drake", 2009),
        ("Adele", 2008),
        ("Coldplay", 1996),
    ]

    albums_data = [
        ("Abbey Road", "1969-09-26", "The Beatles"),
        ("1989", "2014-10-27", "Taylor Swift"),
        ("Take Care", "2011-11-15", "Drake"),
        ("21", "2011-01-24", "Adele"),
        ("Parachutes", "2000-07-10", "Coldplay"),
        ("Mylo Xyloto", "2011-10-24", "Coldplay"),
        ("Red", "2012-10-22", "Taylor Swift"),
        ("Hello", "2015-10-23", "Adele"),
    ]

    for name, debut_year in artists_data:
        artist = Artist.objects.create(name=name, debut_year=debut_year)

    for title, release_date, artist_name in albums_data:
        artist = Artist.objects.get(name=artist_name)
        Album.objects.create(title=title, release_date=release_date, artist=artist)

