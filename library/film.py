class Film():
    def __init__(self, title, created_at, place, type):
        self.title = title
        self.created_at = int(created_at)
        self.place = place
        self.type = type

    def __str__(self):
        return f"{self.title}"
        
    def __repr__(self):
        return f"{str(self.created_at), self.title, self.place , self.type}"
