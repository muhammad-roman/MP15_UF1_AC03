import json
from character import Character
from character_films import Character_films

def main():
    film_list = []  
    with open ("StarWars.json","r") as j:

        star_wars_data = json.load(j)

    #arreglar    
    for film_character in star_wars_data:
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
    '''
    #prueba
    for film_character in film_list:
        print(f"Edited: {film_character.edited}")

    example1 = Character("2014-12-20T21:17:56.891Z","Luke Skywalker","2014-12-09T13:50:51.644Z","male","fair","blond","172","blue","77",1,"19BBY")
    example2 = Character_films("2014-12-20T21:17:56.891Z","AAAA Skywalker","2014-12-09T13:50:51.644Z","male","fair","blond","172","blue","77",1,"19BBY", 1, "blabla" ,True)

    #print pruebas
    print(example1.edited)
    print(example1.info)
    print(example2.alive_at_the_end)
    print(example2.info)
'''

    info_chewabacca = ("3-8", "Star Wars: Episodio III - La venganza del Sith", "Star Wars: Episodio VIII - Los últimos Jedis")
    info_anakin = ("1-6,9", "Star Wars: Episodio I - La Amenaza Fantasma", "Star Wars: Episodio VI - El retorno del Jedi")
    info_luke= ("3-9", "Star Wars: Episodio III - La venganza del Sith", "Star Wars: Episodio VIII - Los últimos Jedis")


    for film_character in film_list:
        if film_character.name == "Chewbacca":
            film_character = Character_films(
                film_character.edited,
                film_character.name,
                film_character.created,
                film_character.gender,
                film_character.skin_color,
                film_character.hair_color,
                film_character.height,
                film_character.eye_color,
                film_character.mass,
                film_character.homeworld,
                film_character.birth_year,
                info_chewabacca[0],
                info_chewabacca[1],
                info_chewabacca[2])
        if film_character.name == "Luke Skywalker":
            film_character = Character_films(
                film_character.edited,
                film_character.name,
                film_character.created,
                film_character.gender,
                film_character.skin_color,
                film_character.hair_color,
                film_character.height,
                film_character.eye_color,
                film_character.mass,
                film_character.homeworld,
                film_character.birth_year,
                info_luke[0],
                info_luke[1],
                info_luke[2])
        if film_character.name == "Anakin Skywalker":
            film_character = Character_films(
                film_character.edited,
                film_character.name,
                film_character.created,
                film_character.gender,
                film_character.skin_color,
                film_character.hair_color,
                film_character.height,
                film_character.eye_color,
                film_character.mass,
                film_character.homeworld,
                film_character.birth_year,
                info_anakin[0],
                info_anakin[1],
                info_anakin[2])

    for film_character in film_list:
        print(film_character)    
    

main()