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

print(df.to_string()) #use this code to print the whole dataframe (df) rather than just the first 5 & last 5 rows
                    #https://www.w3schools.com/python/pandas/pandas_csv.asp



shape = df.shape #storing as variable shape
describe = df.describe() #storing as variable describe

with open ("variable_summary.txt" , 'wt') as f: #creating a .txt file  as 'f'which i can write to 
    #from now on the file will be referred to as 'f'

    f.write('\t\t\t\t\t\t\tAnalysis:') #Heading-using \t to tab to centre 
    print("\n\nShape:\n", shape, file =f) #\n here so there is 2 lines space from the heading 
    #the first argument is the command shape and the second argument is to send it to file 'f'
    print ("\n\nDataframe Description:\n",  describe, file =f) #/n after description so there is a break between 'Description' and the output

    


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


                    #*******Sliced data for each Iris type******
    print("\n\n\nIris-setosa data (sliced from dataframe):", file =f) 
    print(df.iloc[0:50], file =f) #taking data from index location 0 to index 50 to allow for data from last row 

    print("\n\nIris-versicolor data (sliced from dataframe):", file =f)
    print(df.iloc[50:100], file =f)

    print("\n\nIris-virginica data (sliced from dataframe):", file =f)
    print(df.iloc[100:150], file =f)


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
    print(df[["PetalLengthCm",]][50:100].describe(), file = f) #using describe() to get analysis of the specified column and rows
    print(df[["PetalWidthCm",]][50:100].describe(), file = f)



    #printing from the Sepal Lenth & Width columns and only printing the Iris-virginica data - using code [100:150]
    print("\n\nSepal Length and Sepal Width Analysis of Iris-virginica:\n", file=f)
    print(df[["SepalLengthCm",]][100:150].describe(), file = f) #using describe() to get analysis of the specidied column and rows
    print(df[["SepalWidthCm",]][100:150].describe(), file = f)

    #printing from the Sepal Lenth & Width columns and only printing the Iris-virginica data - using code [100:150]
    print("\n\nPetal Length and Petal Width Analysis of Iris-virginica:\n", file=f)
    print(df[["PetalLengthCm",]][100:150].describe(), file = f) #using describe() to get analysis of the specidied column and rows
    print(df[["PetalWidthCm",]][100:150].describe(), file = f)


#Histogram of Sepal Length 
df.hist(column ="SepalLengthCm", grid=True, color="blue", legend =True) #specifically picking out the sepal length attribute
plt.title("Sepal Length") #labling the title
plt.xlabel('Sepal Length in cm', color ="green") #labling the x axis 
plt.ylabel('Count', color ="green") #labling the y axis
plt.savefig("Sepal Length.png") #saving the hist as a .png file 
#plt.show() #commenting this out - if not commented out it will print a hist in the terminal 

#Histpgram of Sepal width 
df.hist(column ="SepalWidthCm", grid=True, color="blue", legend =True)
plt.title("Sepal Width")
plt.xlabel('Sepal width in cm', color ="green")
plt.ylabel('Count', color ="green")
plt.savefig("Sepal Width.png")
#plt.show()

#Histogram of Petal Length
df.hist(column ="PetalLengthCm", grid=True, color="blue", legend =True) 
plt.title("Petal Length")
plt.xlabel('Petal Length in cm', color ="green")
plt.ylabel('Count', color ="green")
plt.savefig("Petal Length.png")
#plt.show()

#Histogram of Petal width

df.hist(column ="PetalWidthCm", grid=True, color="blue", legend =True)
plt.title("Petal Width")
plt.xlabel('Petal Width in cm', color ="green")
plt.ylabel('Count', color ="green")
plt.savefig("Petal Width.png")
#plt.show()
    
color_dict = dict({'Iris-setosa':'blue', #https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/
                  'Iris-versicolor':'purple',
                  'Iris-virginica': 'red'})

#https://python-graph-gallery.com/43-use-categorical-variable-to-color-scatterplot-seaborn
sns.lmplot( x="SepalLengthCm", y="SepalWidthCm", fit_reg=True, hue='Species', legend=True, palette =color_dict, data=df,)
plt.title("Scatterplot of Sepal Length and Sepal Width", color ="green")
plt.xlabel('Sepal Length cm', color ="green")
plt.ylabel('Sepal Width cm', color ="green")
#plt.show()
plt.savefig("Sepal Length and SepalWidth.png")

sns.lmplot( x="PetalLengthCm", y="PetalWidthCm", fit_reg=True, hue='Species', legend=True, palette =color_dict, data=df,)
plt.title("Scatterplot of Petal Length and Petal Width", color ="green")
plt.xlabel('Petal Length cm', color ="green")
plt.ylabel('Petal Width cm', color ="green")
#plt.show()
plt.savefig("Petal Lenght and Petal Width.png")

sns.lmplot( x="SepalLengthCm", y="PetalWidthCm", fit_reg=True, hue='Species', legend=True, palette =color_dict, data=df,)
plt.title("Scatterplot of Sepal Length and Petal Width", color ="green")
plt.xlabel('Sepal Length cm', color ="green")
plt.ylabel('Petal Width cm', color ="green")
#plt.show()
plt.savefig("Sepal Length and Petal Width.png")

sns.lmplot( x="PetalLengthCm", y="SepalWidthCm", fit_reg=True, hue='Species', legend=True, palette =color_dict, data=df,)
plt.title("Scatterplot of Petal Length and Sepal Width", color ="green")
plt.xlabel('Petal Length cm', color ="green")
plt.ylabel('Sepal Width cm', color ="green")
#plt.show()
plt.savefig("Petal Lenght and Sepal Width.png")

sns.lmplot( x="PetalLengthCm", y="SepalLengthCm", fit_reg=True, hue='Species', legend=True, palette =color_dict, data=df,)
plt.title("Scatterplot of Petal Length and Sepal Length", color ="green")
plt.xlabel('Petal Length cm', color ="green")
plt.ylabel('Sepal Length cm', color ="green")
#plt.show()
plt.savefig("Petal Lenght and Sepal Length.png")

sns.lmplot( x="SepalWidthCm", y="PetalWidthCm", fit_reg=True, hue='Species', legend=True, palette =color_dict, data=df,)
plt.title("Scatterplot of Sepal Width and Petal Width", color ="green")
plt.xlabel('Sepal Width cm', color ="green")
plt.ylabel('Petal Width cm', color ="green")
#plt.show()
plt.savefig("Sepal Width and Petal Width.png")







    
