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
# StartQuestion = print(input("Welcome to the Home Price Predictors! Would you like to see the predicted home price? "))
# if StartQuestion == "Yes" or StartQuestion == "yes":
#    print(homesdata.head())
# elif StartQuestion == "No" or "No":
#     print("Okay then...")
PRICE = int(0)
POINTS = 0
# Draws the Tkinter window
win = Tk()
win.geometry("1000x500")
# Creating the category variables
Bathinput = int()
Bedinput = int()
Conditioninput = int()
Poolinput = ""
Yearinput = int()
Sizeinput = int()
Price = PRICE
# Defines a function of when the button is clicked
def estimation():
   Price = ("Your Home Price is:" + str(PRICE) + " dollars!")
   label= Label(frame, text= Price, font= ('Times New Roman', 14, 'italic'))
   label.pack(pady=30)
   entry.delete(0, 'end')
   
# Creates the frames for the window
frame = LabelFrame(win, width= 600, height= 400, bd=5)
frame.pack()

frame.pack_propagate(False)
# The content of the frames
entry = ttk.Entry(frame, width = 40)
Bath = ttk.Entry(frame, width= 40)
Bed = ttk.Entry(frame, width = 40)
Condition = ttk.Entry(frame, width = 40)
Pool = ttk.Entry(frame, width = 40)
Year = ttk.Entry(frame, width = 40)
Size = ttk.Entry(frame, width = 40)
Bath.insert(INSERT, "Bathroom # ")
Bed.insert(INSERT, "Bedroom # ")
Condition.insert(INSERT, "Condition (out of 10): ")
Pool.insert(INSERT, "Pool? ")
Year.insert(INSERT, "When was it built? ")
Size.insert(INSERT, "What is the size of your home? ")
Bath.pack()
Bed.pack()
Condition.pack()
Pool.pack()
Year.pack()
button = ttk.Button(win, text= "Estimate!", command = estimation).pack(pady=20)
if button:
    print("Your estimatied home price is" + str(PRICE) + " Dollars!")
win.mainloop()
if Conditioninput < 3:
  POINTS += 1
elif Conditioninput > 4 and Conditioninput < 7:
  POINTS += 2
elif Conditioninput > 7:
   POINTS += 3
# Will ask for how many bathrooms there are and will use the input to assign how many qualtiy points their hoem gets.
Bathinput = int(input("How many Bathrooms are there? "))
if Bathinput == 0:
   POINTS += 0
elif Bath == 1:
   POINTS += 1
elif Bathinput > 1 and Bathinput < 5:
   POINTS += 2
elif Bath > 4:
   POINTS += 3
# Processes the the user input of how many bedrooms 
Bedinput = int(input("How many Bedrooms are there? "))
if Bedinput == 0:
   POINTS += 0
elif Bedinput > 0 and Bedinput < 3:
   POINTS += 1
elif Bedinput > 2 and Bedinput < 6:
  POINTS += 2
elif Bedinput > 5:
   POINTS += 3
# Takes in the user input as a string value and will add points if it matches with the string value
Poolinput = input("Is there a Pool? ")
if Poolinput == "Yes" or Poolinput == "yes":
   POINTS += 2
else:
   POINTS +=0
# Asks for the age of the home and adds points to the corresponding answer
Yearinput = int(input("When was the home built? ")) 
if Yearinput < 1950:
   POINTS += 0
elif Yearinput > 1949 and Yearinput < 1965:
   POINTS += 1
elif Yearinput > 1954 and Yearinput < 1980:
   POINTS += 2
elif Yearinput > 1979 and Yearinput < 1995:
   POINTS += 3
elif Yearinput > 1994:
    POINTS += 4
# User inputs the size of the gome and points are added based off user input.
Sizeinput = int(input("How Large is the Home? "))
if Sizeinput < 1500:
   POINTS += 1
elif Sizeinput > 1499 and Sizeinput < 2500:
   POINTS += 2
elif Sizeinput > 2499 and Sizeinput < 3000:
   POINTS += 3
elif Sizeinput > 2999 and Sizeinput < 3500:
   POINTS += 4
elif Sizeinput > 3499 and Sizeinput < 4000:
   POINTS += 5
else: 
   POINTS += 6
# Will then give the Quality score of the home after the questions.
print("Your Home Quality Score is... " + str(POINTS))
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

