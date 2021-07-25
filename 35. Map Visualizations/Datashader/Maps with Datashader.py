#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dask.dataframe as dd
import datashader as ds
import plotly.express as px


# In[2]:


#Datashader is generally used for large data sets. The CSV file that will be used here is about 2 GB large (74 million+ locations).
#You can download it from here: https://drive.google.com/file/d/1HJq4hSkQbNGzgHv48Q7Vce6omy6wMAHF/view?usp=sharing
df = dd.read_csv('Data/lat_lon_data.csv')


# In[3]:


df.head()


# In[4]:


#Remove any unwanted columns
df = df[['latitude','longitude']]

#Clean data, remove any out-of-bounds points
df = df[df['latitude'] > 6]
df = df[df['latitude'] < 38]
df = df[df['longitude'] > 68]
df = df[df['longitude'] < 98]


# In[5]:


cvs = ds.Canvas(plot_width=1000, plot_height=1000)
agg = cvs.points(df, x='longitude', y='latitude')
# agg is an xarray object, see http://xarray.pydata.org/en/stable/ for more details
coords_lat, coords_lon = agg.coords['latitude'].values, agg.coords['longitude'].values
# Corners of the image, which need to be passed to mapbox
coordinates = [[coords_lon[0], coords_lat[0]],
               [coords_lon[-1], coords_lat[0]],
               [coords_lon[-1], coords_lat[-1]],
               [coords_lon[0], coords_lat[-1]]]


# In[6]:


from matplotlib.cm import hot, viridis, Blues, plasma, magma, Greens
import datashader.transfer_functions as tf
img=(tf.shade(agg, cmap = hot, how='log'))[::-1].to_pil() #pil stands for Python Image Library


# In[7]:


# #Alternatively, if you want to use the fire colorset, uncomment the below lines
# from colorcet import fire
# import datashader.transfer_functions as tf
# img = tf.shade(agg, cmap=fire, alpha = 255,how='log')[::-1].to_pil()


# In[8]:


fig = px.scatter_mapbox(df.tail(1), lat='latitude', lon='longitude', zoom=4,width=1000, height=1000)
# Add the datashader image as a mapbox layer image
fig.update_layout(mapbox_style="carto-darkmatter",
                 mapbox_layers = [
                {
                    "sourcetype": "image",
                    "source": img,
                    "coordinates": coordinates
                }]
)
fig.show()


# In[9]:


#Export plot as html
fig.write_html("HTML/Datashader_Map.html")

