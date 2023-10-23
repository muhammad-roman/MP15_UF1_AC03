from character import Character

class Character_films(Character):
    def __init__(self,edited,name,created,gender,skin_color,hair_color,height,eye_color,mass,homeworld,birth_year, num_of_films, first_film, alive_at_the_end):
        super().__init__(edited,name,created,gender,skin_color,hair_color,height,eye_color,mass,homeworld,birth_year)
        self.num_of_films = num_of_films
        self.first_film = first_film
        self.alive_at_the_end = alive_at_the_end
       
    @property
    def num_of_films(self):
        return self._num_of_films

    @num_of_films.setter
    def num_of_films(self, value):
        self._num_of_films = value

    @property
    def first_film(self):
        return self._first_film

    @first_film.setter
    def first_film(self, value):
        self._first_film = value

    @property
    def alive_at_the_end(self):
        return self._alive_at_the_end

    @alive_at_the_end.setter
    def alive_at_the_end(self, value):
        self._alive_at_the_end = value