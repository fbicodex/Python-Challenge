
import os
import csv

pybank_csv = os.path.join("Pybank", "Resources", "budget_data.csv") 

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvfile)
 
    #Set up my variables to 0
    Profit_Total = 0
    Month_Total = 0
    Average_Change = 0
    last_line = 0
    Big_Profit = 0
    Low_Profit = 0
    Change = 0

    # Read through each row of data after the header
    for row in csvreader:
    #we need to define the first variable to have our Avg Change to work for the first line
        if Month_Total == 0:
            last_line = int(row[1])
            Month_Total = Month_Total + 1
            Profit_Total = Profit_Total + int(row[1])
    #after first line/row -> start adding up months, profits; get change of current row - last row and add to avg change counter      
        else:
            Month_Total = Month_Total + 1
            Profit_Total = Profit_Total + int(row[1])
            Change = (int(row[1]) - last_line)
            Average_Change = Change + Average_Change
            last_line = int(row[1])
    #created a separate if statment to find greatest profit through Change -> once finds Big Profit, take the month of the row current on
        if Big_Profit < Change:
            Big_Profit = Change
            Big_Month = row[0]
    #same concept as profit but for loss
        if Low_Profit > Change:
            Low_Profit = Change
            Low_Month = row[0]

    #get average change which is our avg change counter divded by the total months - 1 (since first line doesn't get substracted)
    Average_Change = Average_Change/(Month_Total - 1)
    
    #print out my findings to terminal and text file

    f = open("bank_output.txt", "a")

    print(f"----------------------------------------------------")
    print(f"Financial Analysis:")
    print(f"----------------------------------------------------")
    print(f"Total Months: {Month_Total}")
    print(f"Total: ${Profit_Total}")
    print(f"Average Change: ${Average_Change}")
    print(f"Greatest Increase in Profits: {Big_Month} ${Big_Profit}")
    print(f"Greatest Decrease in Profits: {Low_Month} ${Low_Profit}")
    
    #text file print statmnts

    print(f"----------------------------------------------------", file=f)
    print(f"Financial Analysis:", file=f)
    print(f"----------------------------------------------------", file=f)
    print(f"Total Months: {Month_Total}", file=f)
    print(f"Total: ${Profit_Total}", file=f)
    print(f"Average Change: ${Average_Change}", file=f)
    print(f"Greatest Increase in Profits: {Big_Month} ${Big_Profit}", file=f)
    print(f"Greatest Decrease in Profits: {Low_Month} ${Low_Profit}", file=f)

    f.close()
