from tkinter import *
import random
import requests

window = Tk()
window.title("Periodic Table Top Trumps")
window.geometry("600x500")


# window.configure(background="beige")

#####

def random_element() -> object:
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


#####

def play_atomicNumber():
    global text

    my_stat = my_element['atomicNumber']
    opponent_stat = opponent_element['atomicNumber']

    if my_stat > opponent_stat:
        Label(window, text="\nYou Win!").pack()
        Label(window, text="\nThe value you had was: {}".format(my_stat)).pack()
        Label(window, text="\nYour opponent had the value: {}".format(opponent_stat)).pack()

    elif my_stat < opponent_stat:
        Label(window, text="\nYou Lose!").pack()
        Label(window, text="\nThe value you had was: {}".format(my_stat)).pack()
        Label(window, text="\nYour opponent had the value: {}".format(opponent_stat)).pack()

    else:
        Label(window, text="Draw!\n You both had the same value!").pack()
    return


#####

def play_boilingPoint():
    global text

    my_stat = my_element['boilingPoint']
    opponent_stat = opponent_element['boilingPoint']

    if my_stat > opponent_stat:
        Label(window, text="\nYou Win!").pack()
        Label(window, text="\nThe value you had was: {}".format(my_stat)).pack()
        Label(window, text="\nYour opponent had the value: {}".format(opponent_stat)).pack()

    elif my_stat < opponent_stat:
        Label(window, text="\nYou Lose!").pack()
        Label(window, text="\nThe value you had was: {}".format(my_stat)).pack()
        Label(window, text="\nYour opponent had the value: {}".format(opponent_stat)).pack()

    else:
        Label(window, text="Draw!\n You both had the same value!").pack()
    return


#####

def play_density():
    global text

    my_stat = my_element['density']
    opponent_stat = opponent_element['density']

    if my_stat > opponent_stat:
        Label(window, text="\nYou Win!").pack()
        Label(window, text="\nThe value you had was: {}".format(my_stat)).pack()
        Label(window, text="\nYour opponent had the value: {}".format(opponent_stat)).pack()

    elif my_stat < opponent_stat:
        Label(window, text="\nYou Lose!").pack()
        Label(window, text="\nThe value you had was: {}".format(my_stat)).pack()
        Label(window, text="\nYour opponent had the value: {}".format(opponent_stat)).pack()

    else:
        Label(window, text="Draw!\n You both had the same value!").pack()
    return


#####

# game title
title = Label(window, text="Welcome to the Periodic Table Top Trumps!", font=("Helvetica Bold", 20), bg="light blue",
              fg="white").pack(pady=20)

my_element = random_element()
Label(window, text="You were given the element:", font="Arial 15 italic", bg="light blue", fg="white").pack(pady=20)
Label(window, text="{}".format(my_element['name']), fg="purple").pack()


# icons

def icon():
    if my_element == "hydrogen":
        icon = PhotoImage(file=r"C:\Users\tol28845\PycharmProjects\cfg-python\Week 7\Elements icons\hydrogen.jpg")
    elif my_element == "helium":
        icon = PhotoImage(file=r"C:\Users\tol28845\PycharmProjects\cfg-python\Week 7\Elements icons\helium.jpg")
    else:
        icon = PhotoImage(file=r"C:\Users\tol28845\PycharmProjects\cfg-python\Week 7\Elements icons\lithium.jpg")


Label(window, Image=icon).pack(pady=20)

opponent_element = random_element()

# game instruction
Label(window, text="Which stat would you like to play with?", font="Arial 15 italic", bg="light blue", fg="white").pack(
    pady=20)

# buttons
btn_atomicNumber = Button(window, text="Atomic Number", fg="green", command=play_atomicNumber).pack(pady=5)

btn_boilingPoint = Button(window, text="Boiling Point", fg="red", command=play_boilingPoint).pack(pady=5)

btn_density = Button(window, text="Density", fg="orange", command=play_density).pack(pady=5)

#####
window.mainloop()
