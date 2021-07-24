#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from matplotlib.dates import DateFormatter, WeekdayLocator
from datetime import timedelta


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv', 
    parse_dates=['date'])
df.head()


# In[3]:


countries = ['United States', 'Germany', 'United Kingdom', 'India']
df = df[df['location'].isin(countries)]


# In[4]:


df.isna().sum()


# In[5]:


df


# In[6]:


fig = px.line(df,df['date'],df['daily_vaccinations'], color='location')
fig.update_layout(
    showlegend=True,
    plot_bgcolor="white",
    )
# Edit the layout
fig.update_layout(title='Daily Vaccination Count',
                   xaxis_title='Date',
                   yaxis_title='Daily Vaccination')

