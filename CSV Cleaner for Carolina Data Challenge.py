
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as nm
data = pd.read_csv('https://query.data.world/s/i4qhpwxwteprslnsmbn63o2jhrvgat')
data.head()
to_drop = ['113 Cause Name', 'Age-adjusted Death Rate']
data.drop(to_drop, inplace=True, axis = 1)
data.head()
#No need to set index


# In[6]:


data.to_csv('Death_Causes_Modified.csv')


# In[22]:


#Not implemented************
#state = data['State']
#US = state.str.contains('United States')
#US[:5]
#df['Place of Publication'] = nm.delete(data, nm.where(State, 'United States'), 0)
#Not implemented************


# In[17]:


data.get_dtype_counts() #checking whether numeric or regular data is stored in each one, make sure int is stored in something we will total
#figure out how to calculate population 
#basic-Group by year, cause name, add up all of them then store it in a new population csv


# In[16]:


data['Year'].value_counts() #shows we have equality for each diesease


# In[17]:


data['Cause Name'].value_counts()


# In[12]:


#Group the data so we can calculate the population totals, group it by year and cause name
#basic-Group by year, cause name, add up all of them then store it in a new population csv, population/2 should equal united states, as the united states is part of the states
data.groupby(['Year', 'Cause Name'])['Deaths'].sum()
#Since this has more than one column, it is returning a dataframe, not a series, a series is one column
grouped_data = data.groupby(['Year', 'Cause Name'])
grouped_data['Deaths'].sum().to_csv('Population_Totals')


# In[29]:


data.groupby(['Year', 'Cause Name', 'State'])['Deaths'].sum()
#Test for Vikram's graphs


# In[2]:




