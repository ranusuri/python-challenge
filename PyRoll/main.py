
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
# Modules
import os
import csv


# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

print(csvpath)

candidate_votes = dict()

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first  and skip  header row
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #variable to hold total votes
    total_votes = 0

    votes = 0

    candidate_list = []
    candidate = ""
    # Loop through 
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        #print("row :", row)
        if row[2] not in candidate_list:
            
            candidate_list.append(candidate)
            #add candidate name to dictionary
            candidate_votes[candidate] = 0
        #create candidate dictionary with votes
        #print(candidate)
        for x in candidate_list:       
            if(x == candidate): 
                votes = candidate_votes.get(candidate)
                #print("votes :", votes)
                votes = votes + 1
                candidate_votes[candidate] = votes

#create dictionary with dictionary
election_results = {} 

        
#print("Directory values : ")
#print(candidate_votes)

# Set variable for output file
output_file = os.path.join(".", "analysis","election_results.txt")

#  Open the output file
with open(output_file, "w") as analysis:

    print("Election Results")
    print("-----------------------------")
    print("Total votes : ", total_votes)
    print("-----------------------------")

    analysis.write("Election Results\n")
    analysis.write("-----------------------------------\n")
    analysis.write(f"Total votes :  {total_votes}\n")
    analysis.write("-----------------------------------\n")

    votes = 0
    max_votes = 0
    per_votes_format = ""
    winner = ""
    for x in candidate_votes.keys():
        votes = int(candidate_votes[x])
        per_votes = (votes/total_votes) 
        per_votes_format = "{:.3%}".format(per_votes)
        print(f" {x} : {per_votes_format}  ({votes})" )
        analysis.write(f" {x} : {per_votes_format}  ({votes})\n" )
        if (max_votes < votes):
            max_votes = votes;
            winner = x

    print("----------------------------")
    print(f" Winner : {winner}" )
    print("----------------------------")

    analysis.write("----------------------------\n")
    analysis.write(f" Winner : {winner}\n" )
    analysis.write("----------------------------\n")


    



