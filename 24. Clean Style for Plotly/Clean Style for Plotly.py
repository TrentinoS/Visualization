import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

df = pd.DataFrame({'Animal':['Cat', 'Dog','Fish', 'Lemur'],
                  'Legs': ['4','4','0','2'],
                  'Height':[30, 80, 7, 42]})
df.head()

px.bar(df,
      x='Animal',
      y='Height',
      color='Legs',
      title='The heights of various animals at my zoo.')

custom_template = {
    "layout": go.Layout(
        font={
            "family": "Nunito",
            "size": 12,
            "color": "#707070",
        },
        title={
            "font": {
                "family": "Lato",
                "size": 18,
                "color": "#1f1f1f",
            },
        },
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        colorway=px.colors.qualitative.G10,
    )
}

px.bar(df,
      x='Animal',
      y='Height',
      color='Legs',
      title='The heights of various animals at my zoo.',
      template=custom_template)

def format_title(title, subtitle=None, subtitle_font_size=14):
    title = f'<b>{title}</b>'
    if not subtitle:
        return title
    subtitle = f'<span style="font-size: {subtitle_font_size}px;">{subtitle}</span>'
    return f'{title}<br>{subtitle}'


px.bar(
    df, 
    x="Animal", 
    y="Height", 
    color="Legs", 
    title=format_title("Animal Height/Length", "data collected at my local zoo during 2020"), 
    template=custom_template
)

