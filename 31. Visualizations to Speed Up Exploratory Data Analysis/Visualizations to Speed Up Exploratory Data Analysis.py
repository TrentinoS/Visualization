
# ## Import Packages



import pandas as pd
import numpy as np
import math

import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style('whitegrid')


# ## Get a Convenient Dataset to Play With
# This is for demonstration purposes only. Skip this section when implementing these functions in your notebook with your dataframe.

# _Fetch the demonstration dataset and stick it in a pandas dataframe. There are 20,648 observations in this Sklearn dataset of California housing prices. The 8 feature columns reside in the dataset.data structure._




from sklearn.datasets import fetch_california_housing





dataset = fetch_california_housing()





df = pd.DataFrame(dataset.data,
                  columns=[dataset.feature_names]
                  )
df.head()





df.shape


# _Create the target column “price” (prices, in $ 000,000) which resides in the dataset.target structure. It happens to be placed into a multilevel column index, so I will need to flatten that to one level, as below. I also verified that there were no null values, just to be sure._




df['price'] = 100_000 * dataset.target
df.head()





df.isna().sum().sum()





df.columns





df.columns = df.columns.get_level_values(0)





df.columns


# ## Function: Half-masked Correlation Heatmap

# _There aren’t any non-numerical columns in this dataset, but most often, there will be plenty of data cleaning, binarizing, checking datatypes, etc. to do._
# 
# _Start with a quick look at the Pearson correlation coefficients. Visualizing on a heatmap is a nice way to go for this,and mask half of it with a white upper triangle._




# Required parameter: dataframe ... the reference pandas dataframe
# Optional parameters: title ... (string) chart title
#                      file  ... (string) path+filename if you want to save image


def half_masked_corr_heatmap(dataframe, title=None, file=None):
    plt.figure(figsize=(9,9))
    sns.set(font_scale=1)

    mask = np.zeros_like(dataframe.corr())
    mask[np.triu_indices_from(mask)] = True

    with sns.axes_style("white"):
        sns.heatmap(dataframe.corr(), mask=mask, annot=True, cmap='coolwarm')

    if title: plt.title(f'\n{title}\n', fontsize=18)
    plt.xlabel('')    # optional in case you want an x-axis label
    plt.ylabel('')    # optional in case you want a  y-axis label
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return





half_masked_corr_heatmap(df,
                         'CA Housing Price Data - Variable Correlations',
                         'Plots/Corr to Target.jpg')


# ## Function: Corr to a Target Variable (heat-spectrum)




# Required parameters: dataframe ... the reference pandas dataframe
#                      target ... (string) column name of the target variable

# Optional parameters: title ... (string) chart title
#                      file  ... (string) path+filename if you want to save image

def corr_to_target(dataframe, target, title=None, file=None):
    plt.figure(figsize=(4,6))
    sns.set(font_scale=1)
    
    sns.heatmap(dataframe.corr()[[target]].sort_values(target,
                                                ascending=False)[1:],
                annot=True,
                cmap='coolwarm')
    
    if title: plt.title(f'\n{title}\n', fontsize=18)
    plt.xlabel('')    # optional in case you want an x-axis label
    plt.ylabel('')    # optional in case you want a  y-axis label
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return





corr_to_target(df, 'price',
               'CA Housing Price Data - Corr to Price',
               'Plots/Corr to Price.jpg'
              )


# ## Function: Scatterplots of All Features vs. Target

# _Survey of scatterplots of each potential feature variable vs. the target is a typical next step. The function rotates continuously through this list of colors for each subplot in the feature list._




# Suptitle formatting adapted from Stackoverflow, Alexander McFarlane
# https://stackoverflow.com/questions/7066121/
#   how-to-set-a-single-main-title-above-all-the-subplots-with-pyplot/35676071

# N-across scatterplots of each feature vs. target ...
# Required parameters: dataframe ... the reference pandas dataframe
#                      target ... (string) column name of the target variable

# Optional parameters: title ... (string) chart title
#                      file  ... (string) path+filename if you want to save image


