#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv(r"C:\Users\Shivam Barua\Downloads\8. Netflix Dataset.csv")


# In[5]:


data


# ### GETTING SOME BASIC INFORMATION ABOUT THE DATASET:

# ### 1. HEAD()

# In[6]:


data.head()                                              # to show top 5 records from dataset


# ## 2. TAIL()

# In[7]:


data.tail()                                          ## to show bottom 5 records from dataset


# ## 3. SHAPE

# In[8]:


data.shape                                                 # to show number of Rows and Columns


# ## 4. SIZE 

# In[9]:


data.size                                                  #to show no. of total valves(element) in the dataset


# ## 5. COLUMNS 

# In[10]:


data.columns                                                # to show each column name


# ## 6. DTYPE

# In[12]:


data.dtypes                                                             # to show data type of each column


# ## 7. INFO

# In[14]:


data.info()                                                          # to show indexes, columns, data-types of each column, memory at once


# ### TASK 1. Are there any duplicate records in this dataset ? If yes, then remove the duplicate records.

# In[15]:


data.head()


# In[16]:


data.shape


# In[18]:


data[data.duplicated()]                                          #to check row wise and detect the duplicate rows


# In[22]:


data.drop_duplicates(inplace = True)                                  #to remove the duplicate rows completely


# In[23]:


data[data.duplicated()]


# In[24]:


data.shape


# ### Task 2. is  there any null value present in any column? Show with heat-map.

# ##  isnull ()

# In[25]:


data.head()


# In[26]:


data.isnull()                                               # To show where Null value is present


# In[27]:


data.isnull().sum()                                               # To show the count of Null values in each column


# ### seaborn library (heat-map)

# In[28]:


import seaborn as sns                                               # To import Seaborn library


# In[29]:


sns.heatmap(data.isnull())                                               # Using heat-map to show null values count


# ### Q.1. For 'House of Cards', what is the Show Id and Who is the Director of this show ?

# ### isin()

# In[30]:


data.head()


# In[31]:


data[data['Title'].isin(['House of Cards'])]       #  To show all records of a particular item in any column


# ### str.contains()

# In[32]:


data[data['Title'].str.contains('House of Cards')]          #  To show all records of a particular string in any column


# ### Q.2. In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# ### DATA TYPES

# In[33]:


data.dtypes


# ### to_datetime

# In[34]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[35]:


data.head()


# In[36]:


data.dtypes


# ### dt.year.value_counts()

# In[38]:


data['Date_N'].dt.year.value_counts()                # It counts the occurrence of all individual Years in Date column.


# ### Bar Graph

# In[39]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# ### Q.3. How many Movies & TV Shows are in the dataset ? Show with Bar Graph.

# ### groupby()

# In[40]:


data.head(2)


# In[41]:


data.groupby('Category').Category.count()                 # To group all unique items of a column and show their count


# ### countplot()

# In[47]:


import matplotlib.pyplot as plt


# In[48]:


sns.countplot(data['Category'])        # To show the count of all unique values of any column in the form of bar graph


# ### Q.4. Show all the Movies that were released in year 2000.

# ### Creating new column

# In[49]:


# data.head()
data.head(2)


# In[50]:


# data['Year'] = data['Date_N'].dt.year           # to create new Year column ; it will consider only year

data['Year'] = data['Date_N'].dt.year


# In[51]:


# data.head(2)

data.head(2)


# ### Filtering

# In[52]:


data[ (data['Category'] == 'Movie') & (data['Year']==2020) ]


# In[53]:


data[ (data['Category'] == 'Movie') & (data['Year']==2020) ]


# ### Q.5. Show only the Titles of all TV Shows that were released in India only.

# ### Filtering`

# In[55]:


# data.head(2)

data.head(2)


# In[56]:


# data [ (data['Category'] == 'TV Show') & (data['Country'] == 'India') ] ['Title']

data[ (data['Category']=='TV Show') & (data['Country']=='India') ] ['Title']


# In[ ]:


--------------------------------------------------------------------------------------------------------------------------------


# ### Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# ### value_counts()

# In[57]:


# data['Director'].value_counts().head(10)

data.head(2)


# In[58]:


data['Director'].value_counts().head(10)


# #### Q.7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".

# ### Filtering ( And, Or Operators )
# 

# In[59]:


# data[(data['Category']=='Movie') & (data['Type']=='Comedies') ]

