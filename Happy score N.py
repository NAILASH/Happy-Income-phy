#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


H=pd.read_csv("C:\\Users\\Super\\Downloads\\happyscore_income.csv")


# In[6]:


H


# In[7]:


H.plot.scatter("avg_income","happyScore")
plt.grid()


# In[8]:


H.plot()

