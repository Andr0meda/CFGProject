import random
import requests
import tkinter as tk

screen = tk.Tk()
screen.title("Periodic Table Top Trumps")
screen.geometry("500x500")


def random_element():
    random_element = random.randint(1, 118)
    url = 'https://periodictableapi.herokuapp.com/api/getElement/byAtomicNumber/{}'.format(random_element)

    response = requests.get(url)
    element = response.json()

    dictionary = {
        'name': element['name'],
        'atomicNumber': element['atomicNumber'],
        'boilingPoint': element['boilingPoint'],
        'density': element['density'],
        }
    return dictionary

