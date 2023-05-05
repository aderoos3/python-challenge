#Import dependencies
import os
import csv

#Create Pathway
budget_csv = os.path.join("Resources", "budget_data.csv")
print(budget_csv)

#Lists to store data
months = []
totalpl = 0
changespl = []
increase = []
decrease = []
firstpl = 0
lastpl = 0
flag = True
counter = 0
averageChange = 0
prevpl = 0

#With open, read in function
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    #skip header
    next(csvreader)
    
    #Add total amount of months
    for row in csvreader :
        months.append(row[0])
        monthCount = len(months)
        
        #add net total profit/loss
        totalpl = totalpl + int(row[1])
        
        #add an if statement & counter for first month value
        counter = counter + 1
        if flag:
            firstpl = row[1]
            flag = False
    
    #variable for last month value
    lastpl = row[1]
    
    #Change in profit/loss and average change
    changespl = int(lastpl) - int(firstpl)
    averageChange = round(changespl/(monthCount-1),2)
    
    #add conditional statement in loop if change is bigger than the previous one then save as variable for greatest increase & decrease
    #prevpl = int((row[1]) - 1)
    
    #if changespl > prevpl:
        #increase = changespl
        #increase = row[0]
        
    #print titles
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(monthCount))
    #totalmonths= "Total Months: " + str(monthCount)
    print("Net Total: $" + str(totalpl))
    print("Average Change: $" + str(averageChange))
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")
    
#Zip lists together
cleaned_csv = zip(months)

output_file = os.path.join("analysis","budget_datafinal.csv")

#open output file
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    
    #write the header row
    writer.writerow(["Months", "Net Total", "Changes", "Increase", "Decrease"])

    #write in zipped rows
    writer.writerows(cleaned_csv)

