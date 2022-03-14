from abc import ABC
from library.friend import Friend

class FriendsLoader(ABC):    
    def load(self, storage):
        friends = []
        if len(storage) != 0:
            for item in storage:
                firstname = item[0]
                film_title = item[1] if len(item) > 1 else "" 
                friend = Friend(firstname, film_title)
                friends.append(friend)

        return friends
