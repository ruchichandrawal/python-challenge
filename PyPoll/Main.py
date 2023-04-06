# importing libraries
import os
import csv

# print header
print("Election Results \n____________________________\n")

# defining variables
total_votes = 0
candidates_list = []
per_candidates_votes = []

csvpath = os.path.join("Resources","election_data.csv")

# open CSV file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # read header row
    csvHeader = next(csvreader)

    # loop through remaining rows
    for row in csvreader:
        total_votes+=1
        if(candidates_list.count(row[2])>0):
            position=candidates_list.index(row[2])
            per_candidates_votes[position]+=1
        else:
            candidates_list.append(row[2])
            per_candidates_votes.append(1)

print(f"Total Votes: {total_votes}")
print("_________________________\n")

# calculate values
index=0
for name in candidates_list:
    votes = per_candidates_votes[index]
    percentage = round(votes*100/total_votes,3)
    print(f"{name}: {percentage}% ({votes})")
    index+=1

print("_________________________\n")

# finding final winner
max_votes = max(per_candidates_votes)
index = per_candidates_votes.index(max_votes)
winner = candidates_list[index]
print(f"Winner: {winner}")

print("_________________________\n")

# print to output file
txtPath = os.path.join("Analysis","Output.txt")
with open(txtPath,"w") as output_file:
    output_file.write("Election Results \n____________________________\n\n")
    output_file.write(f"Totalvotes: {total_votes}")        
    output_file.write("\n_________________________\n\n")            
    index=0
    for name in candidates_list:
        votes = per_candidates_votes[index]
        percentage = round(votes*100/total_votes,3)
        output_file.write(f"{name}: {percentage}% ({votes})\n")
        index+=1
    output_file.write("_________________________\n")
    output_file.write(f"\nWinner: {winner}")
    output_file.write("\n_________________________\n")

    