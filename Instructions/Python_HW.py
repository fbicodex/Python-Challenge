import os
import csv

pybank_csv = os.path.join("Pybank", "Resources", "budget_data.csv") 

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvfile)
 
    
    Profit_Total = 0
    Month_Total = 0
    Average_Change = 0
    last_line = 0
    Big_Profit = 0
    Low_Profit = 0
    Change = 0

    # Read through each row of data after the header
    for row in csvreader:
        if Month_Total == 0:
            last_line = int(row[1])
            Month_Total = Month_Total + 1
            Profit_Total = Profit_Total + int(row[1])
            
        else:
            Month_Total = Month_Total + 1
            Profit_Total = Profit_Total + int(row[1])
            Change = (int(row[1]) - last_line)
            Average_Change = (int(row[1]) - last_line) + Average_Change
            last_line = int(row[1])
        if Big_Profit < Change:
            Big_Profit = Change
            Big_Month = row[0]
        if Low_Profit > Change:
            Low_Profit = Change
            Low_Month = row[0]


    Average_Change = Average_Change/(Month_Total - 1)
    
    print(f"Financial Analysis:")
    print(f"----------------------------------------------------")
    print(f"Total Months: {Month_Total}")
    print(f"Total: ${Profit_Total}")
    print(f"Average Change: ${Average_Change}")
    print(f"Greatest Increase in Profits: {Big_Month} ${Big_Profit}")
    print(f"Greatest Decrease in Profits: {Low_Month} ${Low_Profit}")
