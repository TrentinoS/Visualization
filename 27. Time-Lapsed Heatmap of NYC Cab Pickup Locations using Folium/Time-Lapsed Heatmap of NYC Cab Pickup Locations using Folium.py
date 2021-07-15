#!/usr/bin/env python
# coding: utf-8

# ###### Steps to Making the Magic Happen:
# 
# - Data preprocessing to get the hour and day of week for all entries in my training set.
# - Used folium package to plot heatmaps of lat/long coordinates by time and day of week and saved these heatmaps in .html format
# - Used selenium to open .html files in chronological order and take screenshots of every heatmap to save as .png format
# - Defined function to animate .png files as .gifs, and stitched .png files together to create the .gif file shown above!

# # Import Packages

# In[1]:


import pandas as pd
import numpy as np
import time 

import folium
from folium.plugins import HeatMap
from IPython.display import IFrame

import os
import time
from selenium import webdriver
from PIL import Image 
import glob


# This is from the New York City Trip Duration Kaggle competition from 2017 where the goal of this project is to predict the trip duration of each ride. The target label is trip_duration.

# # Import Data

# In[2]:


df_train = pd.read_csv('Data/train.csv')


# In[3]:


df_train.head()


# In[4]:


df = df_train[['pickup_datetime', 'pickup_longitude', 'pickup_latitude']].copy()
df['day_of_week'] = pd.to_datetime(df['pickup_datetime']).dt.dayofweek
df['hour_of_day'] = pd.to_datetime(df['pickup_datetime']).dt.hour


# In[5]:


df.head()


# # Plot Heatmaps of Latitude and Longitude Coordinates

# In[6]:


# Function to visualize map
def embed_map(map, filename):
    map.save(filename)
    return IFrame(filename, width='100%', height='500px')


# # Plot heatmap of lat/long coordinates by hour and day of week

# In[7]:


dow_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}


# In[8]:


for i in range(df.day_of_week.min(), df.day_of_week.max()+1):
    for j in range(df.hour_of_day.min(), df.hour_of_day.max()+1):    
        
        # Filter to include only data for each day of week and hour of day
        df_geo = df.loc[(df.day_of_week==i) & (df.hour_of_day==j)][['pickup_latitude', 'pickup_longitude']].copy()

        # Instantiate map object 
        map_5 = folium.Map(location=[40.75, -73.96], tiles='openstreetmap', zoom_start=10)

        # Plot heatmap
        HeatMap(data=df_geo, radius=10).add_to(map_5)

        # Get day of week string from dow_dict
        d = dow_dict.get(i)
        
        # Add title to heatmap
        title_html = f'''<h3 align="center" style="font-size:20px">
                        <b>NYC Cab Pickups at {j}:00 on {d}: {len(df_geo)} rides</b></h3>
                     '''
        map_5.get_root().html.add_child(folium.Element(title_html))

        # Save map
        embed_map(map_5, f'Plots/HTML Maps Pickup/{i}_{j}_heatmap.html')


# # Automate Screenshots of heatmap files using selenium

# In[9]:


for i in range(0, 7):
    for j in range(0, 24):
        # Set file path
        tmpurl=f'E:/Setup/1. Visualization/27. Time-Lapsed Heatmap of NYC Cab Pickup Locations using Folium/Plots/HTML Maps Pickup/{i}_{j}_heatmap.html'
        
        # Set browser to Chrome
        browser = webdriver.Chrome()
        
        # Open file in browser
        browser.get(tmpurl)
        
        # If hour is < 10, add 0 for sorting purposes and to keep chronological order
        if j < 10:
            browser.save_screenshot(f'Plots/Maps Pickup PNG/{i}_0{j}_heatmap.png')
        else:
            browser.save_screenshot(f'Plots/Maps Pickup PNG/{i}_{j}_heatmap.png')
        
        # Close browser
        browser.quit()


# # Create Animated .gif file

# In[10]:


def png_to_gif(path_to_images, save_file_path, duration=500):
    frames = []
    
    # Retrieve image files
    images = glob.glob(f'{path_to_images}')
    
    # Loop through image files to open, resize them and append them to frames
    for i in sorted(images): 
        im = Image.open(i)
        im = im.resize((550,389),Image.ANTIALIAS)
        frames.append(im.copy())
        
    # Save frames/ stitched images as .gif
    frames[0].save(f'{save_file_path}', format='GIF', append_images=frames[1:], save_all=True,
                   duration=duration, loop=0)


# In[11]:


png_to_gif(path_to_images='Plots/Maps Pickup PNG/*.png', 
           save_file_path='Plots/pickup_heatmap.gif',
           duration=500)

