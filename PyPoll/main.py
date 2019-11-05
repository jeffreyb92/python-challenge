# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

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

#importing the necessary modules
import os
import csv

#creating a variable that stores the path to the datafile for ease of use
polls = os.path.join("Resources","election_data.csv")

#defining variables needed
totalvotes = 0
candidates = dict()
mostvotes = 0
winner = ""


#setting a function that will automatically print out the stats once the for loop is done
def pollstats():
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {str(totalvotes)}")
    print("-------------------------")
    for key, value in candidates.items():
        print(f"{key}: {round(value[0],3)}00% ({value[1]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")


#opening the file using previously set variable for path
with open(polls, 'r') as csvfile:
    
    #telling the csvreader that the delimiter for that file is a comma
    csvreader = csv.reader(csvfile,delimiter=",")
 
    #skipping the header line since we don't really need it here
    next(csvreader)
    
    #for loop to run through operations for each row in the csv
    for row in csvreader:
        #incrementing the number of total votes per row
        totalvotes+= 1
        #setting a default to 1 so that way later on we just increment on that without interrupting the data
        candidatevotes = 1

        #checking if the candidate is in the dictionary. If it's not then we add them
        if row[2] not in candidates:
            #the first value is being set to zero for the candidate percentage until we get more data
            candidates[row[2]] = [0, candidatevotes]
        #if they are in the dictionary then we update their info
        else:
            #updating the candidate vote first before the percentage so it is accurate
            candidates[row[2]][1] += 1
            candidates[row[2]][0] = (candidates[row[2]][1]/totalvotes) * 100

#checking for who is the winner by going through the dictionary
for key, value in candidates.items():
    if int(value[1]) > mostvotes:
        mostvotes = value[1]
        winner = key


#calling our function to print out the stats to the terminal
pollstats()

# print(candidates) was being used to check the dictionary before output

#setting the output file path
output_file = os.path.join("output.txt")

#making the output file and setting it to write mode to write data
with open(output_file, "w", newline="") as datafile:

    #writing the data to the new file we just created
    datafile.write("Election Results \n")
    datafile.write("--------------------------\n")
    datafile.write(f"Total Votes: {str(totalvotes)}\n")
    datafile.write("--------------------------\n")
    for key, value in candidates.items():
        datafile.write(f"{key}: {round(value[0],3)}00% ({value[1]})\n")
    datafile.write("--------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("--------------------------")