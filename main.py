# Zack K
# Sources:
# How to Validate an Entry Widget as an Integer: https://www.youtube.com/watch?v=IbpInH4q4Sg&list=LL&index=1&t=390s
# Course Code Files: Day 30 Exercise
# Switch Multiple Pages in Tkinter: https://www.youtube.com/watch?v=wFyzmZVKPAw

'''
This code will tell you what the projected price of a home would be based of the 
user's input of the the home
'''
# Pandas is a library which reads and analyzes excel spreadsheets
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import Entry
# Analyze the pdf file which has the info of houses and gives a sample of the homes.
homesdata = pd.read_excel("HomeData.xlsx")
print(homesdata.head())

# Draws the Tkinter window
win = Tk()
win.title("Home Price Predictor")
win.geometry("1000x500")
PRICE = int()
POINTS = int
# Creating the settings for points and price used througout the processing of input.
Price = PRICE
Price = int(0)
Points = POINTS
Points = int(0)
# Creates the outline and frames of the tkinter windows. 
frame = Frame(win)
frame1 = Frame(win)
frame.pack()
frame1.pack()
# Creates the pages of the program.
page1 = Frame(frame)
page1.pack(pady=20)
page2 = Frame(frame1)
page2.pack(pady=20)
# The lables used to tell what kind of page the user is in
page1label = Label(page1, text = "Welcome to Home Price Predictors! Would You like to see some sample data?") 
page1label.pack()
page2label = Label(page2, text = "Enter your home's characteristics:")
tableentry = Label(page1, text = homesdata.head(5))
# Groups all the pages together into a tuple and also sets up a page count to keep track of what page the user is on.
pages = [page1, page2]
count = 0
def nextclick():

   global count

   if not count > len(pages):
   
      for p in pages:
         p.pack_forget()
# Adds when the user clicks on the next page.
      count += 1
      page = pages[count]
# Loads in the next page
      page.pack(pady = 20)
# Once the user clicks next, completely new entries and labels replace page 1.
# Also adds the entires and texts in page 2.
   page2label.pack()
   Bath.pack()
   Bed.pack()
   Condition.pack()
   Pool.pack()
   Year.pack()
   Size.pack()
# Adds the estimate button to give the results in page 2.
   estimatebutton.pack(pady=10)
   Bath.insert(INSERT, "Bathroom # ")
   Bed.insert(INSERT, "Bedroom # ")
   Condition.insert(INSERT, "Condition (out of 10): ")
   Pool.insert(INSERT, "Pool? ")
   Year.insert(INSERT, "When was it built? ")
   Size.insert(INSERT, "What is the size of your home? ")
# When the user clicks back:
def backclick():
   global count
# Checks to make sure the user isn't already on page 1.
   if not count == 0:
   
      for p in pages:
# Then, it will go down a page and load in page 1.
         p.pack_forget()
      count -= 1
      page = pages[count]
      page.pack(pady = 20)
# Will activate when the user clicks yes on page 1.
def yesclick():
# Once they click yes, they then see the sample data of homesdata.
   tableentry.pack()

# Creates the buttons for all the pages.
yesbutton = Button(page1, text = "Yes!", command = yesclick)
backbutton = Button(win, text = "Back", command = backclick)
nextbutton = Button(win, text = "Next", command = nextclick)
# Generates the buttons onto the tkinter window.
backbutton.pack()
nextbutton.pack()
yesbutton.pack()
# Creates the entry boxes for each category.
Bath = Entry(page2, width= 40)
Bed = Entry(page2, width = 40)
Condition = Entry(page2, width = 40)
Pool = Entry(page2, width = 40)
Year = Entry(page2, width = 40)
Size = Entry(page2, width = 40)


# Activates when the function when the user clicks "estimate!" on page 2.
def estimation():
# Converts the entries into integers
   try:
      int(Bath.get())
      int(Bed.get())
      int(Condition.get())
      int(Year.get())
      int(Size.get())
   except ValueError:
      print("Invalid answer...")
   PRICE = int()
   POINTS = int()
# Checks the value placed into the pool entry and adds the corresponding points.
   if Pool == "Yes" or Pool == "yes":
      POINTS += 2
   else:
      POINTS +=0
# Checks the condition value and assigns points to how well conditioned the house is.
   if Condition < 3:
      POINTS += 1
   elif Condition > 4 and Condition < 7:
      POINTS += 2
   elif Condition > 7:
      POINTS += 3
# Will ask for how many bathrooms there are and will use the input to assign how many qualtiy points their home gets.
   if Bath == 0:
      POINTS += 0
   elif Bath == 1:
      POINTS += 1
   elif Bath > 1 and Bath < 5:
      POINTS += 2
   elif Bath > 4:
      POINTS += 3
# Processes the the user input of how many bedrooms and gives the neccessary points. 
   if Bed == 0:
      POINTS += 0
   elif Bed > 0 and Bed < 3:
      POINTS += 1
   elif Bed > 2 and Bed < 6:
      POINTS += 2
   elif Bed > 5:
      POINTS += 3
# Takes input from the entry which it gives points to the house based on how old the home is.
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
# User inputs the size of the home and points are added based off user input.
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
# Tells the quality score of the home by adding the points together.
   Points = ("Your Home Quality Score is: " + str(POINTS) + " Points!")
# Tells the price of the home after the user clicks estimate.
   Price = ("Your Home Price is:" + str(PRICE) + " dollars!")
# The labels that are apart of the Points and Price value.
   label2 = Label(frame, text = Points, font = ('Times New Roman', 14, 'italic'))
   label3= Label(frame, text= Price, font= ('Times New Roman', 14, 'italic'))
# Creates the labels text.
   label2.pack(pady = 30)
   label3.pack(pady = 30)
# Creates the button used on page 2 for submitting the inputs.
estimatebutton = ttk.Button(page2, text= "Estimate!", command = estimation)
win.mainloop()


