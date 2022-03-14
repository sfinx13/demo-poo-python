from abc import ABC
from library.film import Film
import library.data as data

class FilmsLoader(ABC):
    def load(self, storage):
        films = []
        if len(data.storage_films) != 0:
            for item in storage:
                title = item[0][:-6].strip()
                created_at =  item[0][-5:-1]
                place =  self.search_borrower_by(title)
                type = item[1].upper()
                film = Film(title, created_at, place, type)
                films.append(film)
        
        return films
    
    def search_borrower_by(self, title):
        for item in data.storage_friends:
            if title != item[1]:
                borrower = 'Library'
            else:
                borrower = item[0]
                break
        
        return borrower
