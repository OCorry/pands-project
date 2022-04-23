# pands-project
# Author: Orla Corry

<<<<<<< HEAD
=======
Introduction
The objective of this project was to obtain a copy of Ronald Fisher’s Iris dataset and carry out some analysis on the data contained in it using various libraries imported into Python.
Before beginning the task, I set about doing some research into Fisher himself and the history and development of the Iris dataset. 
Born in England on the 17th of February 1890, Fisher was a statistician, geneticist and eugenicist (The Royal Society | Scient in The Making, n.d.).The data for this dataset was gathered by a botanist named Edgar Anderson and the dataset was then established by Fisher in the early 20th Century. The data set contains 150 observations in total, allowing for 50 samples of the three different types of Iris Flower; Setosa, Virginica and Versicolor. On these, then he focused on four attributes or variables from each species Sepal Length, Sepal Width, Petal Length and Petal Width (Qureshi, 2021). 

Setting up 
For this project I needed the relevant programming environment on my machine. This included two software packages; namely Cmder and VS Code. I also needed to create a repository on my Github account to allow for my work to be accessed on another machine. 
I set up my pands-project repository on Github and cloned it to my machine using Cmder. I made sure that my repository on Github was set to public for public viewing. I then downloaded a copy of the dataset from (Singh, 2018) as an excel, comma separated values (csv) file and saved this in my pands-project directory. 


Research and Analysis
I imported the relevant libraries needed for the data analysis, namely; Pandas (imported as pd), Numpy (imported as np), Matplotlib(imported as plt) and Seaborn (imported as sns).  Pandas is used for analysing data in tabular form, ie an excel sheet. Numpy is used for working with arrays and while Matplotlib is used for plotting data, Seaborn provides more of a variety of visualisation patterns with the data (Misal, 2019) 
To start off, using Pandas I imported the Iris dataframe in csv format, storing it as ‘df’. 

Firstly, I set about researching what types of analyses I could carry out on the dataset. I sourced some code from (GeeksforGeeks, 2022). Initially I was able to run some analysis but needed to find a way of directing the output to the .txt file rather than just printing it to the terminal I found how to do this from (Christiansen, 2016), where the first argument is what the user wants to input into the .txt file and the second argument is to save it to file=f) in his example, but in my data analysis, the file=f argument wasn’t always the second argument. 

To start off, using Pandas I carried out a df.shape() command to establish to structure of the dataframe. Fig. 1 shoes the output printed 
Fig 1:
 
Confirming that the dataframe contains 150 rows of data and 6 column names (or attributes). 

Next, using the describe() function I printed a number of statistics of all three Iris types from the dataframe: 
Fig 2:
 
Again, this method printed out that there is 150 of each attribute, ie 150 rows of samples. It also gave the mean (or average) length and width of each of the floating point attributes. The standard deviation of each attribute is the measure of how dispersed the data is around the mean value (w3schools, n.d.) 
In this dataframe, the standard deviation of Sepal Length, Sepal Width, Petal length and Petal width are normal as the values lie around 0 or 1 so they lie close to the mean so the data is reliable.
This function also outputs the maximum and minimum values for the 4 floating point attributes I am working with.  

Using the df.iloc() function (w3schools, 2022), I was able to slice out the data for each of the Iris types individually. To do this, I used code df.iloc([0:50]) to allow for the inclusion of the last row of data of the Iris-setosa to be included. Similarly, I included index 50 through to index 100 to allow for the last row of data of the Iris-versicolor and index 100 through to 150 to include the last row of data for the Iris-virginica.  I saved this output to the analysis_summary.txt file using file =f so that the output could be pushed up to Github (Christiansen, 2016). 

Next, I wanted to focus on analysing the data for each particular flower. To do this I had to single out the data for each individual Iris type. I sourced code to work on this from (GeeksforGeeks, 2021) . 
First, I singled out the data relating to the Iris-setosa from index 0 to 50 (to allow for the inclusion of the last row of this Iris type).  I did the same for the other two; index 50 to 100 (to include the last row of this type) for the Iris-versicolor and index 100 to 150 (to include the last row of this type) for the Iris-virginica. These are saved to the analysis_summary.txt file. 


To analyse the individual Iris Flowers Petals and Sepals, I used a combination of code from two sources. Firstly, to get the statistical data from a particular column, I used code from (Miller, 2022). I still needed to restrict the code to run just on the number of columns that were relevant to the particular flower. To do this is sourced code from (GeeksforGeeks, 2021). 
So working these two pieces of code together, I was able to analyse the Sepal Length & Width and Petal Length and Width of the 3 Iris flowers individually. For example the first one, from the dataframe (df) I used describe() on the Sepal Length column only and restricted the column so that the data would only be taken from the Iris-setosa flower. I did this by inputting [0:50] so that index 0 through to index 50, to allow for row 51 to be included also. 

Histograms: 
Next I worked on histograms to give a visual description of the four attributes of the Iris flowers. I created each histogram using df.hist() and inputted different parameters to make the them more readable. (pandas, 2022) & (ImportanceOfBeingErnest, 2017) .
I gave the histograms a title and labelled the x and y axes. (tutorials point, 2022). I used the plt.show() command to print the output in the terminal and also used the plt.savefig(“filename.png”) to save the output as a .png file that would push up to Github. 
In total, I had four histograms; Sepal Length, Sepal width and Petal Length & petal width. These showed me that the most frequent sepal length was about 5.5cm/5.6 cm. The most frequent sepal width was between 3.0 and 3.2cm. The most frequent petal length was between 1.0 and 1.6cm and petal length between 0.1 and 0.6cm. The most normally distributed histogram was the sepal width. This corresponds to the standard deviation figure I got above of 0.433594 which lies between 0 and 1.


Fig 3.1: 

![Sepal Length](https://user-images.githubusercontent.com/98124862/164892735-c1fc424a-0180-4100-b07a-c7e48e688cc8.PNG)


Fig 3.2:

![Sepal Width](https://user-images.githubusercontent.com/98124862/164892747-aa94397c-ffc3-4341-b363-e2d9886b7c28.PNG)
  

Fig 3.3:	 

![Petal Width](https://user-images.githubusercontent.com/98124862/164892645-c0fae330-8c2f-4b96-a794-5f3106643650.PNG)

Fig3.4:

![Petal Width](https://user-images.githubusercontent.com/98124862/164892759-40013b78-5a81-4ace-9fa2-dea88c998474.PNG)

  



>>>>>>> 663b835abae99bef08a4bb1f408c05c699d0154c