def gen_scatterplots(dataframe, target_column, list_of_columns, cols=1, file=None):
    rows      = math.ceil(len(list_of_columns)/cols)
    figwidth  = 5 * cols
    figheight = 4 * rows

    fig, ax = plt.subplots(nrows   = rows,
                           ncols   = cols,
                           figsize = (figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darkorange', 'g']

    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    ax = ax.ravel()         # Ravel turns a matrix into a vector... easier to iterate

    for i, column in enumerate(list_of_columns):
        ax[i].scatter(dataframe[column],
                      dataframe[target_column],
                      color=color_choices[i % len(color_choices)],
                      alpha = 0.1)

#           Individual subplot titles, optional
#             ax[i].set_title(f'{column} vs. {target_column}', fontsize=18)

        ax[i].set_ylabel(f'{target_column}', fontsize=14)
        ax[i].set_xlabel(f'{column}', fontsize=14)

    fig.suptitle('\nEach Feature vs. Target Scatter Plots', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    return




feature_cols = [col for col in df.columns if col != 'price']
gen_scatterplots(df, 'price',
                 feature_cols,
                 3,
                 'Plots/Feature Target Scatter Plots.jpg'
                )


# ## Function: N-across Histograms of Each Variable

# _What do the variable observations look like? Do things look normally distributed? Only a statsmodel normal test will give you a definitive answer, but visual inspection is always a good idea._




# N-across Histograms of each variable in the dataframe ...
# Required parameter: dataframe ... the reference pandas dataframe

# Optional parameters: cols ... no. of subplot columns across fig; default=1
#                      file  ... (string) path+filename if you want to save image

def gen_histograms(dataframe, cols=1, file=None):
    rows      = math.ceil(len(dataframe.columns)/cols)
    figwidth  = 5 * cols
    figheight = 4 * rows

    fig, ax = plt.subplots(nrows   = rows,
                           ncols   = cols,
                           figsize = (figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darkorange', 'g']
    ax = ax.ravel()         # Ravel turns a matrix into a vector... easier to iterate

    for i, column in enumerate(dataframe.columns):
        ax[i].hist(dataframe[column],
                      color=color_choices[i % len(color_choices)],
                      alpha = 1)
        
        ax[i].set_title(f'{dataframe[column].name}', fontsize=18)
        ax[i].set_ylabel('Observations', fontsize=14)
        ax[i].set_xlabel('', fontsize=14)
        
    fig.suptitle('\nHistograms for All Variables in Dataframe', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();

    return





gen_histograms(df, 3,
               'Plots/All var Histograms.jpg'
              )


# ## Function: Boxplots

:


# N-across boxplots of each variable in the dataframe ...
# Required parameter: dataframe ... the reference pandas dataframe

# Optional parameters: cols ... no. of subplot columns across fig; default=1
#                      file  ... (string) path+filename if you want to save image


def gen_boxplots(dataframe, cols=1, file=None):
    rows      = math.ceil(len(dataframe.columns)/cols)
    figwidth  = 5 * cols
    figheight = 4 * rows

    fig, ax = plt.subplots(nrows   = rows,
                           ncols   = cols,
                           figsize = (figwidth, figheight))
    
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    ax = ax.ravel()         # Ravel turns a matrix into a vector... easier to iterate

    for i, column in enumerate(dataframe.columns):
        ax[i].boxplot(dataframe[column])
        
        ax[i].set_title(f'{dataframe[column].name}', fontsize=18)
        ax[i].set_ylabel('', fontsize=14)
        ax[i].set_xlabel('', fontsize=14)
        ax[i].tick_params(labelbottom=False)
        
    fig.suptitle('\nBoxplots for All Variables in Dataframe', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();

    return





gen_boxplots(df, 3,
             'Plots/All Var Boxplots.jpg'
            )


# ## Function: N-across Line Charts

# _Line chart functions to create current CA Housing Prices dataset._



# N-across Line Charts of each variable in the dataframe ...
# Required parameter: dataframe ... the reference pandas dataframe

# Optional parameters: cols ... no. of subplot columns across fig; default=1
#                      file  ... (string) path+filename if you want to save image


def gen_linecharts(dataframe, cols=1, file=None):
    list_of_columns = list(dataframe.columns)
    rows      = math.ceil(len(list_of_columns)/cols)
    figwidth  = 5 * cols
    figheight = 4 * rows

    fig, ax = plt.subplots(nrows   = rows,
                           ncols   = cols,
                           figsize = (figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darkorange', 'g']

    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    ax = ax.ravel()         # Ravel turns a matrix into a vector... easier to iterate

    for i, column in enumerate(list_of_columns):
        ax[i].plot(dataframe[column],
                   color=color_choices[i % len(color_choices)])
        
        ax[i].set_title(f'{column}', fontsize=18)
        ax[i].set_ylabel(f'{column}', fontsize=14)
        
    fig.suptitle('\nLine Graphs for All Variables in Dataframe', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return





gen_linecharts(df, 3,
               'Plots/All Var Linecharts.jpg'
              )


# ## Function: N-across Line Charts with User-specified Rolling Average



# N-across Rolling Avg Line Charts of each variable in the dataframe ...
# Required parameters: dataframe ... the reference pandas dataframe
#                      roll_num ... periods over which to calc rolling avg

# Optional parameters: cols ... no. of subplot columns across fig; default=1
#                      file  ... (string) path+filename if you want to save image

def gen_linecharts_rolling(dataframe, roll_num, cols=1, file=None):
    list_of_columns = list(dataframe.columns)    
    rows      = math.ceil(len(list_of_columns)/cols)
    figwidth  = 5 * cols
    figheight = 4 * rows
    
    dataframe = dataframe.rolling(roll_num).mean()

    fig, ax = plt.subplots(nrows   = rows,
                           ncols   = cols,
                           figsize = (figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darkorange', 'g']

    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    ax = ax.ravel()         # Ravel turns a matrix into a vector... easier to iterate

    for i, column in enumerate(list_of_columns):
        ax[i].plot(dataframe[column],
                   color=color_choices[i % len(color_choices)])
        
        ax[i].set_title(f'{column}', fontsize=18)
        ax[i].set_ylabel(f'{column}', fontsize=14)
        ax[i].set_xlabel('Time', fontsize=14)
        
    fig.suptitle('\nRolling Avg. Line Graphs (all vars)', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return




gen_linecharts_rolling(df, 150, 3,
                      'Plots/All Var Rolling Line Charts.jpg'
                      )

