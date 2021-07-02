import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import hvplot.pandas
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')

from bokeh.models.formatters import DatetimeTickFormatter
dtf = DatetimeTickFormatter( days = '%m-%Y', months = '%m-%Y' , years = '%m-%Y')

mrr = pd.read_csv('Data/mrr.csv', index_col = 'sub_id')

user_table = pd.read_csv( 'Data/user.csv')

mrr.columns = pd.to_datetime( mrr.columns )
user_table['sub_start_date'] =  pd.to_datetime(user_table['sub_start_date'] )
user_table['sub_end_date'] = pd.to_datetime(user_table['sub_end_date'] )

MAX_DATE = mrr.columns[-1]
MIN_DATE = mrr.columns[0]

# creatre a map from user_id to product and duration
user_product_map = user_table.groupby(['user_id'])['sub_product','sub_duration'].first()
### unique products and durations 
products = user_table['sub_product'].unique()
durations = user_table['sub_duration'].unique()

### Calculate start period of the subscription

## #1 Create cohorts based on the first observation of a month with a positive mrr value
cohort = (mrr > 0).idxmax( axis = 1).rename('cohort')

## #2 Add the cohort date to the index
tenure =  mrr.join( cohort ).set_index( 'cohort', append = True).stack()
tenure = tenure.reset_index( ).rename( columns = {'level_2':'date', 0:'revenue'} )


## #3 Calculate the number of periods (months) from the cohort date to the mrr date
tenure['periods'] =  np.round( (tenure['date'] - tenure['cohort']) / np.timedelta64(1, 'M') ,0).astype(int)

tenure.head(10)

## #1 Calculate revenue and subs count by cohort by month
gb =  tenure.groupby( [ pd.Grouper( key ='cohort' , freq = 'M') , 'periods'])
rev_cohorts = gb['revenue'].sum().unstack()
count_cohorts = gb['sub_id'].nunique().unstack()


## #2 turn them into a percentage realtive to the first month
scaled_revenue_cohorts = rev_cohorts.apply( lambda x : x/x[0] ,axis = 1)
scaled_count_cohorts = count_cohorts.apply( lambda x : x/x[0] ,axis = 1)

count_cohorts = gb['sub_id'].nunique().unstack()
count_cohorts.head(5)

scaled_count_cohorts = count_cohorts.apply( lambda x : x/x[0] ,axis = 1)
scaled_count_cohorts.head(5)

### Quick hvplot of both data frames
p1 = scaled_revenue_cohorts[scaled_revenue_cohorts>0].T.hvplot( figsize = [11,7], legend=False , title = 'Revenue')
p2 = scaled_count_cohorts[scaled_count_cohorts>0].T.hvplot(figsize = [11,7], legend=False , title = 'Logo Count')

### Add the graphs together to display as one output
(p1 + p2).cols(1)

### convert the subscription mrr into a user mrr
user_sub_map = user_table.loc[: , ['user_id','sub_id'] ].drop_duplicates()
user_mrr = mrr.reset_index( ).merge( user_sub_map , on = 'sub_id' ).drop( columns = 'sub_id')
user_mrr = user_mrr.groupby( 'user_id').sum()
user_cohort =(user_mrr>0).idxmax( axis = 1).rename('cohort')

user_mrr = user_mrr[ user_mrr >0]
user_tenure = user_mrr.join( user_cohort ).set_index( 'cohort', append = True).stack()
user_tenure = user_tenure.reset_index( ).rename( columns = {'level_2':'date', 0:'revenue'} )
user_tenure['periods'] =  np.round( (user_tenure['date'] - user_tenure['cohort']) / np.timedelta64(1, 'M') ,0).astype(int)

p1 = scaled_revenue_cohorts[scaled_revenue_cohorts>0].T.hvplot( figsize = [11,7], legend=False , title = 'Revenue')
p2 = scaled_count_cohorts[scaled_count_cohorts>0].T.hvplot(figsize = [11,7], legend=False , title = 'Logo Count')
(p1 + p2).cols(1)

## EXPLAINATION 

def gen_cohort_plot( cohort ):
    cohort = cohort[ cohort > 0]
    plot = cohort.T.hvplot( width=700, height=350, legend=False ) 
    d_min = MIN_DATE.year
    d_max = MAX_DATE.year
    
    for item in plot.items():
        date , curve = item
        year = pd.to_datetime( date ).year
        c = plt.cm.Blues( .8* (year - d_min ) / ( d_max - d_min ) + .2)
        curve.opts( hv.opts.Curve( color=c ))
    return plot

user_tenure = user_tenure.merge( user_product_map.reset_index() , on = 'user_id', how = 'left' )

## #1 Create product duration cohorts
gb = user_tenure.groupby( ['sub_product','sub_duration','cohort', 'user_id','periods'])

## #2 Divide each periods user count (observations with revenue > 0) by the month 0 count
cohorts_scaled = gb['revenue'].sum().unstack().groupby(level=[0,1,2]).apply( lambda x : (x>0).sum()/(x[0]>0).sum())

## #3 
cohorts = gb['user_id'].sum().unstack().groupby(level=[0,1,2]).apply( lambda x : (x>0).sum() )
revenue_cohorts = gb['revenue'].sum().unstack().groupby(level=[0,1,2]).sum()

## #4 Calculate the average price
cohort_asp = revenue_cohorts/cohorts

