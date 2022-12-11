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

# This will create the datsheet for the machine. It will then read and analyze the excel file.
# Then it will then show the data on a datasheet
# Analyze the pdf file which tells the info of houses and gives a sample of the homes.
homesdata = pd.read_excel("HomeData.xlsx")
StartQuestion = print(input("Welcome to the Home Price Predictors! Would you like to see the predicted home price? "))
if StartQuestion == "Yes" or StartQuestion == "yes":
    print(homesdata.head())
elif StartQuestion == "No" or "No":
    print("Okay then...")
PRICE = int(0)
POINTS = 0
# Draws the Tkinter window
win = Tk()
win.geometry("1000x500")
# Creating the category variables
Bath = int()
Bed = int()
Condition = int()
Pool = ""
Year = int()
Size = int()
# Defines a function of when the button is clicked
def myclick():
   Bed = input(int("Bedroom # "+ entry.get()))
   label= Label(frame, text= Bed, font= ('Times New Roman', 14, 'italic'))
   label.pack(pady=30)
   entry.delete(0, 'end')
   
   Bath = input(int("Bathroom # " + entry1.get()))
   label= Label(frame, text= Bath , font= ('Times New Roman', 14, 'italic'))
   entry1.delete(0, 'end')
   label.pack(pady=30)
    
   Condition = input(int("Condition (Out of 10) " + entry2.get()))
   label= Label(frame, text= Condition, font= ('Times New Roman', 14, 'italic'))
   entry2.delete(0, 'end')
   label.pack(pady=30)
   
   Year = input(int("Year Built: " + entry3.get()))
   label = Label(frame, text = Year, font = ('Times New Roman', 14, 'italic'))
   label.pack(pady = 30)
   entry3.delete(0, 'end')
# Creates the frames for the window
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()

frame.pack_propagate(False)
# The content of the frames
entry = ttk.Entry(frame, width= 40)
entry1 = ttk.Entry(frame, width = 40)
entry2 = ttk.Entry(frame, width = 40)
entry3 = ttk.Entry(frame, width = 40)
entry1.insert(INSERT, "Bathroom # ")
entry2.insert(INSERT, "Bedroom # ")
entry.insert(INSERT, "Your Home Price is: ")
entry3.insert(INSERT, "Year Built: ")
entry.pack()
entry1.pack()
entry2.pack()
entry3.pack()

ttk.Button(win, text= "Create", command= myclick).pack(pady=20)
win.mainloop()

# This will ask for the quality of the home and will then use the user input to add quality points to the house depending on the quality.
Condition = int(input("Now, On a scale out of ten... What is the condition of the home? "))
if Condition < 3:
  POINTS += 1
elif Condition > 4 and Condition < 7:
  POINTS += 2
elif Condition > 7:
   POINTS += 3
# Will ask for how many bathrooms there are and will use the input to assign how many qualtiy points their hoem gets.
Bath = int(input("How many Bathrooms are there? "))
if Bath == 0:
   POINTS += 0
elif Bath == 1:
   POINTS += 1
elif Bath > 1 and Bath < 5:
   POINTS += 2
elif Bath > 4:
   POINTS += 3
# Processes the the user input of how many bedrooms 
Bed = int(input("How many Bedrooms are there? "))
if Bed == 0:
   POINTS += 0
elif Bed > 0 and Bed < 3:
   POINTS += 1
elif Bed > 2 and Bed < 6:
  POINTS += 2
elif Bed > 5:
   POINTS += 3
# Takes in the user input as a string value and will add points if it matches with the string value
Pool = input("Is there a Pool? ")
if Pool == "Yes" or Pool == "yes":
   POINTS += 2
else:
   POINTS +=0
# Asks for the age of the home and adds points to the corresponding answer
Year = int(input("When was the home built? ")) 
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
Size = int(input("How Large is the Home? "))
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
print("Your Home Qualtiy Score is... " + str(POINTS))
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
print("Based on your home's quality, your estimated price will be: " + str(PRICE) + " Dollars!")

