# # Building styles

# #### Let’s see some examples.



import pandas as pd
import numpy as np

np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
df.iloc[3, 3] = np.nan
df.iloc[0, 2] = np.nan


# ##### Here’s a boring example of rendering a DataFrame, without any (visible) styles:

df.style


df.style.highlight_null().render().split('\n')[:10]


# #### Let’s write a simple style function that will color negative numbers red and positive numbers black.




def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color


# #### In this case, the cell’s style depends only on its own value. That means we should use the Styler.applymap method which works elementwise.
# 



s = df.style.applymap(color_negative_red)
s




def highlight_max(s):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]





df.style.apply(highlight_max)


# #### In this case the input is a Series, one column at a time. Notice that the output shape of highlight_max matches the input shape, an array with len(s) items.
# 
# #### We encourage you to use method chains to build up a style piecewise, before finally rending at the end of the chain.




df.style.    applymap(color_negative_red).    apply(highlight_max)





def highlight_max(data, color='yellow'):
    '''
    highlight the maximum in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.max()
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)


# #### When using Styler.apply(func, axis=None), the function must return a DataFrame with the same index and column labels.



df.style.apply(highlight_max, color='darkorange', axis=None)


# # Building Styles Summary

# Style functions should return strings with one or more CSS attribute: value delimited by semicolons. Use
# 
# - *_Styler.applymap(func)_* for elementwise styles
# 
# - *_Styler.apply(func, axis=0)_* for columnwise styles
# 
# - *_Styler.apply(func, axis=1)_* for rowwise styles
# 
# - *_Styler.apply(func, axis=None)_* for tablewise styles
# 
# And crucially the input and output shapes of func must match. If x is the input then **_func(x).shape == x.shape_**.

# # Finer control: slicing

# Both *_Styler.apply_*, and *_Styler.applymap_* accept a subset keyword. This allows you to apply styles to specific rows or columns, without having to code that logic into your *_style_* function.
# 
# The value passed to subset behaves similar to slicing a DataFrame.
# 
# - A scalar is treated as a column label
# 
# - A list (or series or numpy array)
# 
# - A tuple is treated as *_(row_indexer, column_indexer)_*
# 
# Consider using *_pd.IndexSlice_* to construct the tuple for the last one.
# 
# 



df.style.apply(highlight_max, subset=['B', 'C', 'D'])


# #### For row and column slicing, any valid indexer to .loc will work.
# 
# 




df.style.applymap(color_negative_red, subset=pd.IndexSlice[2:5, ['B', 'D']])


# # Finer Control: Display Values




df.style.format("{:.2%}")


# #### Use a dictionary to format specific columns.
# 
# 




df.style.format({'B': "{:0<4.0f}", 'D': '{:+.2f}'})


# #### Or pass in a callable (or dictionary of callables) for more flexible handling.




df.style.format({"B": lambda x: "±{:.2f}".format(abs(x))})


# #### You can format the text displayed for missing values by *_na_rep_*.




df.style.format("{:.2%}", na_rep="-")


# #### These formatting techniques can be used in combination with styling.




df.style.highlight_max().format(None, na_rep="-")


# # Builtin styles

# #### Finally, we expect certain styling functions to be common enough that we’ve included a few “built-in” to the Styler, so you don’t have to write them yourself.



df.style.highlight_null(null_color='red')


# #### You can create “heatmaps” with the background_gradient method. These require matplotlib, and we’ll use Seaborn to get a nice colormap.




import seaborn as sns

cm = sns.light_palette("green", as_cmap=True)

s = df.style.background_gradient(cmap=cm)
s


# #### Styler.background_gradient takes the keyword arguments low and high. Roughly speaking these extend the range of your data by low and high percent so that when we convert the colors, the colormap’s entire range isn’t used. This is useful so that you can actually read the text still.




# Uses the full color range
df.loc[:4].style.background_gradient(cmap='viridis')





# Compress the color range
(df.loc[:4]
    .style
    .background_gradient(cmap='viridis', low=.5, high=0)
    .highlight_null('red'))


# #### There’s also .highlight_min and .highlight_max.




df.style.highlight_max(axis=0)


# #### Use Styler.set_properties when the style doesn’t actually depend on the values.




df.style.set_properties(**{'background-color': 'black',
                           'color': 'lawngreen',
                           'border-color': 'white'})


# # Bar charts

# #### You can include “bar charts” in your DataFrame.




df.style.bar(subset=['A', 'B'], color='#d65f5f')


# #### Here’s how you can change the above with the new align='mid' option:




df.style.bar(subset=['A', 'B'], align='mid', color=['#d65f5f', '#5fba7d'])


# #### The following example aims to give a highlight of the behavior of the new align options:




import pandas as pd
from IPython.display import HTML

# Test series
test1 = pd.Series([-100,-60,-30,-20], name='All Negative')
test2 = pd.Series([10,20,50,100], name='All Positive')
test3 = pd.Series([-10,-5,0,90], name='Both Pos and Neg')

head = """
<table>
    <thead>
        <th>Align</th>
        <th>All Negative</th>
        <th>All Positive</th>
        <th>Both Neg and Pos</th>
    </thead>
    </tbody>

"""

aligns = ['left','zero','mid']
for align in aligns:
    row = "<tr><th>{}</th>".format(align)
    for series in [test1,test2,test3]:
        s = series.copy()
        s.name=''
        row += "<td>{}</td>".format(s.to_frame().style.bar(align=align,
                                                           color=['#d65f5f', '#5fba7d'],
                                                           width=100).render()) #testn['width']
    row += '</tr>'
    head += row

head+= """
</tbody>
</table>"""


HTML(head)


# # Sharing styles

# ##### Say you have a lovely style built up for a DataFrame, and now you want to apply the same style to a second DataFrame. Export the style with *_df1.style.export_*, and import it on the second DataFrame with *_df1.style.set_*




df2 = -df
style1 = df.style.applymap(color_negative_red)
style1





style2 = df2.style
style2.use(style1.export())
style2


# # Precision
# 

# #### You can control the precision of floats using pandas’ regular *_display.precision_* option.




with pd.option_context('display.precision', 2):
    html = (df.style
              .applymap(color_negative_red)
              .apply(highlight_max))
html


# #### Or through a set_precision method.



df.style  .applymap(color_negative_red)  .apply(highlight_max)  .set_precision(2)


# #### Setting the precision only affects the printed number; the full-precision values are always passed to your style functions. You can always use *_df.round(2).style_* if you’d prefer to round from the start.

# # Captions

# #### Regular table captions can be added in a few ways.




df.style.set_caption('Colormaps, with a caption.')    .background_gradient(cmap=cm)


# # Table styles

# #### The next option you have are *_“table styles”_*. These are styles that apply to the table as a whole, but don’t look at the data. Certain stylings, including pseudo-selectors like :hover can only be used this way. These can also be used to set specific row or column based class selectors, as will be shown.




from IPython.display import HTML

def hover(hover_color="#ffff99"):
    return dict(selector="tr:hover",
                props=[("background-color", "%s" % hover_color)])

styles = [
    hover(),
    dict(selector="th", props=[("font-size", "150%"),
                               ("text-align", "center")]),
    dict(selector="caption", props=[("caption-side", "bottom")])
]
html = (df.style.set_table_styles(styles)
          .set_caption("Hover to highlight."))
html


# #### table_styles should be a list of dictionaries. Each dictionary should have the selector and props keys. The value for selector should be a valid CSS selector. Recall that all the styles are already attached to an id, unique to each Styler. This selector is in addition to that id. The value for props should be a list of tuples of ('attribute', 'value').
# 
# #### table_styles are extremely flexible, but not as fun to type out by hand. We hope to collect some useful ones either in pandas, or preferable in a new package that builds on top the tools here.
# 
# #### table_styles can be used to add column and row based class descriptors. For large tables this can increase performance by avoiding repetitive individual css for each cell, and it can also simplify style construction in some cases. If table_styles is given as a dictionary each key should be a specified column or index value and this will map to specific class CSS selectors of the given column or row.
# 
# #### Note that Styler.set_table_styles will overwrite existing styles but can be chained by setting the overwrite argument to False.




html = html.set_table_styles({
    'B': [dict(selector='', props=[('color', 'green')])],
    'C': [dict(selector='td', props=[('color', 'red')])],
    }, overwrite=False)
html


# # Missing values

# #### You can control the default missing values representation for the entire table through set_na_rep method.
# 
# 



(df.style
   .set_na_rep("FAIL")
   .format(None, na_rep="PASS", subset=["D"])
   .highlight_null("yellow"))


# # Hiding the Index or Columns

# #### The index can be hidden from rendering by calling Styler.hide_index. Columns can be hidden from rendering by calling Styler.hide_columns and passing in the name of a column, or a slice of columns.




df.style.hide_index()





df.style.hide_columns(['C','D'])


# # Fun stuff
# 

# #### Here are a few interesting examples.
# 
# #### Styler interacts pretty well with widgets. If you’re viewing this online instead of running the notebook yourself, you’re missing out on interactively adjusting the color palette.




from IPython.html import widgets
@widgets.interact
def f(h_neg=(0, 359, 1), h_pos=(0, 359), s=(0., 99.9), l=(0., 99.9)):
    return df.style.background_gradient(
        cmap=sns.palettes.diverging_palette(h_neg=h_neg, h_pos=h_pos, s=s, l=l,
                                            as_cmap=True)
    )





def magnify():
    return [dict(selector="th",
                 props=[("font-size", "4pt")]),
            dict(selector="td",
                 props=[('padding', "0em 0em")]),
            dict(selector="th:hover",
                 props=[("font-size", "12pt")]),
            dict(selector="tr:hover td:hover",
                 props=[('max-width', '200px'),
                        ('font-size', '12pt')])
]





np.random.seed(25)
cmap = cmap=sns.diverging_palette(5, 250, as_cmap=True)
bigdf = pd.DataFrame(np.random.randn(20, 25)).cumsum()

bigdf.style.background_gradient(cmap, axis=1)    .set_properties(**{'max-width': '80px', 'font-size': '1pt'})    .set_caption("Hover to magnify")    .set_precision(2)    .set_table_styles(magnify())

