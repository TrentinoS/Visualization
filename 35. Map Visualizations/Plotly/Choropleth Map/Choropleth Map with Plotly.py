#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import json
from osgeo import ogr
import geopandas as gpd


# ## Get GeoJSON from shapefile

# In[2]:


#Method 1: Using OGR

#We used compressed shapefiles obtained from mapshaper.org
driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = 'Shape_Files\\India_States_2020_compressed\\India_states.shp'
data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'FeatureCollection',
    'features': []
    }

lyr = data_source.GetLayer(0)
for feature in lyr:    
    fc['features'].append(feature.ExportToJson(as_object=True))

with open('Json_Files\\India_States_2020_compressed.json', 'w') as f:
    json.dump(fc, f)


# In[3]:


# #Method 2: Using geopandas

# # set the filepath and load
# fp = "shape_files\\India_States_2020_compressed\\India_States.shp"
# #reading the file stored in variable fp
# map_df = gpd.read_file(fp)
# #Export it as GeoJSON
# map_df.to_file("json_files\\India_States_2020_compressed_gpd.json", driver='GeoJSON')


# ## Open, understand and compress the GeoJSON

# In[4]:


with open('Json_Files\\India_States_2020_compressed.json') as f:
  India_states = json.load(f)


# In[5]:


#Have a look at the features
India_states["features"][0].keys()


# In[6]:


#type says that it is a 'Feature'
#geometry contains the coordinates for that feature
#properties contains the state name
#id is the index of the feature
#Let us check the state name for feature 0
India_states["features"][0]['properties']


# In[7]:


#Let us look at just one location:
India_states["features"][0]['geometry']['coordinates'][0][0][0]


# ## Load the data and create the visualization

# In[8]:


#Load the csv file and check its contents. Make sure that there is one entry corresponding to each state in the geojson. 
df = pd.read_csv('Data/state_dummy_data_no_null.csv')
df.head()


# In[9]:


max_value = df['count'].max()
fig = px.choropleth(df, geojson=India_states, locations='st_nm', color='count',
                           color_continuous_scale="Viridis",
                           range_color=(0, max_value),
                           featureidkey="properties.state_name",
                           projection="mercator"
                          )

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[10]:


fig.write_image("Images\\India_Choropleth.png")
fig.write_html('HTML\\Plotly_Choropleth_Map.html')


# In[11]:


#To make sure that you have entries corresponding to all states in geo-json, you can simply print out 
#the state names of the geojson
#You many need to rename some states/UT of the df according to the geojson
#For example, the geo-json has New Delhi named as 'DELHI'
for i in range(0, len(India_states["features"])):
    print(India_states["features"][i]["properties"]["state_name"])

