import json
from character import Character
from character_films import Character_films

def main():
    film_list = []  
    with open ("StarWars.json","r") as j:

        star_wars_data = json.load(j)
    
    info_chewbacca = ("3-8", "Star Wars: Episodio III - La venganza del Sith", "Star Wars: Episodio VIII - Los ultimos Jedis")
    info_anakin = ("1-6,9", "Star Wars: Episodio I - La Amenaza Fantasma", "Star Wars: Episodio VI - El retorno del Jedi")
    info_luke= ("3-9", "Star Wars: Episodio III - La venganza del Sith", "Star Wars: Episodio VIII - Los ultimos Jedis")
        
    for film_character in star_wars_data:
        if film_character['fields']['name'] == "Luke Skywalker":
            actor = Character_films(
            film_character['fields']['edited'], 
            film_character['fields']['name'], 
            film_character['fields']['created'], 
            film_character['fields']['gender'], 
            film_character['fields']['skin_color'], 
            film_character['fields']['hair_color'], 
            film_character['fields']['height'], 
            film_character['fields']['eye_color'], 
            film_character['fields']['mass'], 
            film_character['fields']['homeworld'], 
            film_character['fields']['birth_year'],
            info_luke[0],
            info_luke[1],
            info_luke[2]
            )
        elif film_character['fields']['name'] == "Anakin Skywalker":
            actor = Character_films(
            film_character['fields']['edited'], 
            film_character['fields']['name'], 
            film_character['fields']['created'], 
            film_character['fields']['gender'], 
            film_character['fields']['skin_color'], 
            film_character['fields']['hair_color'], 
            film_character['fields']['height'], 
            film_character['fields']['eye_color'], 
            film_character['fields']['mass'], 
            film_character['fields']['homeworld'], 
            film_character['fields']['birth_year'],
            info_anakin[0],
            info_anakin[1],
            info_anakin[2]
            )
        elif film_character['fields']['name'] == "Chewbacca":
            actor = Character_films(
            film_character['fields']['edited'], 
            film_character['fields']['name'], 
            film_character['fields']['created'], 
            film_character['fields']['gender'], 
            film_character['fields']['skin_color'], 
            film_character['fields']['hair_color'], 
            film_character['fields']['height'], 
            film_character['fields']['eye_color'], 
            film_character['fields']['mass'], 
            film_character['fields']['homeworld'], 
            film_character['fields']['birth_year'],
            info_chewbacca[0],
            info_chewbacca[1],
            info_chewbacca[2]
            )
        else:
            actor = Character(
            film_character['fields']['edited'], 
            film_character['fields']['name'], 
            film_character['fields']['created'], 
            film_character['fields']['gender'], 
            film_character['fields']['skin_color'], 
            film_character['fields']['hair_color'], 
            film_character['fields']['height'], 
            film_character['fields']['eye_color'], 
            film_character['fields']['mass'], 
            film_character['fields']['homeworld'], 
            film_character['fields']['birth_year']
            )
        film_list.append(actor)

    for film_character in film_list:
        print(film_character)    
    
    print(film_list[0].info)

    create_output_json(film_list)
    

def create_output_json(film_list):
    serializable_data = []

    for film_character in film_list:
        if isinstance(film_character, Character_films):
            character_data = {
                "edited": film_character.edited,
                "name": film_character.name,
                "created": film_character.created,
                "gender": film_character.gender,
                "skin_color": film_character.skin_color,
                "hair_color": film_character.hair_color,
                "height": film_character.height,
                "eye_color": film_character.eye_color,
                "mass": film_character.mass,
                "homeworld": film_character.homeworld,
                "birth_year": film_character.birth_year,
                "num_of_films": film_character.num_of_films,
                "first_film": film_character.first_film,
                "alive_at_the_end": film_character.alive_at_the_end
            }
        else:
            character_data = {
                "edited": film_character.edited,
                "name": film_character.name,
                "created": film_character.created,
                "gender": film_character.gender,
                "skin_color": film_character.skin_color,
                "hair_color": film_character.hair_color,
                "height": film_character.height,
                "eye_color": film_character.eye_color,
                "mass": film_character.mass,
                "homeworld": film_character.homeworld,
                "birth_year": film_character.birth_year
            }

        serializable_data.append(character_data)

    
    with open("updated_StarWars.json", "w") as f:
        json.dump(serializable_data, f, indent=4)

main()