import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Data/data.csv')
df.head()

years = [str(year) for year in range(1980,2014)]
df.set_index('Country', drop=True, inplace=True)

#Exercise 1:
#Plot a line graph of immigration from Haiti using df.plot().

haiti_df = df.loc['Haiti', years].to_frame()
sns.set_style('ticks')

# Let's plot the Line plot
haiti_df.plot(kind='line', figsize=(15,8))
plt.title('Immigration from Haiti to Canada (1980-2013)')
plt.xlabel('Years')
plt.ylabel('Immigrants')
plt.savefig('Plots/Plot1.jpg')
plt.show()

haiti_df.index.get_loc('2010')

haiti_df.plot(figsize=(15,8))
plt.title('Immigration from Haiti to Canada (1980-2013)')
plt.ylabel('Immigrants')
plt.xlabel('Years')
plt.text(30, 6500, 'Earthquake')
plt.savefig('Plots/Plot2.jpg')
plt.show()

#Exercise 2: Adding more countries to the line plot.
#Let's compare the number of immigrants from Nigeria and Egypt from 1980 to 2013
# First, we select the countries for the plot

nigeria_egypt_haiti = df.loc[['Nigeria', 'Egypt', 'Haiti'],years].T

nigeria_egypt_haiti.head()

nigeria_egypt_haiti.plot(figsize=(15,8))
plt.title('Line Plot of Nigeria, Egypt and Haiti Immigration')
plt.savefig('Plots/Plot3.jpg')
plt.show()

df.sort_values('Total', ascending=False, inplace=True)
df.head()

#Exercise 3:
#Let’s create an Area plot of the countries with the highest migration to Canada.
# First select the top 5 countries
top_5_df = df.head()

df.head()

# Next select only the columns representing the years for each country, before applying the transpose method.
top_5_df = top_5_df[years].transpose()

# let's view the selection
top_5_df.head()

# First let's define a Font Dict
dict_={'fontsize': 18,
        'fontweight' : 10,
        'verticalalignment': 'baseline',
      'color': 'Red'}

top_5_df.plot(kind='area', figsize=(15,8))
plt.title('Area Plot of Top 5 Migrating Countries to Canada', fontdict=dict_)

dict_['fontsize'] = 14
plt.xlabel('Years', fontdict=dict_)
plt.ylabel('Immigrants', fontdict=dict_)
plt.savefig('Plots/Plot4.jpg')
plt.show()

#Let's re-plot the above plot as an unstacked plot
top_5_df.plot(kind='area', figsize=(15,8), stacked=False)
plt.title('Area Plot of Top 5 Migrating Countries to Canada', fontdict=dict_)

dict_['fontsize'] = 14
plt.xlabel('Years', fontdict=dict_)
plt.ylabel('Immigrants', fontdict=dict_)
plt.savefig('Plots/Plot5.jpg')
plt.show()

#Exercise 4:
#Let’s re-plot the above Area plot as an unstacked plot
top_5_df.plot(kind='area', figsize=(15,8), stacked=False, alpha=0.3)
plt.title('Area Plot of Top 5 Migrating Countries to Canada', fontdict=dict_)

dict_['fontsize'] = 14
plt.xlabel('Years', fontdict=dict_)
plt.ylabel('Immigrants', fontdict=dict_)
plt.savefig('Plots/Plot6.jpg')
plt.show()

#Exercise 5:
#let’s see both stacked and unstacked Area plots with an alpha of 0.4.
fig = plt.figure(figsize=(30,10)) # create figure

ax0 = fig.add_subplot(121) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(122) # add subplot 2 (1 row, 2 columns, second plot)

# Subplot 1: Stacked Area plot
top_5_df.plot(kind='area', alpha=0.4, ax=ax0) # add to subplot 1
ax0.set_title('Stacked Area Plot with alpha=0.4')
ax0.set_ylabel('Immigrants')
ax0.set_xlabel('Years')

# Subplot 2: Unstacked Area Plot
top_5_df.plot(kind='area', stacked=False, alpha=0.4, ax=ax1) # add to subplot 2
ax1.set_title ('Unstacked Area plot with alpha=0.4')
ax1.set_ylabel('Immigrants')
ax1.set_xlabel('Years')
plt.savefig('Plots/Plot7.jpg')
plt.show()
