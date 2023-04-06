# importing libaries
import os
import csv

# print header
print("Financial Analysis \n____________________________\n")

# defining variables
totalMonths = 0
totalProfit = 0
startingProfit = 0
endingProfit = 0
maxIncreaseDate = ""
maxDecreaseDate = ""
maxIncrease = 0
maxDecrease = 0
isFirstRow = True
csvpath = os.path.join("Resources","budget_data.csv")

# open CSV file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # read header row
    csvHeader = next(csvreader)
    
    # loop through remaining rows
    for row in csvreader:
        currentDate = row[0]
        currentProfit= int(row[1])
        
        # set starting values to first row profit
        if(isFirstRow) :
            startingProfit=currentProfit
            isFirstRow=False

        # calculate other values
        totalMonths+=1
        totalProfit+=currentProfit
        endingProfit=currentProfit
        if(currentProfit>maxIncrease):
            maxIncrease=currentProfit
            maxIncreaseDate=currentDate
        if(currentProfit<maxDecrease):
            maxDecrease=currentProfit
            maxDecreaseDate=currentDate    

# print to terminal
print(f"Total Months : {totalMonths}")
print(f"Total : ${totalProfit}")
print(f"Average Change : ${(endingProfit-startingProfit)/totalMonths}")
print(f"Greatest Increase in Profits : {maxIncreaseDate} (${maxIncrease})")
print(f"Greatest Decrease in Profits : {maxDecreaseDate} (${maxDecrease})")

# print to output file
txtPath = os.path.join("Analysis","Output.txt")
with open(txtPath,"w") as output_file:
    output_file.write("Financial Analysis \n____________________________\n\n")
    output_file.write(f"Total Months : {totalMonths}\n")
    output_file.write(f"Total : ${totalProfit}\n")
    output_file.write(f"Average Change : ${(endingProfit-startingProfit)/totalMonths}\n")
    output_file.write(f"Greatest Increase in Profits : {maxIncreaseDate} (${maxIncrease})\n")
    output_file.write(f"Greatest Decrease in Profits : {maxDecreaseDate} (${maxDecrease})\n")