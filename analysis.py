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



sns.set_theme(style="darkgrid")  #https://seaborn.pydata.org/generated/seaborn.barplot.html
sns.countplot(x = 'Species', data =df) #to show how many of each sample of flower there are in the dataframe
#plt.show()                              #https://www.geeksforgeeks.org/countplot-using-seaborn-in-python/

#plt.savefig('species_count.png')

shape = df.shape #storing as variable shape
describe = df.describe() #storing as variable describe

with open ("variable_summary.txt" , 'wt') as f: #creating a .txt file  as 'f'which i can write to 
    #from now on the file will be referred to as 'f'

    f.write('Analysis: Shape of Dataframe:') #writing a heading 'shape of dataframe and printing out result
    print("\nThe shape of this dataframe is:", shape, file =f) #\n here so output will print below heading
    #the first argument is the command shape and the second argument is to sent it to file 'f'
    f.write('\n\n\nAnalysis: Description of Dataframe:') #using \n*3 so this prints 3 lines below the first output
    print ("\n", describe, file =f) #\n here so output will print below heading

    #https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file - accessed 13/04






