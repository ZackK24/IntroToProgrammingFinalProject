# Sources and Overview of the Project.
# https://www.w3schools.com/python/python_ml_linear_regression.asp
# https://colab.research.google.com/drive/1zk6NgYiR2UPzzmjzyhGbEduSt3gZHi7b
'''
This code will tell you what the projected price of a home would be based of the 
user's input of the the home
'''
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import Button, Entry, END

# This will create the datsheet for the machine. It will then read and analyze the excel file.
# Then it will then show the data on a datasheet
# Analyze the pdf file which tells the info of houses and gives a sample of the homes.
homesdata = pd.read_excel("HomeData.xlsx")
StartQuestion = (input("Welcome to the Home Price Predictors! Would you like to see the predicted home price? "))
if StartQuestion == "Yes" or StartQuestion == "yes":
   print("Here are your samples: ")  
   print(homesdata.head())
else:
   print("Okay then...")
PRICE = int(0)
POINTS = int
# Draws the Tkinter window
win = Tk()
win.geometry("1000x500")
# Creating the category variables
Price = PRICE
frame = LabelFrame(win, width= 600, height= 400, bd=5)
Bath = IntVar(win, value = '0')
Bed = IntVar(win, value = '0')
Condition = IntVar(win, value = '0')
Pool = ttk.Entry(frame, width = 40)
Year= IntVar(win, value = '0')
Size = IntVar(win, value = '0')

frame.pack()
frame.pack_propagate(False)
# Creates the entries that are on the window
entry = ttk.Entry(frame, width = 40)
Question = ttk.Entry(frame, width = 40)
Bath = ttk.Entry(frame, width= 40)
Bed = ttk.Entry(frame, width = 40)
Condition = ttk.Entry(frame, width = 40)
Pool = ttk.Entry(frame, width = 40)
Year = ttk.Entry(frame, width = 40)
Size = ttk.Entry(frame, width = 40)
# Creates the answers that use integers into those that accept integers
Bath = Entry(win, textvariable=Bath).pack()
Bed = Entry(win, textvariable = Bed).pack()
Condition = Entry(win, textvariable = Condition).pack()
Year = Entry(win, testvariable = Year).pack()
Size = Entry(win, testvariable = Size).pack()
# Inserts the Entry text into the box
Question.insert(INSERT, "Please enter your house characteristics: ")
Bath.insert(INSERT, "Bathroom # ")
Bed.insert(INSERT, "Bedroom # ")
Condition.insert(INSERT, "Condition (out of 10): ")
Pool.insert(INSERT, "Pool? ")
Year.insert(INSERT, "When was it built? ")
Size.insert(INSERT, "What is the size of your home? ")
# Generates the entry onto the window
Question.pack()
Bath.pack()
Bed.pack()
Condition.pack()
Pool.pack()
Year.pack()
Size.pack()
# Defines a function of when the button is clicked
def estimation():
   PRICE = int(0)
   POINTS = int
   if Condition < 3:
      POINTS += 1
   elif Condition > 4 and Condition < 7:
      POINTS += 2
   elif Condition > 7:
      POINTS += 3
# Will ask for how many bathrooms there are and will use the input to assign how many qualtiy points their hoem gets.
   if Bath == 0:
      POINTS += 0
   elif Bath == 1:
      POINTS += 1
   elif Bath > 1 and Bath < 5:
      POINTS += 2
   elif Bath > 4:
      POINTS += 3
# Processes the the user input of how many bedrooms 
   if Bed == 0:
      POINTS += 0
   elif Bed > 0 and Bed < 3:
      POINTS += 1
   elif Bed > 2 and Bed < 6:
      POINTS += 2
   elif Bed > 5:
      POINTS += 3
# Takes in the user input as a string value and will add points if it matches with the string value
   if Pool == "Yes" or Pool == "yes":
      POINTS += 2
   else:
      POINTS +=0
# Asks for the age of the home and adds points to the corresponding answer
   if Year < 1950:
      POINTS += 0
   elif Year > 1949 and Year < 1965:
      POINTS += 1
   elif Year > 1954 and Year < 1980:
      POINTS += 2
   elif Year > 1979 and Year < 1995:
      POINTS += 3
   elif Year > 1994:
      POINTS += 4
# User inputs the size of the gome and points are added based off user input.
   if Size < 1500:
      POINTS += 1
   elif Size > 1499 and Size < 2500:
      POINTS += 2
   elif Size > 2499 and Size < 3000:
      POINTS += 3
   elif Size > 2999 and Size < 3500:
      POINTS += 4
   elif Size > 3499 and Size < 4000:
      POINTS += 5
   else: 
      POINTS += 6
# Will then give the Quality score of the home after the questions.
# Will use the amount of Quality Points to then estimate how long much the hoem will cost.
   if POINTS == 0:
      PRICE += 0
   elif POINTS > 0 and POINTS < 6:
      PRICE += 250000
   elif POINTS > 5 and POINTS < 11:
      PRICE += 400000
   elif POINTS > 10 and POINTS < 16:
      PRICE += 550000
   elif POINTS > 15 and POINTS < 21:
      PRICE += 700000
   elif POINTS > 20:
      PRICE += 825000
   Points = ("Your Home Quality Score is: " + str(POINTS) + " Points!")
   Price = ("Your Home Price is:" + str(PRICE) + " dollars!")
   label1 = Label(frame, text = Points, font = ('Times New Roman', 14, 'italic'))
   label= Label(frame, text= Price, font= ('Times New Roman', 14, 'italic'))
   label1.pack(pady = 30)
   label.pack(pady=30)
   entry.delete(0, 'end')
ttk.Button(win, text= "Estimate!", command = estimation).pack(pady=20)
win.mainloop()


