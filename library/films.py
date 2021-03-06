from library.films_loader import FilmsLoader
from library.film import Film
from operator import attrgetter
import random


class Films():
    def __init__(self, films_loader):
        if isinstance(films_loader, FilmsLoader):
            self.films = films_loader.load()

    def add_film(self, film):
        if isinstance(film, Film):
            self.films.append(film)

    def sort_by_year_and_title(self):
        self.films = sorted(self.films, key=attrgetter('created_at', 'title'))

    def sort_by(self, field="type"):
        self.films = sorted(self.films, key=attrgetter(field))

    def pick_random_film(self):
        random_number = random.randint(0, len(self.films) - 1)
        return self.films[random_number]

    def get_borrowed_films(self, friend=""):
        if not friend:
            return list(
                    filter(lambda film: film._place != 'Library', self.films)
                )
        return list(filter(lambda film: film._place == friend, self.films))

    def get_films(self):
        return self.films
