import pandas

BACKGROUND_COLOR = "#B1DDC6"

import pandas as pd

import random


DATA = pd.read_csv("data/french_words.csv")

to_learn = DATA.to_dict(orient="records")

current_card={}


import tkinter as tk
import smptp
try :
    data = pandas.read_csv("data/words_to_learn.csv")


except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def next_card():

    global current_card
    current_card = random.choice(to_learn)




    canvas.itemconfig(title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    canvas.itemconfig(canvas_image, image=front_card)
def flip_card():

    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(title, text = "English")
    canvas.itemconfig(card_word,text = current_card["English"])
    # window.after(3000,func=flip_card)
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()
# def is_known():
#         to_learn.remove(current_card)


window = tk.Tk()
window.title('Flashcard App')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#create a canvas

canvas = tk.Canvas(width=800,height=526)

canvas.create_text(400,150,text="Flashcard App Game",font=("Ariel",40,"italic"))


front_card = tk.PhotoImage(file = "images/card_front.png")
back_card=tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(300, 300, image=front_card)




canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)

canvas.grid(row=0,column=0)
title = canvas.create_text(400,150,text="Title",font = ("Arial",40,"italic"))

card_word = canvas.create_text(400,300,text="", font = ("Arial",40,"bold"))





wrong = tk.PhotoImage(file = "images/wrong.png")
wrong_button = tk.Button(image= wrong,command=flip_card)
wrong_button.grid(column=0,row=1)

known = tk.PhotoImage(file = "images/right.png")
known_button = tk.Button(image=known,command=is_known)
known_button.grid(column=1,row=1)

next_card()
window.mainloop()
