#Create by Andrew Bienvenue

# Reading a csv file in our directory

# Importing the csv module
import csv

req_file = "C:\\Users\\andre\\Desktop\\Python_first\\data.csv"

f = open(req_file, 'r')
csv_reader = csv.reader(f, delimiter ="|")

# using a for loop to read the csv file
for each_row in csv_reader:
    print(each_row)

#closing the file
f.close()