data.head(2)


# In[60]:


data[ (data['Category']=='Movie') & (data['Type']=='Comedies') ]


# In[61]:


# data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]

data[ (data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# ### Q.8. In how many movies/shows, Tom Cruise was cast ?

# In[62]:


# data.head()

data.head(2)


# ### filtering

# In[63]:


# data[data['Cast']=='Tom Cruise']

data[data['Cast'] == 'Tom Cruise']


# ### str.contains()

# In[64]:


# data[data['Cast'].str.contains('Tom Cruise')]

data[data['Cast'].str.contains('Tom Cruise')]


# ### Creating new data-frame

# In[65]:


# data_new = data.dropna()                       # It drops the rows that contains all or any missing values.

data_new = data.dropna()


# In[66]:


# data_new.head(2)

data_new.head(2)


# In[67]:


# data_new[data_new['Cast'].str.contains('Tom Cruise')]

data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ### Q.9. What are the different Ratings defined by Netflix ?

# ### nunique()

# In[68]:


# data.Rating.nunique()

data.head(2)


# In[69]:


data['Rating'].nunique()


# ### unique()

# In[70]:


# data.Rating.unique()

data['Rating'].unique()


# #### Q.9.1. How many Movies got the 'TV-14' rating, in Canada ?

# In[72]:


data.head(2)


# In[73]:


# data[(data['Category']=='Movie') & (data['Rating'] == 'TV-14')].shape

data[(data['Category']=='Movie') & (data['Rating']=='TV-14')].shape


# In[74]:


# data[(data['Category']=='Movie') & (data['Rating'] == 'TV-14') & (data['Country']=='Canada')].shape

data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape


# #### Q.9.2. How many TV Show got the 'R' rating, after year 2018 ?

# In[75]:


# data[(data['Category']=='TV Show') & (data['Rating'] == 'R')]

data.head(2)


# In[76]:


data[(data['Category']=='TV Show') & (data['Rating']=='R')]


# In[77]:


# data[(data['Category']=='TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]

data[(data['Category']=='TV Show') & (data['Rating']=='R') & (data['Year'] > 2018)]


# ### Q.10. What is the maximum duration of a Movie/Show on Netflix ?

# In[78]:


# data.head(2)

data.head(2)


# In[79]:


# data['Duration'].unique()

data.Duration.unique()


# In[80]:


# data.Duration.dtypes

data.Duration.dtypes


# ### str.split()

# In[81]:


data.head(2)


# In[82]:


# data[['Minutes','Unit']] = data['Duration'].str.split(' ', expand=True)

data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand = True)


# In[83]:


# data.head(2)

data.head(2)


# ### max()

# In[85]:


# data.Minutes.max()

data['Minutes'].max()


# In[86]:


data['Minutes'].min()


# In[87]:


data['Minutes'].mean()


# In[88]:


data.dtypes


# ### Q.11. Which individual country has the Highest No. of TV Shows ?

# In[89]:


# data.head(2)

data.head(2)


# In[90]:


# data_tvshow = data[data['Category'] == 'TV Show']

data_tvshow = data[data['Category'] == 'TV Show']


# In[91]:


# data_tvshow.head(2)

data_tvshow.head(2)


# In[92]:


# data_tvshow.Country.value_counts()

data_tvshow.Country.value_counts()


# In[93]:


# data_tvshow.Country.value_counts().head(1)

data_tvshow.Country.value_counts().head(1)


# ### Q.12. How can we sort the dataset by Year ?

# In[94]:


# data.head(2)

data.head(2)


# In[95]:


# data.sort_values(by='Year').head(2)

data.sort_values(by = 'Year')


# In[96]:


# data.sort_values(by='Year', ascending=False).head(2)

data.sort_values(by = 'Year', ascending = False).head(10)


# ### Q.13. Find all the instances where : 

# ### Category is 'Movie' and Type is 'Dramas'

# ### or

# ###  Category is 'TV Show' & Type is 'Kids'

# In[98]:


data.head(2)


# In[99]:


# data [(data['Category']=='Movie') & (data['Type']=='Dramas')].head(2)

data [ (data['Category']=='Movie') & (data['Type']=='Dramas') ].head(2)


# In[ ]:


# data [(data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']=="Kids' TV")].head(1)

data [ (data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']== "Kids' TV") ]

