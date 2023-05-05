#Import dependencies
import os
import csv


#Make pathway
election_csv = os.path.join("Resources1", "election_data.csv")

# Lists to store data
totalVotes = 0
candidateOptions = []
candidateVotes = {}
winningCount = 0
winningCandidate = []
candidateName = []

#With open reader
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    next(csvreader)
    
    
    #Add total amount of votes
    totalVotes = len(list(csvreader))
    
    #Loop through candidates
    for row in csvreader :
    #Extract candidate name from each row
        candidateName = row[2]
   
    #if candidate does not match existing candidate
   # if candidateName not in candidateOptions :
    
        #add it to the list of candidates in the running
        #candidateOptions.append(candidateName)
        #and begin tracking candidate's voter count
        #candidateVotes[candidateName] = 0
        
    #Then add vote to that candidate's count
    #candidateVotes[candidateName] = candidateVotes[candidateName] + 1
    
    #Add titles
    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(totalVotes))
    print("-----------------------")
    print("Candidate #1")
    print("Candidate #2")
    print("Candidate #3")
    print("-----------------------")
    print("Winner: ")
    
#for candidate in candidateVotes :
    #votes = candidateVotes.get(candidate)
    #votePercentage = float(votes)/float(totalVotes) *100

    #if (votes > winningCount) :
        #winningCount = votes
        #winningCandidate = candidate

#Zip lists together
#Not iterable?
#cleaned_csv = zip(totalVotes)

output_file = os.path.join("Analysis","election_datafinal.csv")

#open output file
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    
    #write the header row
    writer.writerow(["Total Votes", "Candidate #1", "Candidate #2", "Candidate #3", "Winner"])

    #write in zipped rows
    #writer.writerows(cleaned_csv)

