#Loading Packages
import pandas as pd
import numpy as np
import plotly.express as px

#Loading Data
df = pd.read_csv('Data/Pokemon.csv', index_col = 0, encoding = 'unicode_escape')
df.head()

#Scatter Plot
fig = px.scatter(df, x='Attack', y='Defense')
fig.show()
fig.write_image('Plots/Scatter1.jpg')

fig = px.scatter(df, x='Attack', y='Defense', color='Stage', hover_data = ['Name'])
fig.show()
fig.write_image('Plots/Scatter2.jpg')

fig = px.scatter(df, x='Attack', y='Defense', color='Type 1', size = 'Total', hover_data=['Name'])
fig.show()
fig.write_image('Plots/Scatter3.jpg')

#Line Plot
x = list(range(df.shape[0]))
y = df['Total'].sort_values()
fig = px.line(df, x, y, labels={'x':'Pokemon Rank', 'y':'Total Score'}, hover_data=['Name'])
fig.show()
fig.write_image('Plots/Line.jpg')

#Box Plot
df_copy = df.drop(['Name', 'Type 1', 'Type 2', 'Total', 'Stage', 'Legendary'], axis=1)
fig = px.box(df_copy)
fig.show()
fig.write_image('Plots/Box.jpg')

#Violin Plot
fig = px.violin(df_copy)
fig.show()
fig.write_image('Plots/Violin1.jpg')

fig = px.violin(df, x='Type 1', y='Attack', color='Type 1')
fig.show()
fig.write_image('Plots/Violin2.jpg')

#Heatmaps
corr = df_copy.corr()
labels = list(df_copy)
fig = px.imshow(corr, x=labels, y=labels)
fig.show()
fig.write_image('Plots/Heatmap.jpg')

#Density Plots
fig=px.density_heatmap(df,x='Attack', y='Defense')
fig.show()
fig.write_image("Plots/Density.jpg")

#Histograms
fig = px.histogram(df, x='Attack')
fig.show()
fig.write_image('Plots/Histo.jpg')

