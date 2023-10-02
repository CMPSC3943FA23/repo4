import random  #To get random words
from tkinter import * # For GUI
import time
import pandas  #To extract the data from CSV file
import pyttsx3 # For the voice Feature

BG = "#B1DDC6"
current_card = {}
to_learn = {}
engine = pyttsx3.init()
