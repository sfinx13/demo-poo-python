from library.friend import Friend
import library.data as data

class FriendsLoader:    
    def load(self):
        friends = []
        if len(data.storage_friends) != 0:
            for item in data.storage_friends:
                firstname = item[0]
                film_title = item[1] if len(item) > 1 else "" 
                friend = Friend(firstname, film_title)
                friends.append(friend)

        return friends
