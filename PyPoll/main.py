# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')

# Total rows (not including the header is the total of votes)
Total_Votes = 0 

# empty dictionary to catch votes should be:
# votesPerCandidate = {
#   "candidate_one": votes as int
# }
TotalvotesPerCandidate = {}

# open up election_data
with open(election_data_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        Total_Votes += 1
        if row[2] not in TotalvotesPerCandidate:
            TotalvotesPerCandidate[row[2]] = 1
        else:
            TotalvotesPerCandidate[row[2]] += 1   
                
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_Votes))
print("-------------------------")

for candidate, Votes in TotalvotesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(Votes/Total_Votes) + "   (" +  str(Votes) + ")")
    
print("-------------------------") 

winner = max(TotalvotesPerCandidate, key=TotalvotesPerCandidate.get)

print(f"Winner: {winner}")

# now write this to an output file

f = open("Election_Results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(Total_Votes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, Votes in TotalvotesPerCandidate.items():
    f.write(candidate + ": " + "{:.3%}".format(Votes/Total_Votes) + "   (" +  str(Votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
f.write('-------------------------')
f.write('\n')


