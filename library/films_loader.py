import library.data as data
from library.film import Film
from library.friends_loader import FriendsLoader


class FilmsLoader:
    def load(self):
        films = []
        if len(data.storage_films) != 0:
            for item in data.storage_films:
                title = item[0][:-6].strip()
                created_at = item[0][-5:-1]
                place = FriendsLoader.search_borrower_by(title)
                type = item[1].upper()
                film = Film(title, created_at, place, type)
                films.append(film)

        return films
