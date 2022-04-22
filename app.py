from library.friends_loader import FriendsLoader
from library.films_loader import FilmsLoader
from library.friends import Friends
from library.films import Films
from pprint import pprint

SEPARATOR = "*"


class App:
    def __init__(self):
        self.title = "🎬 Welcome, please choose an option 🎬"
        self.films = Films(FilmsLoader())
        self.friends = Friends(FriendsLoader())
        self.menu_options = {
            1: 'Display films',
            2: 'Display friends',
            3: 'Sort films by year and title',
            4: 'Sort films by type',
            5: 'Pick random film',
            6: 'List borrowed films',
            7: 'List borrowed films by',
            8: 'Exit'
        }

    def show_options(self):
        print("🟢 Welcome, please choose an option 🟢")
        print(SEPARATOR * 40)
        for key in self.menu_options:
            print(f"👉 [{key}] - {self.menu_options[key]}")

    def run_option(self, option):
        try:
            self.title = self.menu_options[option]
            print(f"🟢 {self.title} 🟢")
            print(SEPARATOR * 40)
        except KeyError:
            print("🔴 Please enter a valid key menu item 🔴")
            print(SEPARATOR * 40)

        match option:
            case 1:
                pprint(self.films.get_films())
            case 2:
                pprint(self.friends.get_friends())
            case 3:
                self.films.sort_by_year_and_title()
                pprint(self.films.get_films())
            case 4:
                self.films.sort_by(field="type")
                pprint(self.films.get_films())
            case 5:
                pprint(self.films.pick_random_film())
            case 6:
                pprint(self.films.get_borrowed_films())
            case 7:
                friend = input("Enter a friend: ")
                pprint(self.films.get_borrowed_films(friend))
            case 8:
                exit()

    def run(self):
        while(True):
            self.show_options()
            self.run_option(int(input('Please enter an option:')))
