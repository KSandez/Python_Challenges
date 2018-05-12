import os
import csv

txtfile = "election_data_2.csv"

#Variables to track
votes = 0
candidates = 0

#make lists via loop
candidate_list = []

#makes this list a dictionary as it loops thru it
candidate_votes = {}

with open(txtfile) as election_data:
    csvreader = csv.DictReader(election_data)

    for row in csvreader:
        #count number of voters then store count in variable
        votes = votes + 1
        #count the number of time the candidate name shows up then store count in variable
        candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_list:
            #add a new name to the candidate list plus...
            candidate_list.append(row["Candidate"])
            #put that candidate as a tally of value 1 into the candidate_votes dictionary using their name from the candidate_list as the key.
            candidate_votes[row["Candidate"]] = 1
                       
        else:
            #once the candidate is on the candidate_list, increase dictionary and increase them by 1
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
    print(candidate_list)
    print(candidate_votes)

    print()
    print(("=") * 30)
    print()
    print("Election Results")
    print(("-") * 30)
    print("Total Votes: " + "{:,}".format(votes))
    print(("-") * 30)

#Calculate the results of each candidate from the candidate_votes dictionary
    for candidate in candidate_votes:
        candidate_results = (candidate + ": " + str(round(((candidate_votes[candidate]/votes)*100),2)) + "%" + " (" + "{:,}".format(candidate_votes[candidate]) + ")") 
        print(candidate_results)

#Which candidate has the highest number of candidate votes  
print(("-") * 30)
print("Winner: " + str(candidate_list[0]))
print(("-") * 30)

#--------------------------------------------------------------
output_path = os.path.join("election_results_2.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write(("-") * 30)
    txt_file.write("\n")
    txt_file.write("Total Votes " + "{:,}".format(votes))
    txt_file.write("\n")
    txt_file.write(("-") * 30)
    txt_file.write("\n")
    for candidate in candidate_votes:
        candidate_results = (candidate + ": " + str(round(((candidate_votes[candidate]/votes)*100),2)) + "%" + " (" + "{:,}".format(candidate_votes[candidate]) + ")")
        txt_file.write('{}\n'.format(candidate_results))
    txt_file.write("\n")
    txt_file.write("Winner: " + str(candidate_list[0]))