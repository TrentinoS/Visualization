#!/usr/bin/env python
# coding: utf-8

# ## Importing Packages

# In[1]:


import pandas as pd
import numpy as np
import re
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_context('talk')


# ## Loading Data

# In[2]:


#csv file
df_avatar = pd.read_csv('Data/avatar.csv', engine='python')
df_avatar.drop('Unnamed: 0', axis=1, inplace=True)
#droping scenes description
index_scene = df_avatar[df_avatar['character']=='Scene Description'].index.values
df_avatar.drop(index_scene, axis=0, inplace=True)


# ### Lines per top character

# In[3]:


df_avatar_lines = df_avatar.groupby('character').count().sort_values(by=['character_words'], ascending=False)[:10]
top_character_names = df_avatar_lines.reset_index()['character'].values
df_avatar_lines[['character_words']]


# ### Lines per character in each season / Top character per book

# In[4]:


df_top_characters = df_avatar[df_avatar['character'].isin(top_character_names)]
df_top_characters = df_top_characters.groupby(['character', 'book']).count().sort_values(by=['character_words'], ascending=False).reset_index()
df_top_characters = df_top_characters[['character', 'book','character_words']]


# ### Barplot

# In[5]:


import chart_studio
import chart_studio.plotly as py
from PIL import Image

import plotly.express as px
import plotly.graph_objects as go

fig = px.bar(df_top_characters, x='character_words', y= 'character', orientation = 'h', 
             color=df_top_characters['book'], title='Top 10 Avatar Characters Number of Lines', 
             template = 'plotly_white',
             color_discrete_map={'Fire':'#C43A3A', 'Water':'#3A7FC4', 'Earth':'#BB653B'},)
fig.update_xaxes(title_text='Number of lines')
fig.update_yaxes(title_text='Characters')

#Add pics
fig.add_layout_image(
    dict(
        source="https://vignette.wikia.nocookie.net/avatar/images/1/12/Azula.png",
        x=0.2,
        y=0.9,
    ))
fig.add_layout_image(
    dict(
        source="https://vignette.wikia.nocookie.net/avatar/images/4/46/Toph_Beifong.png",
        x=0.35,
        y=0.8,
    ))#ioph
fig.add_layout_image(
    dict(
        source=Image.open('Plots/suki.png'),
        x=0.14,
        y=0.7,
    ))#suki
fig.add_layout_image(
    dict(
        source=Image.open('Plots/jet.png'),
        x=0.16,
        y=0.6,
    ))#jet
fig.add_layout_image(
 dict(
        source=Image.open('Plots/Zhao.png'),
        x=0.14,
       y=0.5,
    ))#zhao
fig.add_layout_image(
    dict(
        source="https://vignette.wikia.nocookie.net/avatar/images/c/c1/Iroh_smiling.png",
        x=0.25,
        y=0.4,
    ))#iroh
fig.add_layout_image(
    dict(
        source="https://vignette.wikia.nocookie.net/avatar/images/4/4b/Zuko.png",
        x=0.50,
        y=0.3,
    ))

fig.add_layout_image(
    dict(
        source="https://vignette.wikia.nocookie.net/avatar/images/c/cc/Sokka.png",
        x=0.96,
        y=0.2,
    ))
fig.add_layout_image(
    dict(
        source="https://static.wikia.nocookie.net/loveinterest/images/c/cb/Avatar_Last_Airbender_Book_1_Screenshot_0047.jpg",
        x=0.85,
        y=0.11,
    ))
fig.add_layout_image(
    dict(
        source="https://comicvine1.cbsistatic.com/uploads/scale_small/11138/111385676/7212562-5667359844-41703.jpg",
        x=1.03,
        y=0.03,
    ))
fig.update_layout_images(dict(
        xref="paper",
        yref="paper",
        sizex=0.09,
        sizey=0.09,
        xanchor="right",
        yanchor="bottom"
))