## #1 
mix = cohorts[0].rename('count').reset_index()
mix = mix.set_index(['cohort','sub_product','sub_duration'] )
mix = mix.sort_index()
## #2
abs_bars = hv.Bars( mix )
abs_bars.opts( stacked = True, xrotation = 45 , width = 700 , height = 400 , xaxis= None , ylabel = 'Conversions')
## #3
hund_bars = hv.Bars( mix/mix.groupby( level =0 ).sum() )
hund_bars.opts( stacked = True, xrotation = 45 , width = 700 , height = 400 , xformatter = dtf, ylabel = 'Relative %')
layout = (abs_bars + hund_bars).cols(1)
layout.opts(shared_axes=False)

mix.index.get_level_values(2).sort_values()

## #1 
abs_bars = hv.Bars(  mix.swaplevel(1,2).sort_index( level=[0,1] ))
abs_bars.opts( stacked = True, xrotation = 45 , width = 700 , height = 400, xaxis = None , ylabel = 'Conversions' )

## #2
hund_bars = hv.Bars( mix.swaplevel(1,2).sort_index( level=[0,1] )/mix.groupby( level =0 ).sum() )
hund_bars.opts( stacked = True, xrotation = 45 , width = 700 , height = 400  , xformatter = dtf, ylabel = 'Relative %' )

## #3
layout = (abs_bars + hund_bars).cols(1)
layout.opts(shared_axes=False)

## 
def pd_curve( product , duration , data = cohorts_scaled):
    ## explain index slice 
    idx = pd.IndexSlice
    data = data.loc[ idx[product, duration,:] , :].reset_index( level = [0,1], drop = True)
           
    data = data[data > 0]
    plot =  gen_cohort_plot( data  )
    plot.opts( opts.Layout( width = 700))
    return plot

## new version

curve_dict_2D = {(d,p):pd_curve(p,d, cohorts_scaled) for p in products for d in durations }
gridspace = hv.GridSpace(curve_dict_2D , kdims=['Duration', 'Product'])
hmap = hv.HoloMap(curve_dict_2D , kdims=['Duration', 'Product'])

ndlayout = hv.NdLayout(gridspace)
ndlayout.opts(opts.Curve(width=500, height=200)).cols(3)

## plot count of new users 
def conversion_plot( product , duration, data = cohorts ):
    idx = pd.IndexSlice
    data = data.loc[ idx[product,duration,:] , 0]
    data = data.droplevel([0,1]).rename('count').reset_index()    
    data['year'] = data['cohort'].dt.year
    data['cohort'] = data['cohort'].dt.date

    tmp_plot = hv.Bars ( data)
    tmp_plot.opts( opts.Bars( color = 'year' , cmap = 'Blues', xrotation = 45, width = 700 , xformatter = dtf))
    return tmp_plot

## plot asp 

def asp_plot( product , duration,  data = cohort_asp):
    idx = pd.IndexSlice
    data = data.loc[ idx[product,duration,:] , 0].droplevel([0,1] )
    data = data.rename('asp').reset_index()    
    data['year'] = data['cohort'].dt.year
   # data['cohort'] = data['cohort'].dt.date
    tmp_plot = hv.Bars ( data)
    tmp_plot.opts( opts.Bars( color = 'year' , cmap = 'Blues', xrotation = 45, width = 700, xformatter = dtf))
    return tmp_plot

conv_curve_dict_2D = {(d,p):conversion_plot( p , d , cohorts ) for p in products for d in durations }
conv_hmap = hv.HoloMap(conv_curve_dict_2D, kdims=['Duration', 'Product'])

asp_curve_dict_2D =  {(d,p):asp_plot(p,d, cohort_asp) for p in products for d in durations }
asp_hmap = hv.HoloMap(asp_curve_dict_2D, kdims=['Duration', 'Product'])

(hmap +conv_hmap + asp_hmap ).cols(1)

def heatmap_product_duration( product , duration , data = cohorts_scaled):
    idx = pd.IndexSlice
    data = data.loc[ idx[product, duration, :] , :].reset_index( level = [0,1], drop = True)
        
    data = data[data>0]
    
    data = data.stack().rename( 'retention').reset_index()
    data = data[ data['retention'] > 0]
    data.columns = ['cohort','tenure','retention']
    hm = hv.HeatMap(data , kdims=['tenure','cohort']).sort()    
    hm.opts( opts.HeatMap( width = 500 , height = 500  ,colorbar = True, \
                          yformatter = dtf , xrotation = 90 ,cmap = 'RdYlGn' ,tools=['hover'], toolbar='above'))
    return hm

def left_conv_bar( product , duration, data = cohorts ):

    idx = pd.IndexSlice
    data = data.loc[ idx[product, duration, :] , :].reset_index( level = [0,1], drop = True)
    data = data.loc[:,0].rename( 'conversions').reset_index()
    bar = hv.Bars(  data ).opts( invert_axes=True , height = 500 , width = 200 \
                                , color = 'Green' , yaxis = None, invert_xaxis=True )
    return bar



heatmap_curve_dict_2D = {(d,p):heatmap_product_duration(p,d) for p in products for d in durations }
heatmap_hmap = hv.HoloMap(heatmap_curve_dict_2D, kdims=['Duration', 'Product'])
left_bar_curve_dict_2D = {(d,p):left_conv_bar(p,d) for p in products for d in durations }
left_bar_hmap = hv.HoloMap(left_bar_curve_dict_2D, kdims=['Duration', 'Product'])
layout = (left_bar_hmap  + heatmap_hmap ).opts( shared_axes = True)

layout