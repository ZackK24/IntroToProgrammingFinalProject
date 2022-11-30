# Sources and Overview of the Project.
'''
This code will tell you what the projected price of a home in San Jose
will be based on what kind of house you would like to have.

Sources:
https://www.w3schools.com/python/python_ml_linear_regression.asp
https://colab.research.google.com/drive/1zk6NgYiR2UPzzmjzyhGbEduSt3gZHi7b
'''


# Importing the libraries
import pandas as pd
import matplotlib.pylot as plt
import seaborn as sns

# Import the settings and the global variables needed
# This will create the datsheet for the machine. It will then read and analyze the excel file.
# Then it will then show the data on a datasheet
homesdata = pd.read_csv("HousePricePrediction.xlsx")
print(homesdata.head(5))
# Analyze the pdf file which tells the info of houses and the different prices that they have


# The code for the user to input what kind of house they are looking for


# Will then take in the inputs for the user


# Then will print out the user by predicting how much the user's house would be
