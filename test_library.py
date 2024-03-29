import unittest
from library.film import Film
from library.films import Films
from library.friend import Friend
from library.friends import Friends
from library.friends_loader import FriendsLoader
from library.films_loader import FilmsLoader
from library.data import storage_films, storage_friends


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


class TestLoader(unittest.TestCase):
    TERMINATOR = 'Terminator 2 : Le Jugement dernier'
    BLADE_RUNNER = 'Blade Runner'
    BOYZ_N_HOOD = 'Boyz n the Hood'

    def test_film_is_loaded(self):
        film_loader = FilmsLoader()
        films = film_loader.load()
        self.assertEqual(len(films), len(storage_films))
        self.assertTrue(all(isinstance(film, Film) for film in films))
        self.assertEqual(self.TERMINATOR, films[9].title)

    def test_friend_is_loaded(self):
        friend_loader = FriendsLoader()
        friends = friend_loader.load()
        self.assertEqual(len(friends), len(storage_friends))
        self.assertTrue(all(isinstance(friend, Friend) for friend in friends))
        self.assertEqual('Paul', friends[0].firstname)

    def test_borrower_is_found(self):
        self.assertTrue(
            'Paul',
            FriendsLoader.search_borrower_by(self.BLADE_RUNNER)
        )
        self.assertTrue(
            'Lucie',
            FriendsLoader.search_borrower_by(self.BOYZ_N_HOOD)
        )
        self.assertTrue(
            'Zoé',
            FriendsLoader.search_borrower_by(self.TERMINATOR)
        )


class TestCollection(unittest.TestCase):
    def setUp(self):
        self.films = Films(FilmsLoader())
        self.friends = Friends(FriendsLoader())

    def test_film_is_added(self):
        nb_films = len(self.films.get_films())
        film = Film("Terminator 3", "2013", "John", "DVD")
        self.films.add_film(film)
        self.assertEqual(len(self.films.get_films()), nb_films + 1)

    def test_films_collection_is_equal_storage(self):
        self.assertEqual(len(self.films.get_films()), len(storage_films))

    def test_friends_founded(self):
        self.assertIsInstance(self.friends.find(0), Friend)

    def test_random_film_is_instance_film(self):
        self.assertIsInstance(self.films.pick_random_film(), Film)
