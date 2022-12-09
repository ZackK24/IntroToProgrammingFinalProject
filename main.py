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
print(homesdata.head())
# This will ask for the quality of the home and will then use the user input to add quality points to the house depending on the quality.
Condition = int(input("One a scale out of ten... What is the qaultiy of the home? "))
POINTS = 0
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