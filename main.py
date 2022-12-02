# Sources and Overview of the Project.
'''
This code will tell you what the projected price of a home in San Jose
will be based on what kind of house you would like to have.

Sources:
https://www.w3schools.com/python/python_ml_linear_regression.asp
https://colab.research.google.com/drive/1zk6NgYiR2UPzzmjzyhGbEduSt3gZHi7b
NeuralNine Home Price Predictor: https://www.youtube.com/watch?v=Wqmtf9SA_kk&list=LL&index=1&t=643s
'''


# Importing the libraries
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
import openpyxl as py
from sklearn.model_selection import train_test_split
from tkinter import *
from tkinter import ttk
# Import the settings and the global variables needed

# This will create the datsheet for the machine. It will then read and analyze the excel file.
# Then it will then show the data on a datasheet
# Analyze the pdf file which tells the info of houses and the different prices that they have

homesdata = pd.read_excel("HomeData.xlsx")
print(homesdata.head(16))
'''
Train the model with the data given 
These will set the variables of what part of the data set I need.
'Price' is in its own category since that is what the output would be.
Also set up the training and testing variables as well as telling how much of my data will be used for testing
'''
x = homesdata.drop(['Price'], axis = 1)
y = homesdata['Price']
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2) 
train_data = X_train.join(Y_train)
train_data.hist(figsize = (15, 8))
plt.figure(figsiz=(15, 8))
sns.heatmap(train_data.cor(), annot = True, cmap="YlGnBu")
# Will draw the window using tkinter of the charts of data
win = Tk()
win.geometry("750x500")
frame = LabelFrame(win, width= 400, height= 180, bd=5)
entry = ttk.Entry(frame, width= 40)
def chart():
   message= "Your Charts "+ train_data.plt(figsize = (15, 8))
   label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
   label.pack(pady=30)
   entry.delete(0, 'end')
# The code for the user to input what kind of house they are looking for


# Will then take in the inputs for the user


# Then will print out the outcome by predicting how much the user's house would be
win.mainloop()