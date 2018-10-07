# Carolina-Data-Challenge

Website of final visualization: https://public.tableau.com/profile/trivikrama.sai.p.t#!/vizhome/LeadingcausesofdeathintheUS/Dashboard1?publish=yes

I participated in the Carolina Data Challenge this year, and this shows off the project I worked on in a group of two. Our project was the visualzation of death rates of different diseases across the country and grouped by state.
I cleaned the csv file given to us in the competition using Python and the pandas library. The original csv file can be seen as "Original Dataset".
The Dataset provided was a CSV with 10296 rows, with the year, 113 cause name, cause name, state, deaths, and age adjusted death rate. The data contained data from the years 1999-2015.

One of the things I had to do was remove columns we did not want to visualize from the dataset, which were 113 cause name and age adjusted death rate. This cleaned csv can be seen as "Cleaned Dataset".
I also had to check if the data had equality across the dataset. I first checked if the data had an equal amount of data points for each year between 1999-2015, and then checked if the data had an equal amount of data points for each individual disease. The data had an equal amount of data points for both.

Another thing I did was group the dataset by year and cause name, then add up the sums and convert it to a csv, which can be seen as "Population Totals". I thought this would allow us to have data for the entire population of the US. However, what I did not know was that the data already included the data for the entire population, represented as United States in the state column.
This turned out useful though, as our visualization of data of the total population deaths showed an outlier in the year 2015, as it was suddenly less than 2014, which did not make sense in terms of the overall trend of the data. These grouped totals actually turned out to be
population * 2 for all the totals (it added up all the states and also the population), except for 2015, which showed us the population data point was not calculated properly for that point.

My main focus was the cleaning of the dataset, which my group member then plugged into Tableau and Visualized.

Some interesting things we found in our visualization was the large percentage of deaths coming from cancer and heart attacks, and how little proportionally other diseases seemed to make up of the total number of deaths per year. Also, when you go through the state data, all states have their highest proportion of deaths from cancer and heart attack. Proportionally, the percentage of heart attacks and cancer seem to be even across the US, something I did not expect, as I thought geographically poorer regions would have a higher prevalence of these two leading causes of death. Also, from the year 1999-2014 (2015 as well, but data point was miscalculated), the graph of all causes of death in the United States seems to follow an exponential model, coinciding with exponential population growth.
