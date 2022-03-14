class Friend:
    def __init__(self, firstname, film_title = ''):
        self.firstname = firstname
        self.film_title = film_title
        
    def __repr__(self):
        return f"{self.firstname,  self.film_title}"

    def __str__(self):
        return f"{self.firstname}"

