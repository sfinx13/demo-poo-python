from library.films import Films
from library.friends import Friends
from library.friend import Friend
from pprint import pprint
import library.data as data

class App:
    menu_options = {
        1: 'Display films',
        2: 'Display friends',
        3: 'Sort films by year and title',
        4: 'Sort films by type',
        5: 'Pick random film',
        6: 'List borrowed films',
        7: 'List borrowed films by',
        8: 'Exit'
    }
    
    def __init__(self):
        self.title = "🎬 Welcome, please choose an option 🎬"
        self.films = Films(data.storage_films)
        self.friends = Friends(data.storage_friends)

    def show_options(self):
        print("🟢 Welcome, please choose an option 🟢")
        print("******************************************")
        for key in self.menu_options:
            print(f"👉 [{key}] - {self.menu_options[key]}")

    def run_option(self, option):
        try:
            self.title = self.menu_options[option]
            print(f"🟢 {self.title} 🟢")
            print("******************************************")
        except KeyError:
            print("🔴 Please enter a valid key menu item 🔴")
            print("******************************************")
        
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

def main():
    app = App()
    app.run()        

if __name__ == "__main__":
    main()
