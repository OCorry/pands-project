# Introduction:
The objective of this project was to obtain a copy of Ronald Fisher’s Iris dataset and carry out some analysis on the data contained in it using various libraries imported into Python.
Before beginning the task, I set about doing some research into Fisher himself and the history of the Iris dataset. 
Born in England on the 17th of February 1890, Fisher was a statistician, geneticist and eugenicist (The Royal Society | Scient in The Making, n.d.).The data for this dataset was gathered by a botanist named Edgar Anderson and the dataset was then established by Fisher in the early 20th Century. The data set contains 150 observations in total, allowing for 50 samples of the three different types of Iris Flower; Setosa, Virginica and Versicolor. On these, then he focused on four attributes or variables from each species Sepal Length, Sepal Width, Petal Length and Petal Width (Qureshi, 2021). 

## Setting up the Environment:
For this project I needed the relevant programming environment on my PC. This included two software packages; namely Cmder and VS Code. I also needed to create a repository on my Github to allow me to push up my work so that it could be accessed from another machine.
I set up my pands-project repository on Github and cloned it to my machine using Cmder. I made sure that my repository on Github was set to public for public viewing. I then downloaded a copy of the dataset from Kaggle,(Singh, 2018) as an excel, comma separated values (csv) file and saved this in my pands-project directory. In VS code inside of the pands-project directory, I created a program called analysis.py for my code. 

## Research and analysis:
I imported the relevant libraries needed for the data analysis, namely; Pandas (imported as pd), Numpy (imported as np), Matplotlib (imported as plt) and Seaborn (imported as sns).  Pandas is used for analysing data in tabular form, as I was using data from an Excel sheet, I could use this. Numpy is used for working with arrays and while Matplotlib is used for plotting data, Seaborn provides more of a variety of visualisation patterns with the data (Misal, 2019) . For some regression analysis, I also used the sklearn module and imported linear model from it (w3schools, 2022).
To start off using Pandas, I imported the Iris dataframe in csv format, storing it as ‘df’ for easier access when doing my analysis. This printed out the first 5 rows and last 5 rows of data only. I also found that the whole dataset could be printed in the terminal using  code print(df.to_string) (w3schools, 2022) I commented both of these out however, as I didn’t need them to print in the terminal each time I ran the program. 


I needed to find a way of directing the output to the .txt file rather than just printing it to the terminal. I found how to do this from (Christiansen, 2016), where in his case, the first argument is what the user wants to input into the .txt file and the second argument is to save it to file=f. However, in my data analyses, the file=f argument wasn’t always the second argument as some of my commands had multiple arguments.

Using the with open () command, I created a text file called variable_summary.txt in which I could save some of my output to. I opened this .txt file in write text (wt) mode as I needed to be able to write to the file. I did not use append mode as it kept adding changes that I made rather than re-writing them and deleting obsolete output that I no longer wanted. I saved this file as ‘f’ to represent the file to make it more accessible when sending the output to the .txt file. 

### Analysis of the Dataframe:
Next, I set about researching what types of analyses I could carry out on the dataset. I sourced some code from (GeeksforGeeks, 2022). 
Using Pandas I carried out a df.shape() command to establish to structure of the dataframe. Fig. 1 provides output confirming that the dataframe contains 150 rows of data and 6 column names (or attributes). 

Fig 1:
 
