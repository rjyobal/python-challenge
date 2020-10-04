#Import libraries
import os
import csv

#File path
budget_csv = os.path.join("Resources", "budget_data.csv")

#Set variables
output_row=[]
total=0
maxvalue=0
minvalue=0

#Open file - readonly
with open(budget_csv,'r',encoding='UTF-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Skip the header
    csv_header = next(csv_reader)

    #Fill out list
    for row in csv_reader:
            total=total+int(row[1])
            output_row.append(row)
            #Get Max values
            if int(row[1]) > maxvalue:
                maxvalue=int(row[1])
                maxmonth=row[0]
            #Get Min values
            if int(row[1]) < minvalue:
                minvalue=int(row[1])
                minmonth=row[0]                
    
#Build final report string
analysis=(f"""
Financial Analysis
------------------
Total Months: {len(output_row)}
Total: ${total}
Average  Change: ${round(total/len(output_row),2)}
Greatest Increase in Profits: {maxmonth} (${maxvalue})
Greatest Decrease in Profits: {minmonth} (${minvalue})
""")

#Print in terminal
print(analysis)

#Create final report in txt file
output_file = os.path.join("analysis", "final_report.txt")
with open(output_file,'w') as file:
    file.write(analysis)