# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

bank = os.path.join("Resources","budget_data.csv")

totalmonths = 0
totalamount = 0
#averagechange = totalamount/totalmonths
greatestincrease = 0
greatestdecrease = 0
previousamount = 0
firstamount = 0
lastamount = 0

def bankstats():
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {str(totalmonths)}")
    print(f"Total: ${str(totalamount)}")
    print(f"Average Change: ${str(round((lastamount - firstamount)/(totalmonths - 1),2))}")
    print(f"Greatest Increase in Profits: {dategreat} (${str(greatestincrease)})")
    print(f"Greatest Decrease in Profits: {dateleast} (${str(greatestdecrease)})")



with open(bank, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=",")
 

    next(csvreader)
    

    for row in csvreader:
        if csvreader.line_num == 2:
            firstamount = int(row[1])

        else:
            lastamount = int(row[1])
        
        totalmonths += 1
        totalamount += int(row[1])
        increase = int(row[1]) - previousamount
        previousamount = int(row[1])

        if increase > greatestincrease:
            greatestincrease = increase
            dategreat = row[0]
        if increase < greatestdecrease:
            greatestdecrease = increase
            dateleast = row[0]


bankstats()

output_file = os.path.join("output.txt")

with open(output_file, "w", newline="") as datafile:

    datafile.write("Financial Analysis \n")
    datafile.write("-------------------------\n")
    datafile.write(f"Total Months: {str(totalmonths)}\n")
    datafile.write(f"Total: ${str(totalamount)}\n")
    datafile.write(f"Average Change: ${str(round((lastamount - firstamount)/(totalmonths - 1),2))}\n")
    datafile.write(f"Greatest Increase in Profits: {dategreat} (${str(greatestincrease)})\n")
    datafile.write(f"Greatest Decrease in Profits: {dateleast} (${str(greatestdecrease)})\n")