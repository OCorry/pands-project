#Program that reads the Iris Dataset into Python and run analysis on the dataset 
#Author: Orla Corry 


#importing libraries 

import pandas as pd  #to analysie data that is in tabular form
import numpy as np #for working with data stored as arrays
import matplotlib.pyplot as plt #plotting data 
import seaborn as sns #plotting data 


#reading in the dataset
filename =("iris.csv")
df = pd.read_csv (filename) #reading in the file to Python using Pandas
#print (df)

#print(df.to_string()) #use this code to print the whole dataframe (df) rather than just the first 5 & last 5 rows
                    #https://www.w3schools.com/python/pandas/pandas_csv.asp

shape = df.shape #storing as variable shape
describe = df.describe() #storing as variable describe

print (shape) #gives the number of columns and rows of the dataframe 
print (describe) #distribution of data - eg, mean, standard deviation and max & min values

sns.set_theme(style="darkgrid")  #https://seaborn.pydata.org/generated/seaborn.barplot.html
sns.countplot(x = 'Species', data =df) #to show how many of each sample of flower there are in the dataframe
#plt.show()                              #https://www.geeksforgeeks.org/countplot-using-seaborn-in-python/

plt.savefig('species_count.png')







