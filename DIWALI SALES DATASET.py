#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


df = pd.read_csv(r"C:\Users\Shivam Barua\Desktop\ms excel\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv", encoding= "unicode_escape")


# In[5]:


df.shape


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[9]:


df


# In[10]:


#check for null values
pd.isnull(df).sum()


# In[11]:


# drop null values
df.dropna(inplace=True)


# In[12]:


df


# In[13]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[14]:


df['Amount'].dtypes


# In[17]:


df.columns


# In[18]:


#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})


# In[19]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# ## Exploratory Data Analysis

# ## Gender

# In[20]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# ###  * From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men *

# ## Age

# In[22]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# ###  *From above graphs we can see that most of the buyers are of age group between 26-35 yrs female *

# ## State

# In[24]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[25]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# ###  * From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively *
# 

# ## Marital Status

# In[26]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[27]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# ##  * From above graphs we can see that most of the buyers are married (women) and they have high purchasing power *

# ## Occupation

# In[28]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[29]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# ## * From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector *

# ## Product Category

# In[30]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[31]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# ## * From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category *

# In[32]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


#  ## Conclusion:

# *Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*

# In[ ]:




