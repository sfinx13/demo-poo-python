from library.friends_loader import FriendsLoader

class Friends():
    def __init__(self, friends_loader):
        if isinstance(friends_loader, FriendsLoader):
            self.friends = friends_loader.load()
        
    def find(self, index):
        return self.friends[index]
    
    def get_friends(self):
        return self.friends
