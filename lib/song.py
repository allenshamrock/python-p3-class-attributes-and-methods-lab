class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {} 

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
