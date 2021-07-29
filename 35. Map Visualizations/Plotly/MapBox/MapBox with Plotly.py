#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import shapefile as shp
from datetime import datetime, timedelta
import geopandas as gpd
import json
import plotly.express as px


# # Get GeoJSON from GeoPandas DataFrame

# In[2]:


# set the filepath and load
fp = "Shape_Files\\India_Districts_2020_compressed\\India_Districts_2020.shp"
#reading the file stored in variable fp
map_df = gpd.read_file(fp)
# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
map_df.head()


# In[3]:


map_df_up = map_df[map_df['stname'] == 'UTTAR PRADESH']
map_df_up.to_file("json_files\\up_districts_2020_compressed.json", driver='GeoJSON')


# # Prepare GeoJSON

# In[4]:


with open('Json_Files\\up_districts_2020_compressed.json') as f:
  up_districts = json.load(f)


# In[5]:


#Check the keys of the json
up_districts["features"][0].keys()


# In[6]:


#We have the first level keys. The properties key is what we are interested in. Let's dig deeper there
#We'll see that almost all the keys corresponding to the columns in the geopandas object are present here.
up_districts["features"][0]['properties'].keys()


# In[7]:


#Let us check the precision of the coordinates
up_districts["features"][0]['geometry']['coordinates'][0][0]


# In[8]:


#Round off the locations to 2 decimal places (about 1.1 km accuracy)
for i in range(0, len(up_districts["features"])):
    for j in range(0,len(up_districts["features"][i]['geometry']['coordinates'])):
        try:
            up_districts["features"][i]['geometry']['coordinates'][j] = np.round(np.array(up_districts["features"][i]['geometry']['coordinates'][j]),2)
        except:
            print(i,j)


# In[9]:


#Let us check the precision of the coordinates
up_districts["features"][0]['geometry']['coordinates'][0][0]


# # Load and Process Data

# In[10]:


df = pd.read_csv('Data\\UP_dummy_data.csv')
df.head()


# In[11]:


df['Installed On'] = df['Installed On'].apply(lambda x: x.split('T')[0])
df['Installed On'] = pd.to_datetime(df['Installed On'],format="%Y-%m-%d")
df.sort_values(by=['Installed On'],inplace=True)


# In[12]:


#Get only district field from shape file
df_d = map_df_up[['dtname']]
df_d.head()


# In[13]:


#Generate the cumulative dataframe
date_min = df['Installed On'].min()
df_final = pd.DataFrame(columns=['dtname','count','date'])

#Generate cumulative data for for each month (approximated as 30 days), starting from date_min, and upto 6 months
for i in range(0,180,30):
    date = date_min+timedelta(days=i)
    #Get the cumulative df
    df_c = df[df['Installed On'] <= date]
    
    #Create a temporary df to store the value_counts
    df_t = df_c['installation_district'].value_counts().to_frame()
    df_t.reset_index(inplace=True)
    df_t.columns = ['dist','count']
    merged = df_d.set_index('dtname').join(df_t.set_index('dist'))
#     merged['count'].fillna(0,inplace=True)
    merged.reset_index(inplace=True)
    merged['date'] = date
    df_final=pd.concat([df_final,merged], ignore_index=True)

df_final['dt_str'] = df_final['date'].apply(lambda x: x.strftime("%d-%b-%Y"))


# # Generate the Visualization

# In[14]:


max_count = df_final['count'].max()
fig = px.choropleth_mapbox(df_final, geojson=up_districts, locations='dtname', color='count',
                           color_continuous_scale="Viridis",
                           range_color=(0, max_count),
                           featureidkey="properties.dtname",mapbox_style="carto-positron",
                           opacity=0.5,center = {"lat": 26.8467, "lon": 80.9462}, zoom=5,
                          animation_frame='dt_str')

fig.update_geos(fitbounds="locations",visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},)

fig.show()


# In[15]:


fig.write_html('HTML\\Plotly_Mapbox_Choropleth.html')

