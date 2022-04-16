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

with open ("variable_summary.txt" , 'wt') as f: #creating a .txt file  as 'f'which i can write to 
    #from now on the file will be referred to as 'f'

    f.write('\t\t\t\t\t\t\tAnalysis:') #Heading-using \t to tab to centre 
    print("\n\nShape:\n", shape, file =f) #\n here so there is 2 lines space from the heading 
    #the first argument is the command shape and the second argument is to send it to file 'f'
    print ("\n\nDataframe Description:\n",  describe, file =f) #/n after description so there is a break between 'Description' and the output

    
    sliced_data_Iris_setosa=df[0:50] #saving the Iris- Setosa sliced data as a variable 
    sliced_data_Iris_versicolor=df[50:100] #saving Iris-versicolor data as variable 
    sliced_data_Iris_virginica =df[100:150] #saving Iris-virginica data as variable


    #print ("\n\nDetails of the Iris-setosa:\n",  sliced_data_Iris_setosa, file=f)
    #print ("\n\nDetails of Iris-versicolor:\n", sliced_data_Iris_versicolor, file=f)
    #print ("\nDetails of Iris-virginica:\n", sliced_data_Iris_virginica, file =f)


    #Analysis on Sepal Length
    std_data = round(df["SepalLengthCm"].std(),2)
    mean_data = round(df["SepalLengthCm"].mean(),2)
    median_data = round(df["SepalLengthCm"].median(),2)

    print ("\n\n\nAnalysis on Sepal Length of three Iris types combined:", file=f)
    print ("The standard deviation of Sepal Length is {}cm:".format(std_data), file=f)
    print ("The mean of Sepal Length is {}cm:".format(mean_data), file=f)
    print ("The median of Sepal Length is {}cm:".format(median_data), file=f)

    #Analysis on Sepal Width
    std_data = round(df["SepalWidthCm"].std(),2)
    mean_data = round(df["SepalWidthCm"].mean(),2)
    median_data = round(df["SepalWidthCm"].median(),2)

    print ("\n\n\nAnalysis on Sepal Width of three Iris types combined:", file=f)
    print ("The standard deviation of Sepal Width is {}cm:".format(std_data), file=f)
    print ("The mean of Sepal Width is {}cm:".format(mean_data), file=f)
    print ("The Median of Sepal Width is {}cm:".format(median_data), file=f,)
    
    #Analysis on Petal Length
    std_data = round(df["PetalLengthCm"].std(),2)
    mean_data = round(df["PetalLengthCm"].mean(),2)
    median_data = round(df["PetalLengthCm"].median(),2)

    print ("\n\n\nAnalysis on Petal Length of three Iris types combined:", file=f)
    print ("The standard deviation of Petal Length is {}cm:".format(std_data), file=f)
    print ("The mean of Petal Length is {}cm:".format(mean_data), file=f)
    print ("The Median of Petal Length is {}cm:".format(median_data), file=f,)

    #Analysis on Petal Width
    std_data = round(df["PetalWidthCm"].std(),2) #using round() here to round the output to 2 decimal places
    mean_data = round(df["PetalWidthCm"].mean(),2)
    median_data = round(df["PetalWidthCm"].median(),2)

    print ("\n\n\nAnalysis on Petal Width of three Iris types combined:", file=f)
    print ("The standard deviation of Petal Width is {}cm:".format(std_data), file=f)
    print ("The mean of Petal Width is {}cm:".format(mean_data), file=f)
    print ("The Median of Petal Width is {}cm:".format(median_data), file=f,)

                    #*****Data on the indivudual Iris types, Sepals and Petals******

    #printing from the Sepal Lenth & Width columns and only printing the Iris-setosa data - using code [0:50]
    print("\n\n\nSepal Length and Sepal Width Analysis of Iris-setosa:\n",file=f)
    print(df[["SepalLengthCm",]][0:50].describe(), file = f) #using describe() to get analysis of the specidied column and rows
    print(df[["SepalWidthCm",]][0:50].describe(), file = f)

    #printing from the Petal Lenth & Width columns and only printing the Iris-setosa data - using code [0:50]
    print("\n\n\nPetal Length and Petal Width Analysis of Iris-setosa:\n",file=f)
    print(df[["PetalLengthCm",]][0:50].describe(), file = f) #using describe() to get analysis of the specidied column and rows
    print(df[["PetalWidthCm",]][0:50].describe(), file = f)



    #printing from the Sepal Lenth & Width columns and only printing the Iris-versicolor data - using code [50:100]
    print("\n\nSepal Length and Sepal Width Analysis of Iris-versicolor:\n", file=f)
    print(df[["SepalLengthCm",]][50:100].describe(), file = f) #using describe() to get analysis of the specidied column and rows
    print(df[["SepalWidthCm",]][50:100].describe(), file = f)

    #printing from the Petal Lenth & Width columns and only printing the Iris-versicolor data - using code [50:100]
    print("\n\nPetal Length and Petal Width Analysis of Iris-versicolor:\n", file=f)
    print(df[["PetalLengthCm",]][50:100].describe(), file = f) #using describe() to get analysis of the specidied column and rows
    print(df[["PetalWidthCm",]][50:100].describe(), file = f)



    #printing from the Sepal Lenth & Width columns and only printing the Iris-virginica data - using code [100:150]
    print("\n\nSepal Length and Sepal Width Analysis of Iris-virginica:\n", file=f)
    print(df[["SepalLengthCm",]][100:150].describe(), file = f) #using describe() to get analysis of the specidied column and rows
    print(df[["SepalWidthCm",]][100:150].describe(), file = f)

    #printing from the Sepal Lenth & Width columns and only printing the Iris-virginica data - using code [100:150]
    print("\n\nPetal Length and Petal Width Analysis of Iris-virginica:\n", file=f)
    print(df[["PetalLengthCm",]][100:150].describe(), file = f) #using describe() to get analysis of the specidied column and rows
    print(df[["PetalWidthCm",]][100:150].describe(), file = f)



    












sns.set_theme(style="darkgrid")  #https://seaborn.pydata.org/generated/seaborn.barplot.html
sns.countplot(x = 'Species', data =df) #to show how many of each sample of flower there are in the dataframe
#plt.show()                              #https://www.geeksforgeeks.org/countplot-using-seaborn-in-python/

#plt.savefig('species_count.png')

    
