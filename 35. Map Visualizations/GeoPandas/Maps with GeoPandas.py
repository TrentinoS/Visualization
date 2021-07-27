#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import geopandas as gpd


# In[2]:


# set the filepath
fp = "Shape_Files\\India_Districts_2020\\India_Districts.shp"
#read the file stored in variable fp
map_df = gpd.read_file(fp)
# check data type so we can see that this is a GEOdataframe
map_df.head()


# In[3]:


#Isolate the UP districts
map_df_up = map_df[map_df['stname'] == 'UTTAR PRADESH']

#Check the resulting UP Plot
map_df_up.plot()


# In[4]:


#Get the data CSV file
df = pd.read_csv('Data\\UP_dummy_data.csv')
df.head()


# In[5]:


#Get district wise installation count
df_district = df['installation_district'].value_counts().to_frame()
df_district.reset_index(inplace=True)
df_district.columns = ['district','count']
df_district.head()


# In[6]:


#Merge the districts df with the geopandas df
merged = map_df_up.set_index('dtname').join(df_district.set_index('district'))
merged.head()


# In[7]:


#Fill NA values
merged['count'].fillna(0,inplace=True)
#Get max count
max_installs = merged['count'].max()


# In[8]:


#Generate the choropleth map
fig, ax = plt.subplots(1, figsize=(20, 12))
merged.plot(column='count', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
# remove the axis
ax.axis('off')
# add a title
ax.set_title('District-wise Dummy Data', fontdict={'fontsize': '25', 'fontweight' : '3'})
# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=0, vmax=max_installs))
# add the colorbar to the figure
cbar = fig.colorbar(sm)


# # Generating a number of choropleth maps to stitch to form a video

# In[9]:


#We've seen how to generate a standalone choropleth map using geopandas
#Now we'll attempt to generate a number of such maps and stitch them together
#to form an animated video
df['Installed On'] = df['Installed On'].apply(lambda x: x.split('T')[0])
df['Installed On'] = pd.to_datetime(df['Installed On'],format="%Y-%m-%d")
df.head()


# In[12]:


date_min = df['Installed On'].min()
n_days = df['Installed On'].nunique()

fig, ax = plt.subplots(1, figsize=(20, 12))

for i in range(0,n_days):
    date = date_min+timedelta(days=i)
    
    #Get cumulative df till that date
    df_c = df[df['Installed On'] <= date]
    
    #Generate the temporary df
    df_t = df_c['installation_district'].value_counts().to_frame()
    df_t.reset_index(inplace=True)
    df_t.columns = ['dist','count']
    
    #Get the merged df
    df_m = map_df_up.set_index('dtname').join(df_t.set_index('dist'))
    df_m['count'].fillna(0,inplace=True)
    fig, ax = plt.subplots(1, figsize=(20, 12))
    df_m.plot(column='count',
                cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
    # remove the axis
    ax.axis('off')
    # add a title
    ax.set_title('District-wise Dummy Data', 
                 fontdict={'fontsize': '25', 'fontweight' : '3'})
    # Create colorbar as a legend
    sm = plt.cm.ScalarMappable(cmap='Blues', 
            norm=plt.Normalize(vmin=0, vmax=df_t['count'].iloc[0]))
    # add the colorbar to the figure
    cbar = fig.colorbar(sm)
    fontsize = 36
    
    # Positions for the date
    date_x = 82
    date_y = 29

    ax.text(date_x, date_y, 
            f"{date.strftime('%b %d, %Y')}", 
            color='black',
            fontsize=fontsize)
    fig.savefig(f"Frames/frame_{i:03d}.png", 
                dpi=100, bbox_inches='tight')
    plt.close()

