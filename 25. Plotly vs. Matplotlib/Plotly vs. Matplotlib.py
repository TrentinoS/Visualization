# Importing Libraries
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
plt.rcParams["figure.figsize"] = (15,8)

# Setting the dataset to the variable df
df = pd.read_csv('Data/world-happiness-report-2021.csv')
df.head()

#Bar Plot
happiest_regions = df.groupby(by=['Regional indicator'])['Ladder score'].mean().sort_values(ascending=False).reset_index()
happiest_regions = pd.DataFrame(happiest_regions)
happiest_regions

###Plotly Express
px.bar(happiest_regions, x='Regional indicator', y='Ladder score', color='Regional indicator')

###Matplotlib
plt.bar(x = happiest_regions['Regional indicator'], height = happiest_regions['Ladder score'])
plt.savefig('Plots/Plot2.png')
plt.show()

import seaborn as sns
sns.set_theme(style="darkgrid")

plt.figure(figsize=(14,6))
sns.barplot(x='Regional indicator', y='Ladder score', data=df, palette="tab10")
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Plots/Plot3.png')
plt.show()

#Histogram

###Plotly Express
px.histogram(df, x='Ladder score', color='Regional indicator')

###Matplotlib
sns.histplot(data=df, x='Ladder score', hue='Regional indicator')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Plots/Plot5.png')
plt.show()

#Scatterplot

###Plotly Express
px.scatter(df, x='Ladder score', y='Logged GDP per capita', color='Regional indicator')

###Matplotlib
sns.scatterplot(data=df, x='Ladder score', y='Logged GDP per capita', hue='Regional indicator')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Plots/Plot7.png')
plt.show()

#Line Charts

###Plotly Express
df2 = pd.read_csv('Data/world-happiness-report.csv')
df2.head(5)

px.line(df2, x='year', y='Life Ladder', color='Country name')

first_10_countries = df2.head(110)

px.line(first_10_countries, x='year', y='Life Ladder', color='Country name')


###Matplotlib
sns.lineplot(data=df2, x='year', y='Life Ladder')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Plots/Plot10.png')
plt.show()

sns.lineplot(data=first_10_countries, x='year', y='Life Ladder', hue='Country name')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Plots/Plot11.png')
plt.show()

#Editing

###Matplotlib
sns.histplot(data=df, x='Ladder score', hue='Regional indicator', palette='husl')
plt.title('Ladder Score Distribution', fontsize=18)
plt.xlabel('Ladder Score', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('Plots/Plot12.png')
plt.show()

#Plotly Express
px.histogram(df, x='Ladder score', color='Regional indicator',
            title='Ladder Score Distribution').update_layout(
            xaxis_title="Ladder Score",
            yaxis_title="Count",
            legend_title="Legend Title",
            font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
    )
)