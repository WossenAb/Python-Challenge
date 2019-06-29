#import env and add ins

import os
import csv
import pandas as pd
import numpy

#Saving the data

csv_path = ("election_data.csv")

#Reading the data with Pandas

Election_pd = pd.read_csv(csv_path)

#Creating a list of unique candidate names column

Candidate_Names = Election_pd["Candidate"].unique()

#Identifying total unique votes in each Candidate's Column.

Vote_Total = Election_pd["Candidate"].value_counts()

#Counting total number of votes 

Total_Votes = Election_pd["Candidate"].count()

#Counting the votes each candidate collected

#Counting candidate Kahn's Votes

KahnVote = Vote_Total[0]

KahnPerc = ("{0:.3%}".format(KahnVote/Total_Votes))

#Counting candidate Correy's Votes

CorreyVote = Vote_Total[1]

CorreyPerc = ("{0:.3%}".format(CorreyVote/Total_Votes))

#Counting candidate Li's Votes

LiVote = Vote_Total[2]

LiPerc = ("{0:.3%}".format(LiVote/Total_Votes))

#Counting candate O'Tooley' Votes

OTooleyVote = Vote_Total[3]

OTooleyPerc = ("{0:.3%}".format(OTooleyVote/Total_Votes))

#Printing results

print("Election Results")                            #Election results

print("-"*25)                                        #dashed line

print(f"Total Votes:  {Total_Votes}")                #Print total number of votes

print("-"*25)                                        #dashed line

print(f"Kahn: {KahnPerc} ({KahnVote})")              # print Kahn

print(f"Correy: {CorreyPerc} ({CorreyVote})")        # print Correy

print(f"Li: {LiPerc}  ({LiVote})")                   #print li

print(f"O'Tooley: {OTooleyPerc} ({OTooleyVote})")    #print O'Tooley

print("-"*25)                                        #dashed line

print("Winner: Kahn")                                   #print the winner is

print("-"*25)                                           #dashed line

#Documenting results in a new text file

#"\n" used to incert a new line after each result

text_file = open("PollPy_Results.txt", "w")

with open("PollPy_Results.txt", "w") as text_file:

    print("Election Results"+ "\n"  +                           

    ("-"*25) + "\n" +                                         

    (f"Total Votes:  {Total_Votes}") + "\n" +                 

    ("-"*25)  + "\n"  +                                          

    (f"Kahn: {KahnPerc} ({KahnVote})")    + "\n"  +             

    (f"Correy: {CorreyPerc} ({CorreyVote})")  + "\n"  +         

    (f"Li: {LiPerc}  ({LiVote})")   + "\n"  +                   

    (f"O'Tooley: {OTooleyPerc} ({OTooleyVote})")  + "\n"  +      

    ("-"*25)   + "\n"  +                                        

    (f"Winner: {Candidate_Names[0]}")  + "\n"  +                                

    ("-"*25),  file=text_file)

    

text_file.close()


