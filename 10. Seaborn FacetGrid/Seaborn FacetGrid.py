import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', color_codes=True)

%matplotlib inline


df = sns.load_dataset('tips')
df.head()
df['time'].value_counts()


g = sns.FacetGrid(df, col='time')

g = sns.FacetGrid(df, col='time', height=5)

g = sns.FacetGrid(df, col='time', height=5, aspect=1.5)
g.map(plt.hist, "total_bill")
plt.savefig('hist1.png')
;

g = sns.FacetGrid(df, col='time', height=5, aspect=1.5)
g.map(plt.scatter, "total_bill", "tip")
plt.savefig('scat1.png')
;

g = sns.FacetGrid(df, row='sex', col='time', height=4, aspect=2)
g.map(plt.scatter, "total_bill", "tip")
plt.savefig('scat2.png')
;

g = sns.FacetGrid(df, row='sex', col='time', hue='smoker',
                  height=4, aspect=2)
g.map(plt.scatter, "total_bill", "tip")
g.add_legend()
plt.savefig('scat3.png')
;

df.day.value_counts()

g = sns.FacetGrid(df, col="day", height=7, aspect=0.6)
g.map(sns.histplot, "total_bill")
plt.savefig('hist2.png')
;

def annotate(data, **kws):
    n = len(data)
    ax = plt.gca()
    ax.text(.1, .6, f"N = {n}", transform=ax.transAxes)

g = sns.FacetGrid(df, col="time", height=8, aspect=0.8)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total bill", "Tip")
g.map_dataframe(annotate)
plt.savefig('scat4.png')
;

