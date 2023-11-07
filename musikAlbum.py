import random


class MusicAlbum:

    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def get_info(self):
        print(f'''
Название: {self.title}
Исполнитель: {self.artist}
Релиз: {self.release_year}
Жанр: {self.genre}
Список треков: {self.tracklist}
''')
    def play_random_track(self):
        return random.choice(self.tracklist)

album4 = MusicAlbum("Пропаганда денег", "Scally Milano", 2022, "HIP-HOP",
                    ["Подкован", "Большие Бабки", "Я Украду Твои Деньги", "По Пятам",
                     "Недоволен", "GLO"])
album4.play_random_track()
print(album4.play_random_track())
