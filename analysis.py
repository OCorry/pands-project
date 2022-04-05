#Author: Orla Corry 
'''
import sys 
with open(sys.argv[1], 'rt') as f:
    data = f.read()  #storing f.read() in a variable called data so it is more accessable
print (data)
#dataset source https://datahub.io/machine-learning/iris#data
#checking that I have saved the dataset correcly and checking if i can read it in from the command line
'''
import pandas as pd
filename =("iris.csv")
df = pd.read_csv (filename)
print(df.to_string()) #use this code to print the whole dataframe (df) rather than just the first 5 & last 5 rows
                    #https://www.w3schools.com/python/pandas/pandas_csv.asp
