# Zack K
# Sources:
# Tkinter simpledialog to collect user input in integer or string: https://www.youtube.com/watch?v=Tbdg3J_YbII
# Course Code Files: Day 30 Exercise (Used as a template ot setup tkinter window)
# Switch Multiple Pages in Tkinter: https://www.youtube.com/watch?v=wFyzmZVKPAw
# Adding separate sample dataset: https://www.youtube.com/watch?v=Ooo3q7MuKMA&t=932s

'''
This code will tell you what the projected price of a home would be based of the 
user's input of the the home
'''
'''
Pandas is a library which reads and analyzes excel spreadsheets
openpyxl will open the excel file which can be displayed on the window.
simplediaglog is able to process the user input through a small tkinter window and can take in integers, 
floats, and strings. It also has a built-in error detection when the user doesn't give the right datatype.
'''
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import filedialog, messagebox


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
page1 = Frame(frame, width = 1000)
page1.pack(pady=20)
page2 = Frame(frame1)
page2.pack(pady=20)
datalabel = Label(page1, text = homesdata.loc[0:4])
# The lables used to tell what kind of page the user is in
page1label = Label(page1, text = "Welcome to Home Price Predictors! Would You like to see some sample data?") 
page1label.pack()
page2label = Label(page2, text = "Please enter the characteristics on the given separate windnow. Then, click estmiate!")
#tableentry = Label(page1, text = homesdata.loc[0:4])

# Groups all the pages together into a tuple and also sets up a page count to keep track of what page the user is on.
pages = [page1, page2]
count = 0
def nextclick():
   global count
# Will check to make sure the user isn't already on page 2 yet.
   if not count > len(pages):
# Changes what was on page 1 into what is on page 2
      for p in pages:
         p.pack_forget()
# Adds when the user clicks on the next page.
      count += 1
      page = pages[count]
# Loads in the next page
      page.pack(pady = 20)
# Loads in the label
      page2label.pack()
# Adds the estimate button onto page 2
   estimatebutton.pack(pady=10)
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
# Will activate when the user clicks yes on page 1. It will create a separate window to show the sample.
def yesclick():
# Creates the separate window for the dataset
   win1 = Tk()
   win1.title("Dataset")
   win1.geometry("1000x400")
# Allows the variables to be used in to create the dataset in the window
   global homesdata
   global treeview
# Creates the treeview/dataset element.
   treeview = ttk.Treeview(win1)
   treeview.pack(pady = 30)
# It will see if the data file is downloaded or not to then use
   try:
      homesdata = pd.read_excel("HomeData.xlsx")
   except Exception as e:
      messagebox.showerror("File Not there... Please Download the dataset", {e})
# Makes sure that there is nothing else in the dataset.
   treeview.delete(*treeview.get_children())
   # This will create the contents of the dataset.
   treeview['column'] = list(homesdata.columns)
   treeview['show'] = 'headings'
   for col in treeview['column']:
      treeview.heading(col, text = col)
   homesdata_rows = homesdata.to_numpy().tolist()
   for row in homesdata_rows:
      treeview.insert("", "end", values = row)
  

# Creates the buttons for all the pages.
yesbutton = Button(page1, text = "Yes!", command = yesclick)
backbutton = Button(win, text = "Back", command = backclick)
nextbutton = Button(win, text = "Next", command = nextclick)
# Generates the buttons onto the tkinter window.
backbutton.pack()
nextbutton.pack()
yesbutton.pack()
# Creates the separate windows which can accept the integer and String values from the user.

Bed = simpledialog.askinteger(page2, "Bedroom #:")
Bath = simpledialog.askinteger(page2, "Bathroom #:")
Condition = simpledialog.askinteger(page2, "Condition out of 10: ")
Year = simpledialog.askinteger(page2, "Year Built:" )
Size = simpledialog.askinteger(page2, "Size")
Pool = simpledialog.askstring(page2, "Pool?")

# Activates when the function when the user clicks "estimate!" on page 2.
def estimation():
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
   elif Condition > 2 and Condition < 6:
      POINTS += 2
   elif Condition > 5 and Condition < 10:
      POINTS += 3
   elif Condition > 10:
      POINTS += 4
# Will ask for how many bathrooms there are and will use the input to assign how many qualtiy points their home gets.
   if Bath == 0:
      POINTS += 0
   elif Bath == 1:
      POINTS += 1
   elif Bath > 1 and Bath < 5:
      POINTS += 2
   elif Bath > 4 and Bath < 8:
      POINTS += 3
   elif Bath > 6 and Bath < 10:
      POINTS += 4
   elif Bath > 9 and Bath < 14:
      POINTS += 5
   elif Bath > 13:
      POINTS += 6
# Processes the the user input of how many bedrooms and gives the neccessary points. 
   if Bed == 0:
      POINTS += 0
   elif Bed > 0 and Bed < 3:
      POINTS += 1
   elif Bed > 2 and Bed < 5:
      POINTS += 2
   elif Bed > 4 and Bed < 8:
      POINTS += 3
   elif Bed > 7 and Bed < 10:
      POINTS += 4
   elif Bed > 9 and Bed < 14:
      POINTS += 5
   elif Bed > 13:
      POINTS += 6
# Takes input from the entry which it gives points to the house based on how old the home is.
   if Year < 1950:
      POINTS += 0
   elif Year > 1949 and Year < 1965:
      POINTS += 1
   elif Year > 1954 and Year < 1980:
      POINTS += 2
   elif Year > 1979 and Year < 1995:
      POINTS += 3
   elif Year > 1994 and Year < 2005:
      POINTS += 4
   elif Year > 2004 and Year < 2015:
      POINTS +=5
   elif Year > 2014:
      POINTS += 6
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
   elif Size > 3999 and Size < 4500: 
      POINTS += 6
   elif Size > 4499 and Size < 5000:
      POINTS += 7
   elif Size > 4999:
      POINTS += 8
# Will use the amount of Quality Points to then estimate how long much the hoem will cost.
   if POINTS == 0:
      PRICE += 0
   elif POINTS > 0 and POINTS < 4:
      PRICE += 250000
   elif POINTS > 3 and POINTS < 7:
      PRICE += 400000
   elif POINTS > 6 and POINTS < 10:
      PRICE += 550000
   elif POINTS > 9 and POINTS < 13:
      PRICE += 700000
   elif POINTS > 12 and POINTS < 16:
      PRICE += 825000
   elif POINTS > 15 and POINTS < 19:
      PRICE += 900000
   elif POINTS > 18 and POINTS < 22:
      PRICE += 1050000
   elif POINTS > 21 and POINTS < 25:
      PRICE += 1175000
   elif POINTS > 24 and POINTS < 28:
      PRICE += 1500000
   elif POINTS > 27:
      PRICE += 1750000
# Tells the quality score of the home by adding the points together.
   Points = ("Your Home Quality Score is: " + str(POINTS) + " Points!")
# Tells the price of the home after the user clicks estimate.
   Price = ("Your Home Price is:" + str(PRICE) + " dollars!")
# The labels that are apart of the Points and Price value.
   label2 = Label(page2, text = Points, font = ('Times New Roman', 14, 'italic'))
   label3= Label(page2, text= Price, font= ('Times New Roman', 14, 'italic'))
# Creates the labels text.
   label2.pack(pady = 10)
   label3.pack(pady = 10)
# Creates the button used on page 2 for submitting the inputs.
estimatebutton = ttk.Button(page2, text= "Estimate!", command = estimation)
win.mainloop()


