class Character:
    def __init__(self,edited,name,created,gender,skin_color,hair_color,height,eye_color,mass,homeworld,birth_year):
        self.edited = edited
        self.name = name
        self.created = created
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.height = height
        self.eye_color = eye_color
        self.mass = mass
        self.homeworld = homeworld
        self.birth_year = birth_year

    @property
    def info(self):
        info_text = f"Name: {self.name}, Gender: {self.gender}, Homeworld: {self.homeworld}, Birth Year: {self.birth_year}"
        return info_text  
    
    def __str__(self):
        return (" Edited: " + str(self.edited) +
                " Name: " + str(self.name) +
                " Created: " + str(self.created )+
                " Gender: " + str(self.gender) +
                " Skin_color: " + str(self.skin_color) +
                " Hair_color: " + str(self.hair_color )+
                " Height: " + str(self.height )+
                " Eye_color: " + str(self.eye_color) +
                " Mass: " + str(self.mass )+
                " Homeworld: " + str(self.homeworld) +
                " Birth_year: " + str(self.birth_year) )