fig.update_layout(
    font=dict(
        size=15,
    )
)
fig.show()


# # Wordclouds

# In[6]:


df_water = df_avatar[df_avatar['book']=='Water']
df_earth = df_avatar[df_avatar['book']=='Earth']
df_fire = df_avatar[df_avatar['book']=='Fire']
#clean
water_text = ' '.join(df_water['character_words'].values).lower()
earth_text = ' '.join(df_earth['character_words'].values).lower()
fire_text = ' '.join(df_fire['character_words'].values).lower()


# ### Most repeater words

# In[7]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text 
import scipy.sparse

cv = CountVectorizer() # max_df=0.9
cv.fit(df_water['character_words'])
cv = CountVectorizer().fit(df_water['character_words'])
bag_of_words = cv.transform(df_water['character_words'])
sum_words = bag_of_words.sum(axis=0) 
words_freq = [(word, sum_words[0, idx]) for word, idx in cv.vocabulary_.items()]
words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)


# In[8]:


# list(map(lambda x:x.lower(), list(top_character_names)))
character_names = [i.lower() for i in list(top_character_names)]
character_names = set(character_names)


# ### StyleCloud

# In[9]:


import stylecloud
from wordcloud import STOPWORDS

my_custom_stopwords = character_names | STOPWORDS
#water -> fas fa-tint  ... #3A7FC4
#earth -> fas fa-globe-americas #BB653B #9A3F12
#fire -> fas fa-fire fas fa-fire-alt... #C43A3A
stylecloud.gen_stylecloud(earth_text, palette="cmocean.sequential.Matter_16", 
                          background_color="white", icon_name= 'fas fa-tint',
                          colors=['#3A7FC4', '#3A7FC4', '#3A7FC4'], stopwords=STOPWORDS,
                          custom_stopwords = my_custom_stopwords, collocations=False)


# ### WordCloud

# In[10]:


from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
shape = np.array(Image.open('Plots/fire.png'))
wc = WordCloud(background_color = 'white', mask=shape, collocations=False, width=600, height=300,
              stopwords=my_custom_stopwords)
wc.generate(fire_text)

def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,70%%, %d%%)" % np.random.randint(49,50))

image_colors = ImageColorGenerator(shape)
wc.recolor(color_func=grey_color_func)
plt.figure(figsize=(20,10))
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file("Plots/fire.jpg")
("")


# ### My cabbages!

# In[11]:


#My Cabbages!
df_avatar[df_avatar['character_words'].str.contains('cabbages')]
#zuko's honor


# ### Dialogue vs IMDB

# In[12]:


#preparing data
df_avatar['tokens'] = df_avatar['character_words'].apply(lambda x:len(x.split(' ')))
df_scatter = pd.concat([df_avatar[['book', 'chapter', 'tokens']].groupby('chapter').sum(), 
           df_avatar[['book', 'chapter', 'imdb_rating']].drop_duplicates(['chapter']).set_index('chapter')],
         axis=1)

df_scatter.reset_index(inplace=True)
df_scatter.rename(columns={'index':'chapter'}, inplace=True)

#Static plot
fig, ax = plt.subplots(figsize=(15, 8))
ax = sns.scatterplot(x='tokens', y='imdb_rating', data=df_scatter, hue='book',
                    s=100, palette='deep')
plt.savefig('Plots/Dialogue.jpg')


# In[13]:


# Dynamic/Interactive plot (Plotly)
fig = px.scatter(df_scatter, x='tokens', y= 'imdb_rating', color='book', hover_name='chapter',
                  title='IMDb Ratings vs Number of Spoken Words', template = 'plotly_white',
                  color_discrete_map={'Fire':'#C43A3A', 'Water':'#3A7FC4', 'Earth':'#BB653B'},
                 )
fig.update_xaxes(title_text='Number of Spokens Words')
fig.update_yaxes(title_text='IMDb Rating')
fig.update_traces(marker=dict(size=12,
                               line=dict(width=2,
                                         color='DarkSlateGrey')),
                   selector=dict(mode='markers'))
