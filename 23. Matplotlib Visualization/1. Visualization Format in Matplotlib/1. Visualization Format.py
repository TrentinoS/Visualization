#Visualization Format in Matplotlib

import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

"""
Ways to define colors
"""
plt.figure(figsize=(15, 8))
samples = range(1,4)

for i, col in zip(samples, [(0.0, 0.0, 1.0), 'blue', '#0000FF']):
    plt.plot([0, 10], [0, i], lw=3, color=col)

plt.legend(['RGB values: (0.0, 0.0, 1.0)',
            "matplotlib names: 'blue'",
            "HTML hex values: '#0000FF'"],
           loc='upper left')
plt.title('3 alternatives to define the color blue')
plt.savefig('1. Visualization Format Plots/plot_1.jpg')
plt.show()

"""
MY Way
"""

fig,ax = plt.subplots(figsize=(15,8))
fig.patch.set_facecolor('xkcd:gray')
ax.set_facecolor((0.,0.,0.))

plt.plot([0,10], [0,1], lw=3, color=(1.0,0.0,0.0))
plt.plot([0,10], [0,2], lw=3, color='red')
plt.plot([0,10], [0,3], lw=3, color='#f54842')
plt.legend(['RGB values: (1.0,0.0,0.0)',
            "matplotlib names: 'red'",
            "HTML hex values: '#f54842'"],
           loc='upper left')
plt.title('3 ways to define colors', fontsize=13)
plt.savefig("1. Visualization Format Plots/plot_2.jpg")
plt.show()

"""
color names
"""
cols = ['blue', 'green', 'red', 'cyan',  'magenta', 'yellow', 'black', 'white']

samples = range(1, len(cols)+1)
plt.figure(figsize=(15,8))
fig.patch.set_facecolor('xkcd:gray')

for i, col in zip(samples, cols):
    plt.plot([0, 10], [0, i], label=col, lw=3, color=col)

plt.legend(loc='upper left')
plt.title('Matplotlib Sample Colors', fontsize=13)
plt.savefig('1. Visualization Format Plots/plot_3.jpg')
plt.show()


"""
gray levels
"""
plt.figure(figsize=(15,8))

samples = np.arange(0, 1.1, 0.1)

for i in samples:
    plt.plot([0, 10], [0, i], label='gray-level %s'%i, lw=3,
             color=str(i)) # ! gray level has to be parsed as string

plt.legend(loc='upper left')
plt.title('Gray Gradients with RGBA Formatting', fontsize=13)
plt.savefig('1. Visualization Format Plots/plot_4.jpg')
plt.show()

"""
Color gradients
"""
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm
import numpy as np

# input data
mean_values = np.random.randint(1, 101, 100)
x_pos = range(len(mean_values))

fig = plt.figure(figsize=(15,8))

# create colormap
cmap = cm.ScalarMappable(col.Normalize(min(mean_values),
                                       max(mean_values),
                                       cm.hot))

# plot bars
plt.subplot(131)
plt.bar(x_pos, mean_values, align='center', alpha=0.5,
        color=cmap.to_rgba(mean_values))
plt.ylim(0, max(mean_values) * 1.1)

plt.subplot(132)
plt.bar(x_pos, np.sort(mean_values), align='center', alpha=0.5,
        color=cmap.to_rgba(mean_values))
plt.ylim(0, max(mean_values) * 1.1)

plt.subplot(133)
plt.bar(x_pos, np.sort(mean_values), align='center', alpha=0.5,
        color=cmap.to_rgba(np.sort(mean_values)))
plt.ylim(0, max(mean_values) * 1.1)

plt.savefig('1. Visualization Format Plots/plot_5.jpg')
plt.show()


"""
Marker styles
"""
marker_name = ['point', 'pixel', 'circle', 'triangle down', 'triangle up', 'triangle_left', 'triangle_right',
               'tri_down', 'tri_up', 'tri_left', 'tri_right', 'octagon', 'square', 'pentagon', 'star', 'hexagon1',
               'hexagon2', 'plus', 'x', 'diamond', 'thin_diamond', 'vline']

markers = [

'.', # point
',', # pixel
'o', # circle
'v', # triangle down
'^', # triangle up
'<', # triangle_left
'>', # triangle_right
'1', # tri_down
'2', # tri_up
'3', # tri_left
'4', # tri_right
'8', # octagon
's', # square
'p', # pentagon
'*', # star
'h', # hexagon1
'H', # hexagon2
'+', # plus
'x', # x
'D', # diamond
'd', # thin_diamond
'|', # vline

]
samples = range(len(markers))

plt.figure(figsize=(15, 8))
for i in samples:
    plt.plot([i-1, i, i+1], [i, i, i], label=marker_name[i], marker=markers[i], markersize=11)

# Annotation
plt.title('Matplotlib Marker styles', fontsize=20)
plt.ylim([-1, len(markers)+1])
plt.legend(loc='lower right')
plt.savefig('1. Visualization Format Plots/plot_6.jpg')
plt.show()


"""
line style
"""
linestyles = ['-.', '--', 'None', '-', ':']

plt.figure(figsize=(15, 8))
samples = range(len(linestyles))


