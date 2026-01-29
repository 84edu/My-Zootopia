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
        output += '<li class="cards__item">'
        name = animal.get("name")
        if name:
            output += f'<div class="card__title">{name}</div><br/>\n'

        output += '  <p class="card__text">\n'
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        if diet:
           output += f"<strong>Diet:</strong> {diet}<br/>\n"

        location_data = animal.get("locations") or characteristics.get("locations") or characteristics.get("location")
        if location_data:
            if isinstance(location_data, list) and len(location_data) > 0:
                main_location = location_data[0]
            else:
                main_location = location_data

            output += f'<strong>Location:</strong> {main_location}</br>\n'

        type_info = characteristics.get("type")
        if type_info:
            output += f"<strong>Type:</strong> {type_info}<br/>\n"
        output += '</p>\n'
        output += '<li>\n'
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
