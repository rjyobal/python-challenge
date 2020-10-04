#Import libraries
import os
import csv

#File path
budget_csv = os.path.join("Resources", "election_data.csv")

#Set variables
candidates=[]
summ_candidates=[]
candidates_report=[]
count_candidate_vote=0
total=0
maxvalue=0

candidate_name=[]
candidate_votes=[]

#Open file - readonly
with open(budget_csv,'r',encoding='UTF-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #Skip the header
    csv_header = next(csv_reader)
    csv_reader=list(csv_reader)
    #Fill out list
    for row in csv_reader:
        candidates.append(row[2])
        
    #Dedup candidate list
    for dedup in candidates:
        if dedup not in summ_candidates:
            summ_candidates.append(dedup)

    #Create summary results
    for candidate in summ_candidates:
        count_candidate_vote=0
        #print(f'Candidate: {candidate}')
        for row2 in csv_reader:
            if candidate == row2[2]:
                count_candidate_vote += 1
        percentage = round(count_candidate_vote/len(candidates)*100,2)
        candidate_record=f'{candidate}: {percentage:.3f}%, ({count_candidate_vote})'
        candidates_report.append(candidate_record)
        #Create list to get winner name
        candidate_name.append(candidate)
        candidate_votes.append(count_candidate_vote)

#Get max votes and winner name
sum_table=zip(candidate_name,candidate_votes)
for win in sum_table:
    if int(win[1]) > maxvalue:
        maxvalue=int(win[1])
        winner=win[0]

#Print vars
print_header=(f"""
Election Results
-------------------------
Total Votes: {len(candidates)}
-------------------------
""")
print_bottom=(f"""
-------------------------
Winner: {winner}
-------------------------
""")

#Print in terminal
print(print_header)
for z in candidates_report:
    print(z)
print(print_bottom)

#Create final report in txt file
output_file = os.path.join("analysis", "final_report.txt")
with open(output_file,'w') as file:
    file.write(print_header)
    for z in candidates_report:
        file.write(z)
        file.write('\n')
    file.write(print_bottom)