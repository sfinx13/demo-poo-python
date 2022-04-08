import unittest
from library.film import Film
from library.friend import Friend

class TestModel(unittest.TestCase):
    def test_film_is_valid(self):
        film = Film("Terminator 2", "1991", "John", "DVD")
        self.assertTrue(film.title == 'Terminator 2')
        self.assertTrue(film.created_at == 1991)
        self.assertTrue(film.place == 'John')
        self.assertTrue(film.type == 'DVD')
        self.assertIsInstance(film, Film)

    def test_friend_is_valid(self):
        friend = Friend('John', 'Terminator 2')
        self.assertTrue(friend.firstname == 'John')
        self.assertTrue(friend.film_title == 'Terminator 2')
        self.assertIsInstance(friend, Friend)

    def test_film_is_not_valid_wih_wrong_title(self):
        with self.assertRaises(ValueError):
            film = Film()
            film.title = 'T'

    def test_film_is_not_valid_wih_wrong_year(self):
        with self.assertRaises(ValueError):
            film = Film()
            film.year = 1912

    def test_film_is_not_valid_wih_wrong_type(self):
        with self.assertRaises(ValueError):
            film = Film()
            film.type = 'YTHG'
    
