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

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# set variables Total_Months, Total, Average_Change, Budget_Data
# Month_Year_Increase, Month_Year_Decrease, Greatest_Increase_Profits, Greatest_Decrease_Profits
# Date, P_and_L
Total_Months = 0
Total = 0
Average_Change = 0
Greatest_Increase_Profits = 0
Greatest_Decrease_Profits = 0
Budget_Data=[]
Date=[]
P_and_L=[]
Sum=0
count=0

#initialize initial change in list to 0.  first delta in second month
Changes=[0]


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        #The total number of months included in the dataset
        Total_Months+= 1

        #The net total amount of "Profit/Losses" over the entire period
        Total = Total + int(row[1])

        #get dates
        Date.append(row[0])

        #get P/L
        P_and_L.append(int(row[1]))

#calculate month to month changes
for index in range(len(P_and_L)-1):
    Changes.append(P_and_L[index+1]-P_and_L[index])

#zip lists together
cleaned_csv = zip(Date, P_and_L,Changes)

for value in cleaned_csv:

    #sum all month-to-month changes
    Sum = Sum + value[2]
    
    #The greatest increase in profits (date and amount) over the entire period
    if  value[2] > Greatest_Increase_Profits:
        Greatest_Increase_Profits = value[2]
        Month_Year_Increase = value[0]
      
    #The greatest decrease in losses (date and amount) over the entire period
    if  value[2] < Greatest_Decrease_Profits:
        Greatest_Decrease_Profits = value[2]
        Month_Year_Decrease = value[0]

    count=count+1

#calculate average P/L changes over the entire period
Average_Change = Sum / (count-1)

print('\n')

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {Total_Months}')
print(f'Total: ${Total}')
print(f'Average Change: ${Average_Change:.6}')
print(f'Greatest increase in Profits: {Month_Year_Increase} (${Greatest_Increase_Profits})' )
print(f'Greatest decrease in Profits: {Month_Year_Decrease} (${(Greatest_Decrease_Profits)})' )

# set output file
#output_file = open("../analysis/pybank.txt","w")
output_path = os.path.join("..","analysis","pybank.txt")

with open(output_path,'w') as output_file: 

    output_file.write('Financial Analysis\n')
    output_file.write('----------------------------\n')
    output_file.write(f'Total Months: {Total_Months}\n')
    output_file.write(f'Total: ${Total}\n')
    output_file.write(f'Average Change: ${Average_Change:.6}\n')
    output_file.write(f'Greatest increase in Profits: {Month_Year_Increase} (${Greatest_Increase_Profits})\n' )
    output_file.write(f'Greatest decrease in Profits: {Month_Year_Decrease} (${(Greatest_Decrease_Profits)})\n' )

    output_file.close()