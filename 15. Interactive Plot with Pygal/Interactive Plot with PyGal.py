import pygal

bar_chart = pygal.Bar()

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
fact_list = [factorial(i) for i in range(11)]

from IPython.display import display, HTML
base_html = """
<!DOCTYPE html>
<html>
  <head>
  <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
  <script type="text/javascript" src="https://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js""></script>
  </head>
  <body>
    <figure>
      {rendered_chart}
    </figure>
  </body>
</html>
"""

bar_chart = pygal.Bar(height=400)
bar_chart.add('Factorial', fact_list)
display(HTML(base_html.format(rendered_chart=bar_chart.render(is_unicode=True))))

## Import Data
import pygal
import pandas as pd
data = pd.read_csv('Data/us-counties.csv')
data.head()
data.sample(10)


## Bar Chart
mean_per_state = data.groupby('state')['cases'].mean()
barChart = pygal.Bar(height=400)
[barChart.add(x[0], x[1]) for x in mean_per_state.items()]
display(HTML(base_html.format(rendered_chart=barChart.render(is_unicode=True))))

#Import needed libraries
import pygal
import pandas as pd
#Parse the dataframe
data = pd.read_csv("Data/us-counties.csv") 
#Get the mean number of cases per states
mean_per_state = data.groupby('state')['cases'].mean()
#Draw the bar chart
barChart = pygal.Bar(height=400)
[barChart.add(x[0], x[1]) for x in mean_per_state.items()]
display(HTML(base_html.format(rendered_chart=barChart.render(is_unicode=True))))


## Tree Map
sort_by_cases = data.sort_values(by=['cases'],ascending=False).groupby(['state'])['cases'].apply(list)
top_10_states = sort_by_cases[:10]
treemap = pygal.Treemap(height=400)
[treemap.add(x[0], x[1][:10]) for x in top_10_states.items()]
display(HTML(base_html.format(rendered_chart=treemap.render(is_unicode=True))))

#Import needed libraries
import pygal
import pandas as pd
#Parse the dataframe
data = pd.read_csv("Data/us-counties.csv") 
#Sort states by cases count
sort_by_cases = data.sort_values(by=['cases'],ascending=False).groupby(['state'])['cases'].apply(list)
#Get the top 10 states with the highest number of cases
top_10_states = sort_by_cases[:10]
#Draw the treemap
treemap = pygal.Treemap(height=400)
[treemap.add(x[0], x[1][:10]) for x in top_10_states.items()]
display(HTML(base_html.format(rendered_chart=treemap.render(is_unicode=True))))

#Get the cases by county for all states
cases_by_county = data.sort_values(by=['cases'],ascending=False).groupby(['state'], axis=0).apply(
    lambda x : [{"value" : l, "label" : c } for l, c in zip(x['cases'], x['county'])])
cases_by_county= cases_by_county[:10]
#Create a new dictionary that contains the cleaned up version of the data

clean_dict = {}
start_dict= cases_by_county.to_dict()
for key in start_dict.keys():
    values = []
    labels = []
    county = []
    for item in start_dict[key]:
        if item['label'] not in labels:
            labels.append(item['label'])
            values.append(item['value'])
        else:
            i = labels.index(item['label'])
            values[i] += item['value']
    
    for l,v in zip(labels, values):
        county.append({'value':v, 'label':l})
    clean_dict[key] = county
#Convert the data to Pandas series to add it to the treemap

new_series = pd.Series(clean_dict)


treemap = pygal.Treemap(height=200)
[treemap.add(x[0], x[1][:10]) for x in new_series.iteritems()]
display(HTML(base_html.format(rendered_chart=treemap.render(is_unicode=True))))

#Import needed libraries
import pygal
import pandas as pd
#Parse the dataframe
data = pd.read_csv("Data/us-counties.csv") 
#Get the cases by county for all states
cases_by_county = data.sort_values(by=['cases'],ascending=False).groupby(['state'], axis=0).apply(
    lambda x : [{"value" : l, "label" : c } for l, c in zip(x['cases'], x['county'])])
cases_by_county= cases_by_county[:10]
#Create a new dictionary that contains the cleaned up version of the data
clean_dict = {}
start_dict= cases_by_county.to_dict()
for key in start_dict.keys():
    values = []
    labels = []
    county = []
    for item in start_dict[key]:
        if item['label'] not in labels:
            labels.append(item['label'])
            values.append(item['value'])
        else:
            i = labels.index(item['label'])
            values[i] += item['value']
    
    for l,v in zip(labels, values):
        county.append({'value':v, 'label':l})
    clean_dict[key] = county
#Convert the data to Pandas series to add it to the treemap
new_series = pd.Series(clean_dict)
#Draw the treemap
treemap = pygal.Treemap(height=200)
[treemap.add(x[0], x[1][:10]) for x in new_series.iteritems()]
display(HTML(base_html.format(rendered_chart=treemap.render(is_unicode=True))))


## Pie Chart 
#Import needed libraries
import pygal
import pandas as pd
#Parse the dataframe
data = pd.read_csv("Data/us-counties.csv") 
#Get the mean number of cases per states
sort_by_cases = data.sort_values(by=['cases'],ascending=False).groupby(['state'])['cases'].apply(list)
#Draw the bar chart
pi_chart = pygal.Pie(height=400)
#Get the top 10 states
first10 = list(sort_by_cases.items())[:10]
[pi_chart.add(x[0], x[1]) for x in first10]
display(HTML(base_html.format(rendered_chart=pi_chart.render(is_unicode=True))))

## Gauge chart
gauge = pygal.SolidGauge(inner_radius=0.70)
[gauge.add(x[0], [{"value" : x[1] * 100}] ) for x in mean_per_state.head().iteritems()]
display(HTML(base_html.format(rendered_chart=gauge.render(is_unicode=True))))
gauge = pygal.Gauge(human_readable=True)
[gauge.add(x[0], [{"value" : x[1] * 100}] ) for x in mean_per_state.head().iteritems()]
display(HTML(base_html.format(rendered_chart=gauge.render(is_unicode=True))))

#Import needed libraries
import pygal
import pandas as pd
#Parse the dataframe
data = pd.read_csv("Data/us-counties.csv") 
#Get the mean number of cases per states
mean_per_state = data.groupby('state')['cases'].mean()
#The donut shape gauge chart
gauge = pygal.SolidGauge(inner_radius=0.70)
[gauge.add(x[0], [{"value" : x[1] * 100}] ) for x in mean_per_state.head().iteritems()]
display(HTML(base_html.format(rendered_chart=gauge.render(is_unicode=True))))
#The needle shape gquge chart
gauge = pygal.Gauge(human_readable=True)
[gauge.add(x[0], [{"value" : x[1] * 100}] ) for x in mean_per_state.head().iteritems()]
display(HTML(base_html.format(rendered_chart=gauge.render(is_unicode=True))))

from pygal.style import *

from pygal.style import Style
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  font_family = 'googlefont:Bad Script',
  colors=('#05668D', '#028090', '#00A896', '#02C39A', '#F0F3BD'))