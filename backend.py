import os
import json
import requests

API_KEY = 'AIzaSyACQN62sWB45n5IOucZauQU1a04Y9KCBa4'
SEARCH_ENGINE_ID = 'b54df523b3476449d'


def create_symptom_queries(filename, priority='top'):
    with open(symptom_file, "r") as read_file:
        keywords = json.load(read_file)

    print(keywords)

    return query

def search_for_diagnostics(query, page=1):
    start = (page - 1) * 10 + 1

    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    info = requests.get(url).json()

    return info

if __name__ == '__main__':
    symptom_file = os.path.join(os.path.realpath(os.path.dirname(__file__)), "examples/symptoms.json")

    query = create_symptom_queries(symptom_file)