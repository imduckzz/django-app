import requests
import os

def get_comet_data(api_key):
    os.system("clear")
    print(":::::::::::::: COMET INFORMATION :::::::::::::::")
    print("------------------------------------------------")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"
    try:  
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

def print_menu():
    print("::::::::::::::::::::::SHOW::::::::::::::::::::::")
    print("------------------------------------------------")
    print("[1] Comet name")
    print("[2] Absolute magnitude")
    print("[3] Estimated  diameter max (KM)")
    print("[4] Estimated  diameter min (KM)")
    print("[5] Estimated diameter max  (FT)")
    print("[6] Estimated diameter min  (FT)")
    print("[7] Orbital_data")
    print("[8] Show everything")
    print("[9] Exit")

while True:
    print_menu()
    choice = input("Press an option: ")
    if choice == '9':
        print("Leaving the program...")
        break  
    elif choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print("Invalid option")
        continue  
    api_key_nasa = 'c9hkw2qN7iXHdixPD2OKlTMNTNBe0x1qFGxkABFo'
    info = get_comet_data(api_key_nasa)
    if info:
        if choice == '1':
            print(f"Comet name: {info['name']}")
            print("------------------------------------------------")        
        elif choice== '2':
            print(f"Absolute magnitude: {info['absolute_magnitude_h']}")
            print("------------------------------------------------")
        elif choice == '3':
            print(f"Estimated diameter max (KM): {info['estimated_diameter']['kilometers']['estimated_diameter_max']}")
            print("------------------------------------------------")
        elif choice == '4':
            print(f"Estimated diameter min (KM): {info['estimated_diameter']['kilometers']['estimated_diameter_min']}")
            print("------------------------------------------------")
        elif choice == '5':
            print(f"Estimated diameter max (FT): {info['estimated_diameter']['feet']['estimated_diameter_max']}")
            print("------------------------------------------------")
        elif choice == '6':
            print(f"Estimated diameter min (FT): {info['estimated_diameter']['feet']['estimated_diameter_min']}")
            print("------------------------------------------------")
        elif choice == '7':
            print("::::::ORBITAL DATA::::::::")
            print(f"Last Observation date: {info['orbital_data']['last_observation_date']}")
            print(f"Orbit class description: {info['orbital_data']['orbit_class']['orbit_class_description']}")
            print("------------------------------------------------")  
        elif choice == '8':
            print(f"Comet name: {info['name']}")
            print(f"Absolute magnitude: {info['absolute_magnitude_h']}")
            print(f"Estimated diameter max (KM): {info['estimated_diameter']['kilometers']['estimated_diameter_max']}")
            print(f"Estimated diameter min (KM): {info['estimated_diameter']['kilometers']['estimated_diameter_min']}")
            print(f"Estimated diameter max (FT): {info['estimated_diameter']['feet']['estimated_diameter_max']}")
            print(f"Estimated diameter min (FT): {info['estimated_diameter']['feet']['estimated_diameter_min']}")
            print("::::::ORBITAL DATA::::::::")
            print(f"Last Observation date: {info['orbital_data']['last_observation_date']}")
            print(f"Orbit class description: {info['orbital_data']['orbit_class']['orbit_class_description']}")
            print("------------------------------------------------") 
        
