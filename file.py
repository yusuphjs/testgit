"""
CSV code Chunks
Aug 7th, 2019
"""
import csv
import sys
import os

input_file = r"path/to/csv.csv"

# returns the csv as an object
data1 = csv.reader(open(input_file), delimiter = ',')

# returns the csv as a list of lists where each row
data = list(csv.reader(open(input_file), delimiter = ','))

row1 = data[1]

x.strip()

 # create a list comprehension loop to use
               # the ".strip()" method for every item in
               # the list "row1"
    example:   [item.strip() for item in row1]

# Not Correct, will result in a list of strings
[item.strip() for row in data for item in row]

# Correct, results in a list of lists
newdata = []
for row in data:
    newline = [item.strip() for row in data]
    newdata.append(newline)


#Combining multiple operations
>>>newdata = []
>>>for row in data:
...    newline = [item.strip() for item in row]
       newline = [item.title() for item in newline]
       newline[2] = newline[2].lower()
       # more things here
...    newdata.append(newline)

# Other string methods
string.title() # Makes the first letter of each word uppercase
string.upper() # Makes every letter of each word uppercase
string.lower() # Makes every letter of every word lowercase
string.capitalize() # Makes the first letter of each string an uppercase letter.
# more: https://www.w3schools.com/python/python_ref_string.asp

# Changing one column of a csv only
newdata = []
for row in data:
    newline = row
    newline[2] = newline[2].lower()
    # converts only the third column into lowercase
    newdata.append(newline)
