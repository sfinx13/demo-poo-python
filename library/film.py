from enum import Enum


class ContentType(Enum):
    VHF = "VHF"
    DVD = "DVD"


class Film():
    """ 
    >>> film = Film("Terminator 2", "1991", "John", "DVD")
    >>> print(film)
    Terminator 2
    >>> film
    ('1991', 'Terminator 2', 'John', 'DVD')
    >>> film.title
    'Terminator 2'
    >>> film.type
    'DVD'
    >>> film.created_at
    1991
    >>> film.title = "Titanic"
    >>> film.title
    'Titanic'
    >>> film.title = "R" 
    Traceback (most recent call last):
    ...
    ValueError: Film title is too short
    >>> film.type = "VVV" 
    Traceback (most recent call last):
    ...
    ValueError: Content tyde does not exist
    """
    def __init__(self, title, created_at, place, type):
        self._title = title
        self._created_at = int(created_at)
        self._place = place
        self._type = type

    def __str__(self):
        return f"{self._title}"

    def __repr__(self):
        return f"{str(self._created_at), self._title, self._place , self._type}"

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if len(title) > 1:
            self._title = title
        else:
            raise ValueError("Film title is too short")

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if type in list(ContentType):
            self._type = type
        else:
            raise ValueError("Content tyde does not exist")

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        if int(created_at) > 1950:
            self._title = created_at
        else:
            raise ValueError("We do not sell movies released before 1950")

if __name__ == '__main__':
    import doctest
    doctest.testmod()