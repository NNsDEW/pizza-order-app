import json

DATA_FILE = "data.json"

def read_data():
    """Читает данные из JSON-файла."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def write_data(data):
    """Записывает данные в JSON-файл."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

