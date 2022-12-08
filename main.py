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
# Analyze the pdf file which tells the info of houses and the different prices that they have
homesdata = pd.read_excel("HomeData.xlsx")
print(homesdata.head())
Condition = int(input("One a scale out of ten... What is the waultiy of the home? "))
qualitypoints = 0
if Condition == 0 and Condition < 3:
    qualitypoints + 1
elif Condition > 4 and Condition < 7:
    qualitypoints + 2
elif Condition > 7:
    qualitypoints + 3
print(qualitypoints)
