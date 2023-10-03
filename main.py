import random  #To get random words
from tkinter import * # For GUI
import time
import pandas  #To extract the data from CSV file
import pyttsx3 # For the voice Feature

BG = "#B1DDC6"
current_card = {}
to_learn = {}
engine = pyttsx3.init()













window = Tk()
window.title("FlipCard")
window.config(padx=50, pady=50, bg=BG) #padding: 50px to x and y

flip_timer = window.after(3000, func=flip_card) #Flips the card in 3 secs

canvas = Canvas(width=800, height=526) #This is our actual width and height of the app window.
