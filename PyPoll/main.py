#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following

#The total number of votes cast
#A complete list of candidates who received votes

#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Python Challenge - PyBank
#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# set variables Total_Votes, Candidates
Total_Votes = 0
Candidates = []
Percentages = [0,0,0,0]
Candidate_Votes = [0,0,0,0]


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
                
        #The total number of months included in the dataset
        Total_Votes+= 1

        #Determine who are the candidates
        if row[2] not in Candidates:
            Candidates.append(row[2])

    #reset the csvfile back to top    
    csvfile.seek(0)
    next(csvreader)

    #count the votes for each candidate
    for row in csvreader:
        if row[2] == Candidates[0]:
            Candidate_Votes[0]+=1
        elif row[2] == Candidates[1]:
            Candidate_Votes[1]+=1
        elif row[2] == Candidates[2]:
            Candidate_Votes[2]+=1
        else:
            row[2] == Candidates[3]
            Candidate_Votes[3]+=1

#calculate percentages per candidate
for x in range(4):
    Percentages[x] = Candidate_Votes[x]/Total_Votes * 100

#calculate winner based on popular vote
Winner_Votes = max(Candidate_Votes)
index = Candidate_Votes.index(Winner_Votes)
Winner = Candidates[index]

print(Candidates)

print('Election Results')
print('----------------------------')
print(f'Total Votes: {Total_Votes}')
print('----------------------------')

for x in range(4):
    print(f'{Candidates[x]}: {Percentages[x]:.6}%  {Candidate_Votes[x]}')

print('----------------------------')
print(f'Winner: {Winner}')
print('----------------------------')

# set output file
#output_file = open("..\analysis\pypoll.txt","w")
output_path = os.path.join("..","analysis","pypoll.txt")

with open(output_path,'w') as output_file: 

    output_file.write('Election Results\n')
    output_file.write('----------------------------\n')
    output_file.write(f'Total Votes: {Total_Votes}\n')
    output_file.write('----------------------------\n')

    for x in range(4):
        output_file.write(f'{Candidates[x]}: {Percentages[x]:.6}%  {Candidate_Votes[x]}\n')

    output_file.write('----------------------------\n')
    output_file.write(f'Winner: {Winner}\n')
    output_file.write('----------------------------\n')

    output_file.close()