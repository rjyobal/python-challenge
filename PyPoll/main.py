#Import libraries
import os
import csv

#File path
budget_csv = os.path.join("Resources", "election_data.csv")
#budget_csv = 'Resources/budget_data.csv'

#Set variables
candidates=[]
summ_candidates=[]
candidates_report=[]
count_candidate_vote=0
output_row=[]
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
        #output_row.append(row)
        candidates.append(row[2])
        
    #Dedup candidate list
    for x in candidates:
        if x not in summ_candidates:
            summ_candidates.append(x)
    
    for candidate in summ_candidates:
        count_candidate_vote=0
        #print(f'Candidate: {candidate}')
        for row2 in csv_reader:
            if candidate == row2[2]:
                count_candidate_vote = count_candidate_vote + 1
        percentage = round(count_candidate_vote/len(candidates)*100,2)
        candidate_record=f'{candidate}: {round(percentage,2)}%, ({count_candidate_vote})'
        candidates_report.append(candidate_record)
        candidate_name.append(candidate)
        candidate_votes.append(count_candidate_vote)

#Get max votes and winner name
sum_table=zip(candidate_name,candidate_votes)
for n in sum_table:
    if int(n[1]) > maxvalue:
        maxvalue=int(n[1])
        winner=n[0]

#Print in terminal
print(f"""
Election Results
-------------------------
Total Votes: {len(candidates)}
-------------------------
""")

for z in candidates_report:
    print(z)

print(f"""
-------------------------
Winner: {winner}
""")

#Create final report in txt file
output_file = os.path.join("analysis", "final_report.txt")
with open(output_file,'w') as file:
    file.write(f"""
Election Results
-------------------------
Total Votes: {len(candidates)}
-------------------------
""")
    for z in candidates_report:
        file.write(z)
        file.write('\n')
    file.write(f"""
-------------------------
Winner: {winner}
""")