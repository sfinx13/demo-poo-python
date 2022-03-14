from library.friends_loader import FriendsLoader
from pprint import pprint

class Friends(FriendsLoader):
    def __init__(self, storage):
        self.friends = super().load(storage)
        
    def find(self, index):
        return self.friends[index]
    
    def get_friends(self):
        return self.friends
