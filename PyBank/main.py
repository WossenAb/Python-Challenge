# Importing libraries 
import csv
import os

import numpy as np
import pandas as pd

# importing csv file
csv_path = ("budget_data.csv") 
bank_pd = pd.read_csv(csv_path, parse_dates=True)
print("test")
months = bank_pd["Date"].count()
print(months)

#Total amount of money captured converted into currency
aggregatefunds = '${:.0f}'.format(bank_pd["Profit/Losses"].sum())
print(aggregatefunds)

#determining increase/decrease from one month to the next

amountchange = bank_pd["Profit/Losses"].diff()
bank_pd["amount Changed"] = amountchange 

# testing if argument works
print(bank_pd.head(4))

# locating the biggest positive change in funds

#this line finds and formats the highest dollar amount
biggestpositivechange = '${:.0f}'.format(bank_pd["amount changed"].max())

#this line finds the date in the row with the biggest dollar amount
Gi_Date = (bank_pd.loc[bank_pd['amount Changed'].idxmax(), 'Date'])


# locating the biggest negative change in funds

#This line finds and formats the lowest dollar amount
biggestnegativechange = '${:.0f}'.format(bank_pd["amount changed"].min())

#This line finds the date in the rows with the minimum dollar amount
Gd_Date = (bank_pd.loc[bank_pd['amount Changed'].idxmin(), 'Date'])

average = '${:.2f}'.format(bank_pd['amount Changed'].mean())

# Printing 

print("financial analysis")
print("_"*25)
print(f"total months: {months}")
print(f"total: {aggregatefunds}")
print(f"average change: {average}")
print(f"largest increase in profits: {Gi_Date} ({biggestpositivechange}")
print(f"greatest decrease in profits: {Gd_Date} ({biggestnegativechange})")

#Saving File in a text format
text_file = open("PyBank_Results.txt",  "w")

with open("PyBank_Results.text", "w") as text_file:
    print("Financial Analysis" + '\n' +
    ("-"*25) + '\n' +
    (f"Total Months: {months}") + '\n' +
    (f"Total: {aggregatefunds}") + '\n' +
    (f"average Change:  {average}") + '\n' +
    (f"Greatest Increase in Profits: {Gi_Date}  ({biggestpositivechange})") + '\n' +
    (f"Greatest Decrease in Profits: {Gd_Date} ({biggestnegativechange})"),
     file=text_file)

text_file.close()   

