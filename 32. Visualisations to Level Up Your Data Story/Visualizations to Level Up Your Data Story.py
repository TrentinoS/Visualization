# # 1. Animations



import plotly.express as px
from vega_datasets import data
df = data.disasters()
df = df[df.Year > 1990]
fig = px.bar(df,
             y="Entity",
             x="Deaths",
             animation_frame="Year",
             orientation='h',
             range_x=[0, df.Deaths.max()],
             color="Entity")
# improve aesthetics (size, grids etc.)
fig.update_layout(width=1000,
                  height=800,
                  xaxis_showgrid=False,
                  yaxis_showgrid=False,
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  title_text='Evolution of Natural Disasters',
                  showlegend=False)
fig.update_xaxes(title_text='Number of Deaths')
fig.update_yaxes(title_text='')
fig.show()


# In[2]:


import plotly.express as px
df = px.data.gapminder()
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    range_x=[100, 100000],
    range_y=[25, 90],

    #   color_continuous_scale=px.colors.sequential.Emrld
)
fig.update_layout(width=1000,
                  height=800,
                  xaxis_showgrid=False,
                  yaxis_showgrid=False,
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)')


# # 2. Sunburst Charts

# _Sunburst charts are a great way to visualise your group by statements. If you want to break down a given quantity through one or multiple categorical variables, go for a sunburst chart._

# In[3]:


import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
df = px.data.tips()
fig = go.Figure(go.Sunburst(
    labels=["Female", "Male", "Dinner", "Lunch", 'Dinner ', 'Lunch '],
    parents=["", "", "Female", "Female", 'Male', 'Male'],
    values=np.append(
        df.groupby('sex').tip.mean().values,
        df.groupby(['sex', 'time']).tip.mean().values),
    marker=dict(colors=px.colors.sequential.Emrld)),
                layout=go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)'))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0),
                  title_text='Tipping Habbits Per Gender, Time and Day')
fig.show()


# In[4]:


import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
df = px.data.tips()
fig = go.Figure(go.Sunburst(labels=[
    "Female", "Male", "Dinner", "Lunch", 'Dinner ', 'Lunch ', 'Fri', 'Sat',
    'Sun', 'Thu', 'Fri ', 'Thu ', 'Fri  ', 'Sat  ', 'Sun  ', 'Fri   ', 'Thu   '
],
                            parents=[
                                "", "", "Female", "Female", 'Male', 'Male',
                                'Dinner', 'Dinner', 'Dinner', 'Dinner',
                                'Lunch', 'Lunch', 'Dinner ', 'Dinner ',
                                'Dinner ', 'Lunch ', 'Lunch '
                            ],
                            values=np.append(
                                np.append(
                                    df.groupby('sex').tip.mean().values,
                                    df.groupby(['sex',
                                                'time']).tip.mean().values,
                                ),
                                df.groupby(['sex', 'time',
                                            'day']).tip.mean().values),
                            marker=dict(colors=px.colors.sequential.Emrld)),
                layout=go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)'))
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0),
                  title_text='Tipping Habbits Per Gender, Time and Day')

fig.show()


# # 3. Parallel Categories

# _Another great way to explore relationships between categorical variables is this flowchart. You can drag and drop, highlight and explore values on-the-go which is excellent for presentations._

# In[5]:


import plotly.express as px
from vega_datasets import data
import pandas as pd
df = data.movies()
df = df.dropna()
df['Genre_id'] = df.Major_Genre.factorize()[0]
fig = px.parallel_categories(
    df,
    dimensions=['MPAA_Rating', 'Creative_Type', 'Major_Genre'],
    color="Genre_id",
    color_continuous_scale=px.colors.sequential.Emrld,
)
fig.show()


# # 4. Parallel Coordinates

# _Parallel coordinates plot is the continuous version of the plot above. Here, each chord represents a single observation. This is a great tool for spotting outliers (single threads isolated from the rest of the data), clusters, trends and redundant variables (e.g. if two variables have similar values for each observation, they’ll lie on a horizontal line and indicate redundancy)._

# In[6]:


import plotly.express as px
from vega_datasets import data
import pandas as pd
df = data.movies()
df = df.dropna()
df['Genre_id'] = df.Major_Genre.factorize()[0]
fig = px.parallel_coordinates(
    df,
    dimensions=[
        'IMDB_Rating', 'IMDB_Votes', 'Production_Budget', 'Running_Time_min',
        'US_Gross', 'Worldwide_Gross', 'US_DVD_Sales'
    ],
    color='IMDB_Rating',
    color_continuous_scale=px.colors.sequential.Emrld)
fig.show()


# # 5. Gauge Charts and Indicators

# _Gauge charts merely serve for aesthetics. They’re a great way to report some success metrics or KPIs and relate them to your target._
# 
# _Indicators are quite useful in business and consultancy context. They complement your visuals with textual marks that grab your audience’s attention and communicate your growth metrics._

# In[7]:


import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 4.3,
    mode = "gauge+number+delta",
    title = {'text': "Success Metric"},
    delta = {'reference': 3.9},
    gauge = {'bar': {'color': "lightgreen"},
        'axis': {'range': [None, 5]},
             'steps' : [
                 {'range': [0, 2.5], 'color': "lightgray"},
                 {'range': [2.5, 4], 'color': "gray"}],
          }))
fig.show()


# In[8]:


import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
    title = {'text': "Success Metric"},
     mode = "number+delta",
    value = 300,
    delta = {'reference': 160}))
fig.show()


fig = go.Figure(go.Indicator(
     title = {'text': "Success Metric"},
    mode = "delta",
    value = 40,
 delta = {'reference': 160}))
fig.show()

