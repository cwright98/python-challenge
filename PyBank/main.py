import os
import csv

path = r"C:\Users\Curtis Wright\Desktop\HW GT ATL\python-challenge\PyBank\budget_data.csv"

count = 0  # initialize counter
running_sum = 0
max = 0
min = 0

with open(path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)  # skip the first row
    for row in csvreader:
        count = count + 1  # keep track of the number of rows/months
        running_sum = running_sum + int(row[1])  # keep the running sum
        if int(row[1]) > max:
            max = int(row[1])
            max_month = row[0]
        elif int(row[1]) < min:
            min = int(row[1])
            min_month = row[0]

print(f"There are {count} months in this statement")
print(f"The net sum of profits and losses are ${running_sum}")
print(f"The average gain was {running_sum / count} per month.")
print(f"The company gained the most money, ${max}, in {max_month}.")
print(f"The company lost the most money, ${min}, in {min_month}.")

financial_statement_file = open("Financial_analysis.txt", "w")
financial_statement_file.write(f"There are {count} months in this statement")
financial_statement_file.write(f"The net sum of profits and losses are ${running_sum}")
financial_statement_file.write(f"The average gain was {running_sum / count} per month.")
financial_statement_file.write(f"The company gained the most money, ${max}, in {max_month}.")
financial_statement_file.write(f"The company lost the most money, ${min}, in {min_month}.")
financial_statement_file.close()









