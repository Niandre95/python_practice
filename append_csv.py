# create by Andrew Bienvenue

# appending bulk Information to a csv  file

# Importing the csv module
import csv

# defiding the files path
req_file = "C:\\Users\\andre\\Desktop\\Python_first\\data.csv"
data_file = "C:\\Users\\andre\\Desktop\\Python_first\\info.txt"

#Reading the first information file
f = open(data_file, "r")
content = f.read()
f.close()

# append the information file contents into the data files
dfile = open(req_file, "a")
dfile.write(content)
dfile.close()
