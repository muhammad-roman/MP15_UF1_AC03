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

    #prueba
    for film_character in film_list:
        print(f"Name: {film_character.edited}")

    example1 = Character("2014-12-20T21:17:56.891Z","Luke Skywalker","2014-12-09T13:50:51.644Z","male","fair","blond","172","blue","77",1,"19BBY")
    example2 = Character_films("2014-12-20T21:17:56.891Z","AAAA Skywalker","2014-12-09T13:50:51.644Z","male","fair","blond","172","blue","77",1,"19BBY", 1, "blabla" ,True)

    #print pruebas
    print(example1.edited)
    print(example1.info)
    print(example2.alive_at_the_end)
    print(example2.info)

main()