for i in samples:
    plt.plot([i-1, i, i+1], [i, i, i],
             label='"%s"' %linestyles[i],
             linestyle=linestyles[i],
             lw=4
             )

# Annotation

plt.title('Matplotlib line styles', fontsize=20)
plt.ylim([-1, len(linestyles)+1])
plt.legend(loc='lower right')
plt.savefig('1. Visualization Format Plots/plot_7.jpg')

plt.show()

"""
removing frames
"""
x = range(10)
y = range(10)

plt.figure(figsize=(15,8))
fig = plt.gca()

plt.plot(x, y)

# removing frame
fig.spines["top"].set_visible(False)
fig.spines["bottom"].set_visible(False)
fig.spines["right"].set_visible(False)
fig.spines["left"].set_visible(False)

# removing ticks
plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="on", left="off", right="off", labelleft="on")
plt.savefig('1. Visualization Format Plots/plot_8.jpg')
plt.show()


"""
custom tick labels
"""
x = range(10)
y = range(10)
labels = ['super long axis label' for i in range(10)]

fig, ax = plt.subplots(figsize=(15,8))

plt.plot(x, y)

# set custom tick labels
ax.set_xticklabels(labels, rotation=45, horizontalalignment='right')
plt.savefig('1. Visualization Format Plots/plot_9.jpg')
plt.show()
;

"""
grid styling
"""
import numpy as np
import random, math
from matplotlib import pyplot as plt



data = np.random.normal(0, 20, 1000)
bins = np.arange(-100, 100, 5) # fixed bin size

# horizontal grid
plt.figure(figsize=(15,8))
plt.hist(data, bins=bins, alpha=0.5)
ax = plt.gca()
ax.yaxis.grid(True)
plt.savefig('1. Visualization Format Plots/plot_10.jpg')
plt.show()

# vertical grid
plt.figure(figsize=(15,8))
plt.hist(data, bins=bins, alpha=0.5)
ax = plt.gca()
ax.xaxis.grid(True)
plt.savefig('1. Visualization Format Plots/plot_11.jpg')
plt.show()

# linestyle
plt.figure(figsize=(15,8))
from matplotlib import rcParams

rcParams['grid.linestyle'] = '-'
rcParams['grid.color'] = 'blue'
rcParams['grid.linewidth'] = 0.2

plt.grid()
plt.hist(data, bins=bins, alpha=0.5)
plt.savefig('1. Visualization Format Plots/plot_12.jpg')
plt.show()


"""
outside of the box labels
"""
# above
fig = plt.figure(figsize=(15,8))
ax = plt.subplot(111)

x = np.arange(10)

for i in range(1, 4):
    ax.plot(x, i * x**2, label='Group %d' % i)

ax.legend(loc='upper center',
          bbox_to_anchor=(0.5,  # horizontal
                          1.15),# vertical
          ncol=3, fancybox=True)
plt.savefig('1. Visualization Format Plots/plot_13.jpg')
plt.show()

# right
fig = plt.figure(figsize=(15,8))
ax = plt.subplot(111)

x = np.arange(10)

for i in range(1, 4):
    ax.plot(x, i * x**2, label='Group %d' % i)

ax.legend(loc='upper center',
          bbox_to_anchor=(1.15, 1.02),
          ncol=1, fancybox=True)
plt.savefig('1. Visualization Format Plots/plot_14.jpg')
plt.show()

# transparent
x = np.arange(10)
plt.figure(figsize=(15,8))
for i in range(1, 4):
    plt.plot(x, i * x**2, label='Group %d' % i)

plt.legend(loc='upper right', framealpha=0.1)
plt.savefig('1. Visualization Format Plots/plot_15.jpg')
plt.show()



"""
style sheets
"""
print(plt.style.available)

# 1st way: set the style for our coding environment globally via the plt.style.use function
plt.style.use('ggplot')

x = np.arange(10)
plt.figure(figsize=(15,8))
for i in range(1, 4):
    plt.plot(x, i * x**2, label='Group %d' % i)
plt.legend(loc='best')
plt.title('Style sheet formatting', fontsize=13)
plt.savefig('1. Visualization Format Plots/plot_16.jpg')
plt.show()

# 2nd way: via the with context manager, which applies the styling to a specific code block only
with plt.style.context('fivethirtyeight'):
    plt.figure(figsize=(15,8))
    for i in range(1, 4):
        plt.plot(x, i * x**2, label='Group %d' % i)
    plt.legend(loc='best')
    plt.title('Style sheet formatting', fontsize=13)
    plt.savefig('1. Visualization Format Plots/plot_17.jpg')
    plt.show()

# All styles
import math

n = len(plt.style.available)
num_rows = math.ceil(n/4)

fig = plt.figure(figsize=(20, 15))

for i, s in enumerate(plt.style.available):
    with plt.style.context(s):
        ax = fig.add_subplot(num_rows, 4, i+1)
        for i in range(1, 4):
            ax.plot(x, i * x**2, label='Group %d' % i)
            ax.set_xlabel(s, color='black')
            ax.legend(loc='best')

fig.tight_layout()
plt.savefig('1. Visualization Format Plots/plot_18.jpg')
plt.show()

