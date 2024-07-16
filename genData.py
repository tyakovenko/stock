#generate fake data csv file to test on
#created in separate folder data
'''
Purpose: generate random data for testing purposes
Notes: In general, data is usually exported in a csv or txt file. In order to further process them they will be put into python data structure
called a DataFrame from the pandas package (https://pypi.org/project/pandas/)
See examples on how to use the data structures in all the other code files

'''

import csv
import random

# avg price of stock for a given company per month
months = 12
companies = 10
filename = 'data/rd.csv'

# Generate random numbers for the grid
data = [[random.randint(1, 100) for _ in range(companies)] for _ in range(months)]

# Specify the filename


# Write the data to a CSV file
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvwriter.writerow(row)

print(f"CSV file '{filename}' has been generated with random numbers.")

