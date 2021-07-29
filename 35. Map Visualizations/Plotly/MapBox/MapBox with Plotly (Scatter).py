#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime, timedelta
import plotly.express as px
import pandas as pd


# In[2]:


#Load and prepare data
df = pd.read_csv('Data/scatter_dummy_data.csv')
df['day'] = pd.to_datetime(df['day'],format="%d-%m-%Y")
df['dt_str'] = df['day'].apply(lambda x: x.strftime("%d-%b-%Y"))
df.head()


# In[3]:


#Trim and sort data
date1 = datetime(2020,3,1)
date2 = datetime(2020,3,10)
df = df[(df['day'] >= date1) & (df['day'] <= date2)]
df.sort_values(by = ['day'], inplace=True)
df['n_trip_scaled']=df['n_trip_on'].apply(lambda x: x/500)


# In[4]:


fig = px.scatter_mapbox(df, lat="start_lat", 
                        lon="start_lon", 
                        hover_name="day", 
                        hover_data=["device_fk_id","n_trip_on"],
                        color_discrete_sequence=["yellow"], 
                        zoom=3, height=550, width=500, 
                        animation_frame="dt_str", 
                        size='n_trip_scaled',size_max=10,)
fig.update_layout(
    mapbox_style="carto-darkmatter")
#Adjust pitch and bearing to adjust the rotation
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, 
                  mapbox=dict(
                      pitch=60,
                      bearing=30
                  ))
fig.show()


# In[5]:


fig.write_html("HTML/Plotly_Mapbox_Scatter.html")

