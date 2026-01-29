import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html(file_path):
    """Read the HTML file as text."""
    with open(file_path, "r") as handle:
        return handle.read()


def get_animals_data(animals_data):
    """A long string with all animals data"""
    output = ""
    for animal in animals_data:
        name = animal.get("name")
        if name:
            output += f"Name: {name}\n"

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        if diet:
           output += f"Diet: {diet}\n"

        location = characteristics.get("location")
        if location and len(location) > 0:
            output += f"Location: {location[0]}\n"

        type_info = characteristics.get("type")
        if type_info:
            output += f"Type: {type_info}\n"

    return output


def main(animals_string=None):
    animals_data = load_data('animals_data.json')
    template_content = load_html("animals_template.html")
    animals_string = get_animals_data(animals_data)
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    with open("animals.html", "w") as file:
        file.write(new_html_content)


if __name__ == "__main__":
    main()
