import json


class Importer:

    def __init__(self):
        self.tasks = []

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open("taski.json") as file:
            self.tasks = json.load(file)
        file.close()

    def get_tasks(self):
        return self.tasks
