import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animals_data(animals_data):
    for animal in animals_data:
        name = animal.get("name")
        if name:
            print(f"Name: {name}")

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        if diet:
            print(f"Diet: {diet}")

        location = characteristics.get("location")
        if location and len(location) > 0:
            print(f"Location: {location}")

        type = characteristics.get("type")
        if type:
            print(f"Type: {type}")

        print('-' * 30)


def main():
    animals_data = load_data('animals_data.json')
    get_animals_data(animals_data)

if __name__ == "__main__":
    main()