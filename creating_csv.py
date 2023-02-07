#create by Andrew Bienvenue
# Creating a CSV file with content

# importing the csv module
import csv

#creating a variable that holds the path to our file

req_file = "C:\\Users\\andre\\Desktop\\Python_first\\data.csv"
f = open(req_file, 'w', newline= "")

#creating variable that would allow us to read the req_file
# setting the delimiter as a comma
csv_writer = csv.writer(f, delimiter=",")

#creating a variable to hold the data

my_data = [['No:', ' Name:', ' Age:', ' Country:'], [1,"Kevin Howard", 30, "USA"],\
[2, "Andrew Bien", 26, "USA"], [3, "Danny Johns", 24, "UK"]]

csv_writer.writerows(my_data)

#closing the file
f.close()
