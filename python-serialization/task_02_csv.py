import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en fichier JSON.

    Paramètre :
        csv_filename (str) : nom du fichier CSV à lire.

    Retourne :
        True si la conversion réussit, False si le fichier est introuvable.
    """
    try:
        with open(csv_filename, "r") as file:
            panda = csv.DictReader(file)
            data = list(panda)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
