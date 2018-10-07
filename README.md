# Carolina-Data-Challenge

Website of final visualization:

I participated in the Carolina Data Challenge this year, and this shows off the project I worked on in a group of two. Our project was the visualzation of death rates of different diseases across the country and grouped by state.
I cleaned the csv file given to us in the competition using Python and the pandas library. The original csv file can be seen as "Original Dataset".
The Dataset provided was a CSV with 10296 rows, with the year, 113 cause name, cause name, state, deaths, and age adjusted death rate. The data was contained from 1999-2015.

One of the things I had to do was remove columns we did not want to visualize from the dataset, which were 113 cause name and age adjusted death rate. This cleaned csv can be seen as "Cleaned Dataset".
I also had to check if the data had equality across the dataset. I first checked if the data had an equal amount of data points for each year between 1999-2015, and then checked if the data had an equal amount of data points for each individual disease. The data had an equal amount of data points for both.

Another thing I did was group the dataset by year and cause name, then add up the sums and convert it to a csv, which can be seen as "Population Totals". I thought this would allow us to have data for the entire population of the US. However, what I did not know was that the data already included the data for the entire population, represented as United States in the state column.
This turned out useful though, as our visualization of data of the total population deaths showed an outlier in the year 2015, as it was suddenly less than 2014, which did not make sense in terms of the overall trend of the data. These grouped totals actually turned out to be
population * 2 for all the totals (it added up all the states and also the population), except for 2015, which showed us the population data point was not calculated properly for that point.
