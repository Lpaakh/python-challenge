import os
import csv
import sys

budget_data = os.path.join('..', 'Resources','budget_data.csv')

with open(budget_data) as budget_data_csv:
    reader = csv.reader(budget_data_csv, delimiter=",")
    row_count = 0
    net = 0
    increase = 0
    decrease = 0
    month_year1 = 0
    month_year2 = 0
    
# Treating each row as a unique month find month count and find the net Profit/Loss
    for row in reader:
        row_count +=1
        try:
            dollars = int(row[1])
            net += dollars
            if dollars > increase: 
                increase = dollars
                month_year1 = row[0]
            if dollars < decrease:
                decrease = dollars
                month_year2 = row[0]
        except ValueError:
            continue
    print(f'Financial Analysis')
    print(f'------------------------------')
    print(f'Total Months: {(row_count)-1}')
    print(f'Total: ${net}')
    print(f'Average Change: ${(net)/(row_count-1)}')
    print(f'Greatest Increase in Profits: {month_year1} ${increase}')
    print(f'Greatest Decrease in Profits: {month_year2} ${decrease}')
        
   

# Write to text file
    sys.stdout = open("financial-analysis.txt", "w")
    print(f'Financial Analysis')
    print(f'------------------------------')
    print(f'Total Months: {(row_count)-1}')
    print(f'Total: ${net}')
    print(f'Average Change: ${(net)/(row_count-1)}')
    print(f'Greatest Increase in Profits: {month_year1} ${increase}')
    print(f'Greatest Decrease in Profits: {month_year2} ${decrease}')

    sys.stdout.close()