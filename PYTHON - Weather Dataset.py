#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"C:\Users\Shivam Barua\Downloads\1. Weather Data (1).csv")


# In[3]:


data


# ## How to Analyze DataFrames?

# ## Head()

# In[4]:


data.head()                                         ## It shows the first N in the data (by default, N=5)


# ## Shape()

# In[6]:


data.shape                                         ## It shows the total no. of rows and columns of the dataframe 


# ## Index

# In[7]:


data.index                                        ##  The attribute provides the index of the dataframe.


# ## columns

# In[8]:


data.columns                                      ## It shows the name of each column


# ## Dtypes

# In[9]:


data.dtypes                                     ## It shows datatype of each columns


# ## Unique

# ### In a column, it shows all the. It can be applied on a single column only, not on the whole dataframe

# In[10]:


data['Weather'].unique()


# ## nunique`

# ### It shows the total no of unique values in each column. It can be applied on a single column as well as on  whole dataframe.

# In[11]:


data.nunique()


# ## Count

# ## It shows the total no of non null-values in each column. It can be applied on a single column as well as on  whole dataframe.

# In[12]:


data.count()


# ## value_counts

# ## In a column it shows all the unique values with their count. It can be applied on a single column only

# In[14]:


data['Weather'].value_counts()


# ## Info()

# ## provides basic information about the dataframe.

# In[15]:


data.info()


# In[ ]:





# ## Q) 1. Find all the uinque 'Wind Speed' values in the data.

# In[16]:


data.head(2)


# In[17]:


data.nunique()


# In[18]:


data['Wind Speed_km/h'].nunique()


# In[19]:


data['Wind Speed_km/h'].unique()                      # Answer


# ## Q) 2. Find the number of time when the 'weather is exactly clear'.

# In[20]:


data.head(2)


# In[21]:


data.Weather.value_counts()                                 #value_counts()


# In[28]:


data[data.Weather == 'Clear']                          # Filtering #data.heads(2)


# In[27]:


data.groupby('Weather').get_group('Clear')               # groupby()


# ## Q) 3. Find the number of times when the 'Wind Speed was exactly 4km/h'.

# In[29]:


data.head(2)


# In[30]:


data[data['Wind Speed_km/h'] == 4]               #Answer


# ## Q. 4) Find out all the Null Values in the data.

# In[31]:


data.isnull().sum()


# In[32]:


data.notnull().sum()


# ## Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather condition'.
# 

# In[33]:


data.head(2)


# In[67]:


data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)


# ## Q) 6. What is the mean ' Visibility'?

# In[68]:


data.head(2)


# In[37]:


data.Visibility_km.mean()


# ## Q) 7. What is the Standard Deviation of 'Pressure' in this data?

# In[38]:


data.Press_kPa.std()


# ## Q) 8. What is the variance of 'Relative humidity' in this data?

# In[40]:


data['Rel Hum_%'].var()


# ## Q) 9. Find all the instances when 'Snow' was recorded.

# In[69]:


data['Weather Condition'].value_counts()                #value_counts()                                            


# In[70]:


data[data['Weather Condition'] == 'Snow']                #Filtering


# In[71]:


data[data['Weather Condition'].str.contains('Snow')].tail(50)                                                    #str.constraint


# ## Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[54]:


data.head(2)


# In[56]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# ## Q. 11) What is the Mean value of each column against each 'Weather Condition

# In[63]:


data.head(2)


# In[72]:


data.groupby('Weather Condition').mean()


# ## Q. 12)What is the Minimum & Maximum value of each column against each 'Weather Condition' ?

# In[ ]:





# In[73]:


data.head(2)


# In[74]:


data.groupby('Weather Condition').min()


# In[75]:


data.groupby("Weather Condition").max()


# In[ ]:





# ## Q. 13) Show all the Records where Weather Condition is Fog.

# In[76]:


data[data['Weather Condition'] == 'Fog']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[78]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# ## Q. 15) Find  all Instances when:
# 
# ## A. 'Weather is Clear' and 'RelativeHumidity is greater than 50'
# 
# ## or
# 
# 
# ## B. 'Visibility is above 40'

# In[79]:


data.head(2)


# In[80]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)|(data['Visibility_km'] > 40)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




