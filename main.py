import random  #To get random words
from tkinter import * # For GUI
import time
import pandas  #To extract the data from CSV file
import pyttsx3 # For the voice Feature

BG = "#B1DDC6"
current_card = {}
to_learn = {}
engine = pyttsx3.init()


/*

PLEASE NAME THE FILE EXACTLY MENTIONED BELOW
(2 Files) in the data Folder: i. words_to_learn.csv
                        ii. spanish_words.csv

*/


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def speak():
  

def flip_card():
   

def is_known():
   
  

window = Tk()
window.title("FlipCard")
window.config(padx=50, pady=50, bg=BG) #padding: 50px to x and y

flip_timer = window.after(3000, func=flip_card) #Flips the card in 3 secs

canvas = Canvas(width=800, height=526) #This is the actual width and height of the app window.
card_front_img = PhotoImage(file="images/card_front.png")




next_card()
window.mainloop() # need this to keep the console window open
