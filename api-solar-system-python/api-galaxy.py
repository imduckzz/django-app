import requests
import os

api_url = "https://api.le-systeme-solaire.net/rest/bodies/"

def get_data(category):
    os.system("clear") 
    print(":::::: SOLAR SYSTEM INFORMATION ::::::")
    print("--------------------------------------")
    try:
        
        response = requests.get(api_url, params={'filter[]': category})
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

def print_menu():
    print("[1] Planets")
    print("[2] Moons")
    print("[3] Stars")
    print("[4] Asteroid")
    print("[5] Comets")
    print("[6] Exit")

#Main
while True:
    print_menu()
    choice = input("Press an option: ")
    if choice == '6':
        print("Leaving the program...")
        break  
    elif choice not in ['1', '2', '3', '4', '5']:
        print("Invalid option")
        continue  

    info = get_data(choice)
    if info:
        if choice == '1':
            planet_data = [body for body in info['bodies'] if body.get('bodyType') == 'Planet']
            if planet_data:
                for planet in planet_data:
                    print("--------------------------------------")
                    print("::::::::::::::: PLANET :::::::::::::::")
                    print("English Name:", planet.get('englishName'), end=", ")
                    print("Gravity:", planet.get('gravity'), end=", ")
                    print("Inclination:", planet.get('inclination'), end=", ")
                    print("Is Planet? :", planet.get('isPlanet'))

            else:
                print("No planets found.")
        elif choice== '2':
            moon_data = [body for body in info['bodies'] if body.get('bodyType') == 'Moon']
            if moon_data:
                for moon in moon_data:
                    print("--------------------------------------")
                    print(":::::::::::::::: MOON ::::::::::::::::")
                    print("English Name:", moon.get('englishName'), end=", ")
                    print("Gravity:", moon.get('gravity'), end=", ")
                    print("Inclination:", moon.get('inclination'), end=", ")
                    print("Is Planet? :", moon.get('isPlanet'))
            else:
                print("No Moons found.")
        elif choice== '3':
            star_data = [body for body in info['bodies'] if body.get('bodyType') == 'Star']
            if star_data:
                for star in star_data:
                    print("--------------------------------------")
                    print(":::::::::::::::: STAR ::::::::::::::::")
                    print("English Name:", star.get('englishName'), end=", ")
                    print("Gravity:", star.get('gravity'), end=", ")
                    print("Inclination:", star.get('inclination'), end=", ")
                    print("Is Planet? :", star.get('isPlanet'))
            else:
                print("No Stars found.")
        elif choice== '4':
            asteroid_data = [body for body in info['bodies'] if body.get('bodyType') == 'Asteroid']
            if asteroid_data:
                for asteroid in asteroid_data:
                    print("--------------------------------------")
                    print(":::::::::::::: ASTEROID ::::::::::::::")
                    print("English Name:", asteroid.get('englishName'), end=", ")
                    print("Gravity:", asteroid.get('gravity'), end=", ")
                    print("Inclination:", asteroid.get('inclination'), end=", ")
                    print("Is Planet? :", asteroid.get('isPlanet'))
            else:
                print("No Asteroids found.")
        elif choice== '5':
            comet_data = [body for body in info['bodies'] if body.get('bodyType') == 'Comet']
            if comet_data:
                for comet in comet_data:
                    print("--------------------------------------")
                    print("::::::::::::::: COMET ::::::::::::::::")
                    print("English Name:", comet.get('englishName'), end=", ")
                    print("Gravity:", comet.get('gravity'), end=", ")
                    print("Inclination:", comet.get('inclination'), end=", ")
                    print("Is Planet? :", comet.get('isPlanet'))
            else:
                print("No Comets found.")
    print("--------------------------------------")           
    input("Press enter to continue...")
