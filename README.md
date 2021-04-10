Summarizing Automobile Evaluation Data
In the following project you’ll use what you’ve learned about summarizing categorical data to analyze a sample from a popular open source dataset. This dataset contains information on the cost and physical attributes of several thousand cars. Originally, this dataset was used for to train a classification model that assigned an acceptability score/category to cars based on these attributes.

The car evaluation dataset has been sourced from the UCI Machine Learning Repository and has been slightly modified for this project. Specifically, one additional field manufacturer_country has been simulated for illustrative purposes. You can read more about the details, features, and original uses of this dataset in research on the UCI data description page.

Tasks
11/11 Complete
Mark the tasks as complete by checking them off
Summarizing Manufacturing Country
1.
manufacturer_country is a nominal categorical variable that indicates the country of the manufacturer of each car reviewed. Create a table of frequencies of all the cars reviewed by manufacturer_country. What is the modal category? Which country appears 4th most frequently? Print out your results.


Stuck? Get a hint
2.
Calculate a table of proportions for countries that appear in manufacturer_country in the dataset. What percentage of cars were manufactured in Japan?


Stuck? Get a hint
Summarizing Buying Costs
3.
buying_cost is a categorical variable which describes the cost of buying any car in the dataset. Print out a list of the possible values for this variable.


Stuck? Get a hint
4.
buying_cost is an ordinal categorical variable, which means we can create an order associated with the values in the data and perform additional numeric operations on the variable. Create a new list, buying_cost_categories, that contains the unique values in buying_cost, ordered from lowest to highest.


Stuck? Get a hint
5.
Convert buying_cost to type 'category' using the list you created in the previous exercise.


Stuck? Get a hint
6.
Calculate the median category of the buying_cost variable and print the result.


Stuck? Get a hint
Summarizing Luggage Capacity
7.
luggage is a categorical variable in the car evaluations dataset that records the luggage capacity for each reviewed car. Calculate a table of proportions for this variable and print the result.


Stuck? Get a hint
8.
Are there any missing values in this column? Replicate the table of proportions from the previous exercise, but do not drop any missing values from the count. Print your result.


Stuck? Get a hint
9.
Without passing normalize = True to .value_counts(), can you replicate the result you got in the previous exercises?


Stuck? Get a hint
Summarizing Passenger Capacity
10.
doors is a categorical variable in the car evaluations dataset that records the count of doors for each reviewed car. Find the count of cars that have 5 or more doors. You can identify cars with 5+ doors by looking for cars that have a value of '5more' in the doors column. Print your result.


Stuck? Get a hint
11.
Find the proportion of cars that have 5+ doors and print the result.
