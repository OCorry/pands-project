#Author: Orla Corry 
'''
import sys 
with open(sys.argv[1], 'rt') as f:
    data = f.read()  #storing f.read() in a variable called data so it is more accessable
print (data)
#dataset source https://datahub.io/machine-learning/iris#data
#checking that I have saved the dataset correcly and checking if i can read it in from the command line
'''
import pandas as pd  #using Pandas library to read the file into Python as a comma seperated values(csv) file
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
filename =("iris.csv")
df = pd.read_csv (filename)
print (df)
#print(df.to_string()) #use this code to print the whole dataframe (df) rather than just the first 5 & last 5 rows
                    #https://www.w3schools.com/python/pandas/pandas_csv.asp


sns.countplot(x = 'class', data =df,) #to show how many of each class(or type) of flower there are in the dataframe)
#plt.show()                              #https://www.geeksforgeeks.org/countplot-using-seaborn-in-python/

plt.savefig('class_count.png')

