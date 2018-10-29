# First we'll import the os module
import os
# Module for reading CSV files
import csv

# Write paths
inputFile = os.path.join('..', '..', 'gitlab-data-analytics', '02-Homework', '03-Python', 'Instructions','PyBank','Resources', 'budget_data.csv')
outputFile = os.path.join("budgetanalysis.txt")

# Assign Variables
totalMonths = 0
monthChange = []
changeList = []
max = ["", 0]
min = ["", 999999999999999]
totalNet = 0
monthlyAvg = 0

# Method 1: Plain Reading of CSV files
with open(inputFile) as financialData:
    reader = csv.reader(financialData)

# Read Header Row
    header = next(reader)
    
# Extract first row
    firstRow = next(reader)
    totalMonths = totalMonths + 1
    totalNet = totalNet + int(firstRow[1])
    prevNet = int(firstRow[1])
    
    for row in reader:
    
# Track Total
        totalMonths = totalMonths + 1
        totalNet = totalNet + int(row[1])

# Track Net Change
        netChange = int(row[1]) - prevNet
        prevNet = int(row[1])
        changeList = changeList + [netChange]
        monthChange = monthChange + [row[0]]
        
# Calculate Greatest Increase & Decrease
        if netChange > max[1]:
            max[0] = row[0]
            max[1] = netChange
            
        if netChange < min[1]:
            min[0] = row[0]
            min[1] = netChange
            
# Calculte Average Change
            monthlyAvg = int(sum(netChange) / len(netChange)

# Print Summary
    sumBank = (
        f"\n              PyBank Summary\n"
        f"------------------------------------------------\n"
        f"Total Months: {totalMonths}\n"
        f"Profit / Loss: ${totalNet}\n"
        f"Avg Change in Profit: ${monthlyAvg:.2f}\n"
        f"Greatest Increase: {max[0]} (${max[1]})\n"
        f"Greatest Decrease: {min[0]} (${min[1]})\n"
        f"------------------------------------------------\n")

print(sumBank)

# Export to txt file
with open(outputFile, "w") as txt_file:
    txt_file.write(output)