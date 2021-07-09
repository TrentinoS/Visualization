#IMPORTS
import matplotlib.pyplot as plt
import numpy as np

#FIRST EXAMPLE

#Days of the week:
days = [1, 2, 3, 4, 5, 6,7]
# Your Money:
money_spent = [1000, 1200, 1500, 1080, 1400, 1650, 1350]
# Your Friend's Money:
money_spent_2 = [900, 1500, 1200, 1050, 950, 1250, 1000]
# Create figure:
fig = plt.figure(figsize=(15,8))
# Plot first week expenses:
plt.plot(days, money_spent)
# Plot second week expenses
plt.plot(days, money_spent_2)
# Display the result:
plt.title('Company Expenditure Comparison')
plt.legend(['First week', 'Second week'])
plt.savefig('Visualizations Basics Plots/plot_1.jpg')
plt.show()

#SECOND EXAMPLE

# Create figure:
fig2 =plt.figure(figsize=(15,8))
# Plot your money:
plt.plot(days, money_spent,color='purple', linestyle='--', marker='o')
# Plot your friend's money:
plt.plot(days, money_spent_2,color='#045a71', linestyle=':', marker='o')
# Display the result:
ax = plt.subplot()
ax.set_xticks(range(1,8))
ax.set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday',' Sunday'])
plt.title('Company Expenditure Comparison')
plt.legend(['First week', 'Second week'])
plt.savefig('Visualizations Basics Plots/plot_2.jpg')
plt.show()

#THIRD EXAMPLE

# Create figure:
fig3 = plt.figure(figsize=(15,8))
# Plot your money:
plt.plot(days, money_spent,color='purple', linestyle='--', marker='o')
# Plot your friend's money:
plt.plot(days, money_spent_2,color='#045a71', linestyle=':', marker='o')
# Display the result:
ax = plt.subplot()
ax.set_xticks(range(1,8))
ax.set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday',' Sunday'])
plt.title('Monday-Wednesday Company Expenditure')
plt.legend(['First week', 'Second week'])
plt.axis([1,3,900,1600])
plt.savefig('Visualizations Basics Plots/plot_3.jpg')
plt.show()


#SUBPLOTS => PARAMETERS (number of rows of subplots, number of columns of subplots, index of subplot)

x = [1,2,3,4]
y = [2,5,6,3]

plt.figure(figsize=(15,8))
plt.subplot(1,2,1)
plt.plot(x,y,color='red',linestyle='--')
plt.axis([0,5,0,7])     # PRIMEROS DOS SON DE Y, SEGUNDOS 2 SON DE X
plt.title('First Plot')

plt.figure(figsize=(15,8))
plt.subplot(1,2,2)
plt.plot(x,y, color='steelblue', linestyle=':')
plt.axis([0,5,0,7])
plt.title('Second Plot')
plt.savefig('Visualizations Basics Plots/Plots_4.jpg')
plt.show()


#TEMPERATURE AND FLIGHTS EXAMPLE

from matplotlib import pyplot as plt

months = range(12)
temperature = [37, 38, 40, 53, 62, 71, 78, 74, 69, 56, 47, 48]
flights_to_hawaii = [1100, 1300, 1200, 1400, 800, 700, 450, 500, 450, 900, 950, 1100]

# Create figure:
fig4 = plt.figure(figsize=(15,8))

# Display the result:
plt.subplot(1,2,1)
plt.plot(months,temperature,color='steelblue',linestyle='--')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.title('Temperature Representation')

plt.subplot(1,2,2)
plt.plot(months,flights_to_hawaii,color='red',marker='o')
plt.xlabel('Month')
plt.ylabel('Flights Summary')
plt.title('Flights per month')

plt.savefig('Visualizations Basics Plots/plot_5.jpg')
plt.show()

#SUBPLOTS ADJUSTMENT

"""
We can customize the spacing between our subplots to make sure that the figure we create is visible and easy to understand.
To do this, we use the plt.subplots_adjust() command.
.subplots_adjust() has some keyword arguments that can move your plots within the figure:
- left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
- right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or decrease it to make room for a legend
- bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label
- top — the top margin, with a default of 0.9
- wspace — the horizontal space between adjacent subplots, with a default of 0.2
- hspace — the vertical space between adjacent subplots, with a default of 0.2
"""
from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.figure(figsize=(15,8))

plt.subplot(2,1,1)
plt.plot(x,straight_line,color='purple',linestyle='--')
plt.xlabel('Range')
plt.ylabel("Line")
plt.title('Example Graph')
plt.savefig('Visualizations Basics Plots/plot_6.jpg')

plt.subplot(2,2,3)
plt.plot(x,parabola, color='green',linestyle=':')
plt.xlabel("Range 1")
plt.ylabel("Line")
plt.savefig('Visualizations Basics Plots/plot_7.jpg')

plt.subplot(2,2,4)
plt.plot(x,cubic, color='red', linestyle='--')
plt.xlabel("Range 2")
plt.ylabel("Line 2")
plt.grid()

plt.subplots_adjust(hspace=0.35,bottom=0.2,wspace=0.35)
plt.show()
plt.savefig('Visualizations Basics Plots/plot_8.jpg')

#LEGENDS AND LABELING

"""
When we have multiple lines on a single graph we can label them by using the command plt.legend().
plt.legend() can also take a keyword argument loc, which will position the legend on the figure ('BEST', 'UPPER RIGHT', 'LOWER CENTER', ETC).
"""
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.figure(figsize=(15,8))
plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)
plt.savefig('Visualizations Basics Plots/plot_9.jpg')

# LEGEND EXAMPLE
legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]
plt.legend(legend_labels, loc=8)
plt.show()

plt.figure(figsize=(15,8))

#MODIFY X AND Y TICKS AND LABELS
ax = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_xticks([1, 2, 4])
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])
plt.savefig('Visualizations Basics Plots/plot_10.jpg')
#EXAMPLE OF TICKS AND LABELS
from matplotlib import pyplot as plt

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]
months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.1,0.25,0.5,0.75])
ax.set_yticklabels(['10%', '25%', '50%','75%'])

plt.xlabel("Months")
plt.ylabel("Conversion")
plt.plot(months, conversion)

plt.show()
plt.savefig('Visualizations Basics Plots/plot_11.jpg')

#FIGURES
"""
Previously, we learned how to put two sets of axes into the same figure. Sometimes, we would rather have two separate figures.
We can use the command plt.figure() to create new figures and size them how we want. We can add the keyword figsize=(width, height) to set
the size of the figure, in inches.
- plt.figure(figsize=(4, 10))
Once we’ve created a figure, we might want to save it so that we can use it in a presentation or a website. We can use the command plt.savefig()
to save out to many different file formats, such as png, svg, or pdf.
After plotting, we can call plt.savefig('name_of_graph.png')
"""
from matplotlib import pyplot as plt

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')
plt.figure()
plt.plot(years, word_length)
plt.savefig('Visualizations Basics Plots/plot_14.jpg')
plt.figure(figsize=(15,8))
plt.plot(years, power_generated)
plt.savefig('Visualizations Basics Plots/plot_12.jpg')


#GENERALIZING SUBPLOTS

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]



plt.figure(figsize=(15,8))
plt.plot(months,temperature,color='steelblue',linestyle='--')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Temperature per month')
plt.savefig('Visualizations Basics Plots/plot_13.jpg')
plt.show()

;

