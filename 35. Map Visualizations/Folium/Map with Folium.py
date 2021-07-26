#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import folium
import json## Read and Understand the TopoJSON file


# ## Read and Understand the TopoJSON file

# In[2]:


with open('Json_Files\\India_States_2020_compressed_topo.json') as f:
  states_topo = json.load(f)


# In[3]:


states_topo.keys()


# In[4]:


states_topo['objects'].keys()


# In[5]:


states_topo['objects']['India_States_2020_compressed'].keys()


# In[6]:


states_topo['objects']['India_States_2020_compressed']['geometries'][0].keys()


# In[7]:


states_topo['objects']['India_States_2020_compressed']['geometries'][0]['properties'].keys()


# In[8]:


states_topo['objects']['India_States_2020_compressed']['geometries'][0]['properties']['state_name']


# ## Load the data and create the visualization

# In[9]:


df = pd.read_csv('Data/state_dummy_data_no_null.csv')
df.head()


# In[10]:


folium_map = folium.Map(location=[19, 80],
                        zoom_start=4,
                        tiles="CartoDB dark_matter")

folium.Choropleth(geo_data=states_topo,
             data=df, # my dataset
             columns=['st_nm','count'], 
             topojson='objects.India_States_2020_compressed',
             key_on='feature.properties.state_name', 
             fill_color='GnBu', fill_opacity=0.7, line_opacity=0.5).add_to(folium_map)

folium_map


# In[11]:


folium_map.save("HTML/Folium_Map.html")


# ## Bonus: Visualize any TopoJSON file without data

# In[12]:


with open('Json_Files\\India_States_2020_compressed_topo.json') as f:
  states_topo = json.load(f)

m = folium.Map(location=[19, 80],
                        zoom_start=4,
                        tiles="CartoDB dark_matter")
folium.TopoJson(states_topo,
             'objects.India_States_2020_compressed').add_to(m)

m


# In[13]:


m.save("HTML/Folium_Map1.html")

