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

#importing the necessary modules
import os
import csv

#creating a variable that stores the path to the datafile for ease of use
bank = os.path.join("Resources","budget_data.csv")

#defining variables needed
totalmonths = 0
totalamount = 0
greatestincrease = 0
greatestdecrease = 0
previousamount = 0
firstamount = 0
lastamount = 0

#setting a function that will automatically print out the stats once the for loop is done
def bankstats():
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {str(totalmonths)}")
    print(f"Total: ${str(totalamount)}")
    print(f"Average Change: ${str(round((lastamount - firstamount)/(totalmonths - 1),2))}")
    print(f"Greatest Increase in Profits: {dategreat} (${str(greatestincrease)})")
    print(f"Greatest Decrease in Profits: {dateleast} (${str(greatestdecrease)})")


#opening the file using previously set variable for path
with open(bank, 'r') as csvfile:
    
    #telling the csvreader that the delimiter for that file is a comma
    csvreader = csv.reader(csvfile,delimiter=",")
 
    #keeping the header line, but not doing anything with it since we don't really need it here
    header = next(csvreader)

    #for loop to run through operations for each row in the csv
    for row in csvreader:
        #checking if the row is equal to the first row of data and then storing that
        if csvreader.line_num == 2:
            firstamount = int(row[1])
        #if not then we are storing it as the last row until we hit the last row to get final value we need
        else:
            lastamount = int(row[1])
        #incremementing the number of months for each row
        totalmonths += 1
        #adding the amount from each row together with the previous
        totalamount += int(row[1])
        #checking how much an increase happened between this row and the previous row
        increase = int(row[1]) - previousamount
        #storing this row as previousamount for next row
        previousamount = int(row[1])

        #if the increase is bigger than the greatest increase we have to date, we update that variable with this one
        if increase > greatestincrease:
            greatestincrease = increase
            dategreat = row[0]
        #if the increase is smaller than the smallest increase we have to date, we update that variable with this one
        elif increase < greatestdecrease:
            greatestdecrease = increase
            dateleast = row[0]

#calling our function to print out the stats to the terminal
bankstats()

#setting the output file path
output_file = os.path.join("output.txt")

#making the output file and setting it to write mode to write data
with open(output_file, "w", newline="") as datafile:

    #writing the data to the new file we just created
    datafile.write("Financial Analysis \n")
    datafile.write("-------------------------\n")
    datafile.write(f"Total Months: {str(totalmonths)}\n")
    datafile.write(f"Total: ${str(totalamount)}\n")
    datafile.write(f"Average Change: ${str(round((lastamount - firstamount)/(totalmonths - 1),2))}\n")
    datafile.write(f"Greatest Increase in Profits: {dategreat} (${str(greatestincrease)})\n")
    datafile.write(f"Greatest Decrease in Profits: {dateleast} (${str(greatestdecrease)})\n")