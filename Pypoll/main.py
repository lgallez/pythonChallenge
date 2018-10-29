# Import Modules
import os
import csv

# Write Paths
inputFile = os.path.join('..', '..', 'gitlab-data-analytics', '02-Homework', '03-Python', 'Instructions','PyPoll','Resources', 'election_data.csv')
outputFile = os.path.join("election_analysis.txt")

# Set Variables
totalVotes = 0
canOpt = [] 
canVotes = {}
winCan = ""
winCount = 0

# Read csv
with open(inputFile) as electionData:
    reader = csv.reader(electionData)

# Read Header
    header = next(reader)

# Start Interation
    for row in reader:
        
        totalVotes = totalVotes + 1
        
        canName = row[2]
        
        if canName not in canOpt:
            canOpt.append(canName)
            canVotes[canName] = 0
            
        canVotes[canName] = canVotes[canName] + 1
        
# Print Results
with open(outputFile, "w") as txtFile2:
    
    electionResults = (
        f"\n\nResults\n"
        f"------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"------------------\n")
    print(electionResults, end="")
    
# Save to Txt File
    txtFile2.write(electionResults)
    
# Determine Winner
    for candidate in canVotes:
        
        votes = canVotes.get(candidate)
        votePercent = float(votes) / float(totalVotes) *100
        
        if (votes > winCount):
            winCount = votes
            winCan = candidate
            
# Print Vote Count
        voteOutput = f"{candidate}: {votePercent:.3f}% ({votes})\n"
        print(voteOutput, end = "")
        
# Save to Txt File
        txtFile2.write(voteOutput)
    
# Print Candidate
        winCanSum = (
            f"------------------\n"
            f"Winner: {winCan}\n"
            f"------------------\n")
        print(winCanSum)
        
# Save to Txt File
        txtFile2.write(winCanSum)
        
        
        
        
        
        