![fig 1](https://user-images.githubusercontent.com/98124862/165548379-559889eb-8240-4690-b54b-feeb04eb3b23.png)

Next, using the describe() function I printed a number of statistics of all three Iris types from the dataframe: 
Fig 2:
 
![fig 2](https://user-images.githubusercontent.com/98124862/165548443-497b0cc2-f2db-4a01-9689-37b9c205ac54.png)
 

Again, this method printed out that there is 150 rows of data foreach attribute. It also gave the mean (or average) length and width of each of the floating point attributes and the standard deviation of each attribute.  The standard deviation of each attribute is the measure of how dispersed the data is around the mean value (w3schools, n.d.) 
In this dataframe, the standard deviation of Sepal Length, Sepal Width, Petal length and Petal width are normal as the values lie around 0 or 1 so they lie close to the mean so the data is reliable.
This function also outputs the maximum and minimum values for the 4 floating point attributes.  

I also used different code to specifically print out the mean, standard deviation and median of each of the Iris flowers’ four attributes. From (Zach, 2021), I sourced code to get the standard deviation of a column of data and I stored the code as variable std_dev. For the mean and median (EasyTweaks, 2022), I stored the code as mean and median respectively. I used the round() function here also to round the output to 2 decimal places.  In addition, I used the .format() function to format the output as string. I inputted file=f as second argument to save the output to the .txt file.

### Analysis of the three Individual Iris Flower types:
Using the df.iloc() function (w3schools, 2022), I was able to slice out the data for each of the three Iris flower types individually. To do this, I used code df.iloc([0:50]) to allow for the inclusion of the last row of data of the Iris-setosa to be included. Similarly, I included index 50 through to index 100 to allow for the inclusion of all the rows of the Iris-versicolor data and finally, index 100 through to 150 to include all rows of data for the Iris-virginica.  Again, I saved this output to the analysis_summary.txt.

Next, I wanted to focus on analysing the data for each particular Iris type. To analyse the individual Iris Flowers’ Petals and Sepals, I used a combination of code from two sources. Firstly, to get the statistical data from a particular column, I used code from (Miller, 2022). However, using this alone was going to take the data from the whole column but I wanted to single out the data for each Iris type individually. 
To do this, I sourced code from (GeeksforGeeks, 2021). I singled out the data relating to the Iris-setosa from index 0 to 50 (to allow for the inclusion of the last row of this Iris type).  I did the same for the other two; index 50 to 100 (to include the last row of this type) for the Iris-versicolor and index 100 to 150 (to include the last row of this type) for the Iris-virginica. 
So working these two pieces of code together, I was able to analyse the data of the three Iris flowers individually. For example the first one, from the dataframe (df) I used .describe() function on the Sepal Length column only and restricted the column so that the data would only be taken from the Iris-setosa flower. I did this by inputting [0:50] so that index 0 through to index 50, to allow for row 51 to be included also. From this then I was able to get the count, mean, standard deviation, minimum and maximum values for each of the Iris flowers individually.  Again, I used the file =f argument to save to the analysis_summary.txt file.


### Regression Analysis:
I carried out some regression analysis on the Iris flowers’ sepals and petals. I sourced code for this from (W3schools, 2022). Using this, I was able to input values for the Sepal Length and Sepal Width to predict what the size of the petal length would be for example. Using Sepal length, 7.7cm and Sepal Width 3.3 for example, the regression analysis predicted that the Petal length would be 7.3cm. Again, I used file=f argument to save to the .txt file. 

### Histograms: 
Next I worked on histograms to give a visual description of the four attributes of the Iris flowers. I created each histogram using df.hist() and inputted different parameters to make the them more readable. (pandas, 2022) & (ImportanceOfBeingErnest, 2017) .
I gave the histograms a title and labelled the x and y axes. (tutorials point, 2022). I used the plt.show() command to print the output in the terminal (I commented this command out so that it didn’t print each time the program ran). I also used the plt.savefig(“filename.png”) to save the output as a .png file to push up to Github. 
In total, I had four histograms; Sepal Length & Sepal width and Petal Length & petal width. These showed me that the most frequent sepal length was about 5.5cm/5.6 cm. The most frequent sepal width was between 3.0 and 3.2cm. The most frequent petal length was between 1.0 and 1.6cm and petal length between 0.1 and 0.6cm. The most normally distributed histogram was the sepal width. This corresponds to the standard deviation figure I got above of 0.433594 which lies between 0 and 1.


![Figure_1](https://user-images.githubusercontent.com/98124862/167013755-f4af36bf-099d-497f-b561-c2a420a1388f.png)


![Sepal Length](https://user-images.githubusercontent.com/98124862/165548664-61a38f23-cda4-409b-a782-446ba3ffb4c1.PNG)  ![Sepal Width](https://user-images.githubusercontent.com/98124862/165548806-c2f82473-302a-47bc-be52-e026102c079d.PNG)



                                                                                                                                                                                                                      
                                                                                                                           

![Petal Length](https://user-images.githubusercontent.com/98124862/165548881-a1c56367-50f9-4643-b751-05f78145680b.PNG)   ![Petal Width](https://user-images.githubusercontent.com/98124862/165548927-74b3e873-f6a0-44b8-9c32-cd30b22ddfc7.PNG)





  
### Scatterplots:

Finally, I generated 6 scatterplots for the 6 variations of pairs of variables:
Sepal Length & Sepal Width, Petal Length and Petal Width, Sepal Length and Petal Width, Petal Length and Sepal Width, Petal Length and Sepal Length, Sepal Width and Petal width.

To create the scatterplots, I used sns.impolot() (Gallery, 2018). Using this code allowed me to modify the appearance of the plot. To include the “Species” variable so that I could work with it, I used ‘hue’. I included a fit line to give more of an idea of how linear the scatterplot was. To include this, I inputted ‘fit_reg=True’. I also included a legend to distinguish which plot was for which Iris type. I labelled the x and y axes as appropriate for each scatterplot.

From (cmdline, 2009), I sourced code to change the colours of each of the three plots on each scatterplot, again to allow for easier interpretation of the plot. The colours were inputted as a dict{} and then stored as variable color_dict. This made it easier as I could just simply input color_dict in my code. 

To take a look at the scatterplot of sepal width and petal width of the Iris-versicolor for example. There is a high correlation between the two as the scatterplot is quite compact and it fits quite well around the straight line. (Frost, 2022) This means that there is a strong connection between the sepal width and petal width in terms of the growth of one impacts the growth of the other.

However, taking for example the sepal length and sepal width of the Iris-virginica, there is very low correlation between them as the plot is not compact and it does not fit well around the straight line. This means that there is little connection between the sepal length and sepal with in terms of their growth.  

![Capture1](https://user-images.githubusercontent.com/98124862/165567109-af264d72-c3e6-4d50-80d4-2e9e2d652803.PNG)

![Capture2](https://user-images.githubusercontent.com/98124862/165567147-7b978d7e-5a48-48b4-951e-12d50e3180db.PNG)

![Capture3](https://user-images.githubusercontent.com/98124862/165567193-aacca54f-fede-4d40-a852-a8185dd26cce.PNG)







## Conclusion:

From the scatter plots in particular, it would appear the that the data for the Iris-setosa petals and sepals is the most correlated as the scatter plots are quite clusterd around the straight line. The Iris-versicolour and Iris- virginica data however, is less correlated as the scatter plots are generally quite dispersed. I found that while the standard deviation of each attribute from the dataframe as a whole (all 150 rows together) was generally quite normal-ranging between 0and 1- the histograms did not reflect this for the Petal Length and Petal Width. 
I found from this project that there is a vast range of different analysis that can be done on this dataframe despite its small size. From my research, I found that there are numerous different types and structures of code that can be used for the same type of analysis. 






# Bibliography


Christiansen, A., 2016. Directing print output to a .txt file. [Online] 
Available at: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
[Accessed 13 April 2022].


Christiansen, A., 2016. Directing print output to a .txt file. [Online] 
Available at: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
[Accessed 23 April 2022].


cmdline, 2009. How To Specify Colors to Scatter Plots in Python. [Online] 
Available at: https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/
[Accessed 23 April 2022].


EasyTweaks, 2022. EasyTweaks. [Online] 
Available at: https://www.easytweaks.com/pandas-mean-column-dataframe/
[Accessed 11 April 2022].


Frost, J., 2022. Statistics By Jim Making statistics intuitive. [Online] 
Available at: https://statisticsbyjim.com/graphs/scatterplots/
[Accessed 23 April 2022].


Gallery, P. G., 2018. Use categorical variable to color scatterplot in seaborn. [Online] 
Available at: https://python-graph-gallery.com/43-use-categorical-variable-to-color-scatterplot-seaborn
[Accessed 23 April 2022].


GeeksforGeeks, 2021. Python – Basics of Pandas using Iris Dataset. [Online] 
Available at: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
[Accessed 16 April 2022].


GeeksforGeeks, 2021. Python – Basics of Pandas using Iris Dataset. [Online] 
Available at: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
[Accessed 16 April 2022].


GeeksforGeeks, 2022. Exploratory Data Analysis on Iris Dataset. [Online] 
Available at: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
[Accessed 06 April 2022].


ImportanceOfBeingErnest, 2017. Python Matplotlib Histogram Color. [Online] 
Available at: https://stackoverflow.com/questions/42172440/python-matplotlib-histogram-color
[Accessed 21 April 2022].


Miller, W., 2022. Python Dataframes: Describing a single column. [Online] 
Available at: https://stackoverflow.com/questions/50165953/python-dataframes-describing-a-single-column
[Accessed 16 April 2022].


Misal, D., 2019. Comparing Python Data Visualization Tools: Matplotlib vs Seaborn. [Online] 
Available at: https://analyticsindiamag.com/comparing-python-data-visualization-tools-matplotlib-vs-seaborn/
[Accessed 10 April 2022].


pandas, 2022. pandas.DataFrame.hist. [Online] 
Available at: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
[Accessed 21 April 2022].


Qureshi, S., 2021. The Might Iris Dataset. [Online] 
Available at: https://braintoy.ai/2021/04/19/mighty-iris-dataset/
[Accessed 9 April 2022].


Singh, S., 2018. Iris.csv. [Online] 
Available at: https://www.kaggle.com/datasets/saurabh00007/iriscsv?resource=download
[Accessed 9 April 2022].


The Royal Society | Scient in The Making, n.d. The Royal Society | Scient in The Making. [Online] 
Available at: https://makingscience.royalsociety.org/s/rs/people/fst00034451
[Accessed 09 April 2022].


tutorials point, 2022. tutorials point. [Online] 
Available at: https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm
[Accessed 21 April 2022].


w3schools, 2022. Machine Learning - Multiple Regression. [Online] 
Available at: https://www.w3schools.com/python/python_ml_multiple_regression.asp
[Accessed 27 April 2022].


W3schools, 2022. Machine Learning - Multiple Regression. [Online] 
Available at: https://www.w3schools.com/python/python_ml_multiple_regression.asp
[Accessed 27 April 2022].


w3schools, 2022. Pandas DataFrame iloc Property. [Online] 
Available at: https://www.w3schools.com/python/pandas/ref_df_iloc.asp
[Accessed 23 April 2022].


w3schools, 2022. Pandas Read CSV. [Online] 
Available at: https://www.w3schools.com/python/pandas/pandas_csv.asp
[Accessed 10 April 2022].


w3schools, n.d. Machine Learning - Standard Deviation. [Online] 
Available at: https://www.w3schools.com/python/python_ml_standard_deviation.asp#:~:text=Standard%20deviation%20is%20a%20number,out%20over%20a%20wider%20range
[Accessed 10 April 2022].


Zach, 2021. Statistics.Simplified Statology. [Online] 
Available at: https://www.statology.org/pandas-standard-deviation/ 
[Accessed 11 April 2022].