fig.update_layout(
     font=dict(
         size=13,
     )
 )
fig.show()


# ### Sentiment Analysis

# In[14]:


import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[15]:


# top_character_names
df_character_sentiment = df_avatar[df_avatar['character'].isin(top_character_names)]
df_character_sentiment = df_character_sentiment[['character', 'character_words']]

sid = SentimentIntensityAnalyzer()
df_character_sentiment.reset_index(inplace=True, drop=True)
df_character_sentiment[['neg', 'neu', 'pos', 'compound']] = df_character_sentiment['character_words'].apply(sid.polarity_scores).apply(pd.Series)##


# In[16]:


#data 
df_character_sentiment = df_character_sentiment.groupby('character').mean().round(3).sort_values('pos', ascending=True)
df_character_sentiment.reset_index(inplace=True)
n = len(df_character_sentiment['pos'])
X = np.arange(n)

#bar plot
fig = plt.figure(figsize = (17, 12))
plt.barh(X, df_character_sentiment['pos'], facecolor='#9999ff', edgecolor='white')
plt.barh(X, -df_character_sentiment['neg'], facecolor='#ff9999', edgecolor='white')

plt.rcParams.update({'font.size':13})
plt.xlim([-.16,.22])
plt.yticks(ticks=X, labels=df_character_sentiment['character'], rotation='0')

plt.xlabel('Senitment Score')
plt.title('Average Sentiment scores of Avatar characters')
plt.legend(('Positive Sentiment','Negative Sentiment'))
plt.grid(False)
plt.savefig('Plots/sentiment.jpg', bbox_inches='tight')
plt.show()


# ### Heatmap: Who speaks to whom? 

# In[17]:


df_who_speaks = df_avatar.sort_values(['id'])
list_who_speaks = list(df_who_speaks['character'].values)
pair_characters = [list_who_speaks[i:i+2] for i in range(0,len(list_who_speaks),1)]
pair_characters.pop(-1)
pairs=[]
for i in pair_characters:
    pairs.append('-'.join(i))


# In[18]:


count_elements = dict((i, pairs.count(i)) for i in set(pairs))


# In[19]:


data_heatmap = sorted(count_elements.items(), key=lambda x:x[1], reverse=True)
data_heatmap = dict(data_heatmap)

x_list = [i.split('-')[0] for i in data_heatmap]
y_list = [i.split('-')[1] for i in data_heatmap]
z_list = [data_heatmap[i] for i in data_heatmap]

x_array = np.array(x_list)
y_array = np.array(y_list)
z_array = np.array(z_list)

df = pd.DataFrame.from_dict(np.array([x_array,y_array,z_array]).T)
df = df[df[0].isin(top_character_names)]
df = df[df[1].isin(top_character_names)]
df.columns = ['X_value','Y_value','Z_value']
df['Z_value'] = pd.to_numeric(df['Z_value'])

conditions = [df['X_value']==df['Y_value'],
              df['X_value']!=df['Y_value']]
values = [0, df['Z_value']]

df['Z_value'] = np.select(conditions, values)

####Scale
df['scale'] = np.log(df['Z_value']+1)
pivotted= df.pivot('Y_value','X_value','scale')

pivotted = pivotted[list(top_character_names[:15])]
pivotted = pivotted.reindex(list(top_character_names[:15]))
pivotted = pivotted.T #rows speak to columns
pivotted = pivotted.fillna(0)
pivotted

#Colors
#RdBu #YlGnBu #sns.cm.rocket

#HEATMAP
fig, ax = plt.subplots(1, 1, figsize = (15,8))
ax = sns.heatmap(pivotted,cmap='YlGnBu_r', cbar_kws={'ticks':[]})
ax.set_ylabel('')    
ax.set_xlabel('')
fig.tight_layout()
fig.savefig('Plots/heatmap.jpg')

