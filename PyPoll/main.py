# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
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

def pollstats():
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