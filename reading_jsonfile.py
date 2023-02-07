#Author: Andrew Bienvenue
#Date: 11/2022

# Reading a json file

# Importing the json module to work with json files
import json

#creating a variable to hold the file path
file_name ="C:\\Users\\andre\\Desktop\\Python_first\\sample_file.json"

with open(file_name,'r') as f:
    #making json data into python understanable data
    print(json.load(f))
# closing the file
f.close()

'''
# or you can use this method

f = open(file_name, 'r')
print(json.load(f))

#closing the file
f.close()
'''
