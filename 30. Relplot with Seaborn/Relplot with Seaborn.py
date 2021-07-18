#!/usr/bin/env python
# coding: utf-8

# # Data Visualizations with Seaborn 
# ### Visualizing using **seaborn.relplot()** function (Relational Plots in Seaborn)

# **Visualizing statistical relationships**
# 
# Statistical analysis is a process of understanding how variables in a dataset relate to each other and how those relationships depend on other variables. Visualization can be a core component of this process because, when data are visualized properly, the human visual system can see trends and patterns that indicate a relationship.

# **Scatter Plots-** Each plot point is an independent observationLine Plots- Each plot point represents the same `thing` , typically tracked over time

# Why use `relplot()` instead of `scatterplot()`. Because `relplot()` lets you create subplots in a single feature.

# ## Importing Packages

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(150,80)})
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Loading and Reading the dataset
# 
# We have loaded the dataset using pandas library.
# 
# Exploratory Data Analysis

# In[2]:


df = pd.read_csv('Data/student-alcohol-consumption.csv')
df.head()


# ## Data Visualization
# 
# 1. **SCATTER PLOTS-**
# 
# Creating scatter plot with relplot() function of Seaborn library. Passing “kind” parameter equals to “scatter” will create scatter plot. Also, passing data , x and y inputs as the parameters.

# In[3]:


sns.relplot(data=df, x='absences', y='G3',kind='scatter',height=8, aspect=2)
plt.savefig('Plots/plot1.jpg')
plt.show()


# **Subplots in Columns:** Passing the `col` parameter in the function to create subplots in columns.

# In[4]:


sns.relplot(x="absences", y="G3", data=df,kind="scatter",col="study_time", height=5, aspect=1)
plt.savefig('Plots/plot2.jpg')
plt.show()


# **Subplots in Rows:** Passing the `row` parameter in the function to create subplots in rows.

# In[5]:


sns.relplot(x="absences", y="G3", data=df,kind="scatter",row="study_time", height=5, aspect=1)
plt.savefig('Plots/plot3.jpg')
plt.show()


# In[6]:


sns.relplot(x="G1", y="G3", data=df, kind='scatter', height=8, aspect=1)
plt.savefig('Plots/plot4.jpg')
plt.show()


# **Ordering Columns:** Changing the order of columns in subplots by passing the order in the `col_order` parameter.

# In[7]:


sns.relplot(x="G1", y="G3", data=df, kind="scatter",col="schoolsup", col_order=["yes","no"], height=5, aspect=1.5)
plt.savefig('Plots/plot5.jpg')
plt.show()


# **Ordering rows and columns:** Changing the order of both the rows and columns by passing order of columns and rows in `col_order` and `row_order` parameters.

# In[8]:


sns.relplot(x="G1", y="G3", 
            data=df,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],row="famsup",
            row_order=["yes", "no"],height=5, aspect=1)
plt.savefig('Plots/plot6.jpg')
plt.show()


# ## Reading the 2nd dataset

# In[9]:


mpg = pd.read_csv('Data/mpg.csv')
mpg.head()


# ## Changing the size of scatter plot points

# **Customizing Scatter Plots:** 
# 
# 1. By changing the size of scatter plot points

# In[10]:


sns.relplot(x="horsepower",y="mpg",size="cylinders",data=mpg, kind='scatter',height=8, aspect=1.5)
plt.savefig('Plots/plot7.jpg')
plt.show()


# ## Setting the Style and Color of the Scatter plot

# 2. Setting the style and color of scatter points

# In[11]:


sns.relplot(x='acceleration',y='mpg', data=mpg, kind='scatter',style="origin",hue="origin",height=8, aspect=1.5)
plt.savefig('Plots/plot8.jpg')
plt.show()


# ## Line Plot

# Creating line plot with relplot() function of Seaborn library. Passing `kind` parameter equals to `line` will create line plot. Also, passing data , x and y as the input parameters.

# In[12]:


sns.relplot(data=mpg,x="model_year",y="mpg",kind='line',height=8, aspect=1.5)
plt.savefig('Plots/plot9.jpg')
plt.show()


# ## Visualizing Standard Deviation with Line Plot

# Visualizing standard deviation with line plot:Passing `ci` parameter equals to `sd` gives the visualization of standard deviation in line plot.

# In[13]:


sns.relplot(data=mpg,x="model_year",y="mpg",kind='line', ci='sd',height=8, aspect=1.5)
plt.savefig('Plots/plot10.jpg')
plt.show()


# ## Plotting subgroups in Line Plots

# **Plotting subgroups in line plots:** Passing `ci` parameter equals to `None`

# In[14]:


sns.relplot(data=mpg, x="model_year",y="horsepower", kind='line',ci=None,height=8, aspect=1.5)
plt.savefig('Plots/plot11.jpg')
plt.show()


# ## Setting the style and color of the Line plot

# **Setting the style and color of line plot:** Passing `style` parameter to change style and `hue` parameter to change the color.

# In[15]:


sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None,style="origin",hue="origin",height=8, aspect=1.5)
plt.savefig('Plots/plot12.jpg')
plt.show()


# ## Setting the Markers in the Line plot and making each line with the same style

# **Setting the markers in the line plot:** Changing the markers in the line plot by passing TRUE in the `markers` parameter.

# In[16]:


sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",markers=True,dashes=False,height=8, aspect=1.5)
plt.savefig('Plots/plot13.jpg')
plt.show()

