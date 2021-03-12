def make_album(artist, title):
    """Takes an artist name  and a title and makes an album."""
    album = {'artist': artist.title(), 'title': title.title()}
    return album

album1 = make_album('ishaan', 'the rocking band')
print(album1)

album2 = make_album('ojas', 'the small kids\' band')
print(album2)

album3 = make_album('shubham', 'the picture band')
print(album3)