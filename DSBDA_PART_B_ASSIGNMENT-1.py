#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#vaibhav devkate
#TI75
#1. Perform the following operations using Python on the Facebook metrics data sets
#a. Create data subsets
#b. Merge Data
#c. Sort Data
#d. Transposing Data
#e. Shape and reshape Data


# In[16]:


import pandas as pd 
import numpy as np
df=pd.read_csv("dataset_Facebook.csv", sep=";")
df


# In[17]:


df.describe()


# In[18]:


df.shape


# In[21]:


#subset 1
df1=df[['Page total likes', 'Category', 'Post Month', 'Post Weekday']].loc[0:15]
df1


# In[22]:


#subset 2
df2=df[['Page total likes', 'Category', 'Post Month', 'Post Weekday']].loc[16:30]
df2


# In[23]:


#subset 3
df3=df[['Page total likes', 'Category', 'Post Month', 'Post Weekday']].loc[31:50]
df3


# In[24]:


#merging subsets
merging=pd.concat([df1,df2,df3])
merging


# In[27]:


#sorting
sort_values=df.sort_values('Page total likes', ascending=False)
sort_values


# In[28]:


#transpose data
transposing=df.transpose()
transposing


# In[29]:


#shaping
shaping=df.shape
shaping


# In[31]:


#reshaping
pivot_table=pd.pivot_table(df,index=['Type','Category'], values="like")
print(pivot_table)

