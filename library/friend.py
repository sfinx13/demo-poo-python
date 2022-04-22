class Friend:
    """
    >>> friend = Friend('John', 'Terminator')
    >>> friend.firstname
    'John'
    >>> friend
    ('John', 'Terminator')
    >>> print(friend)
    John
    """
    def __init__(self, firstname, film_title=''):
        self.firstname = firstname
        self.film_title = film_title

    def __repr__(self):
        return f"{self.firstname,  self.film_title}"

    def __str__(self):
        return f"{self.firstname}"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
