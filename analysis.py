#Program that reads the Iris Dataset into Python and run analysis on the dataset
#Author: Orla Corry 


#importing libraries 

from stat import ST_DEV
from statistics import stdev
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

with open ("variable_summary.txt" , 'wt') as f: #creating a .txt file  as 'f'which i can write to 
    #from now on the file will be referred to as 'f'

    f.write('\t\t\t\t\t\t\tAnalysis:') #Heading-using \t to tab to centre 
    print("\n\nShape:\n", shape, file =f) #\n here so there is 2 lines space from the heading 
    #the first argument is the command shape and the second argument is to send it to file 'f'
    print ("\n\nDataframe Description:\n",  describe, file =f) #/n after description so there is a break between 'Description' and the output


    sliced_data_Iris_setosa=df[0:50] #saving the Iris- Setosa sliced data as a variable 
    sliced_data_Iris_versicolor=df[50:100] #saving Iris-versicolor data as variable 
    sliced_data_Iris_virginica =df[100:150] #saving Iris-virginica data as variable


    print ("\n\nDetails of the Iris-setosa:\n",  sliced_data_Iris_setosa, file=f)
    print ("\n\nDetails of Iris-versicolor:\n", sliced_data_Iris_versicolor, file=f)
    print ("\nDetails of Iris-virginica:\n", sliced_data_Iris_virginica, file =f)







sns.set_theme(style="darkgrid")  #https://seaborn.pydata.org/generated/seaborn.barplot.html
sns.countplot(x = 'Species', data =df) #to show how many of each sample of flower there are in the dataframe
#plt.show()                              #https://www.geeksforgeeks.org/countplot-using-seaborn-in-python/

#plt.savefig('species_count.png')

    
