#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:


import matplotlib.pyplot as plt


# # Line Plot

# In[2]:


plt.figure(figsize=(15, 8))

# pair 1
x = [2016, 2017, 2018, 2019, 2020, 2021] 
y = [42, 43, 45, 47, 48, 50] 

# pair 2
x2 = [2016, 2017, 2018, 2019, 2020, 2021] 
y2 = [43, 43, 44, 44, 45, 45]

# plotting
plt.plot(x, y, marker='o', linestyle='--', color='g', label='Colombia')
plt.plot(x2, y2, marker='d', linestyle='-', color='r', label='Argentina')


plt.xlabel('Year')
plt.ylabel('Population (M)')
plt.title('Year vs Population')
plt.legend(loc='lower right')

plt.yticks([41, 45, 48, 51])
plt.savefig('Plots/Line.jpg')
plt.show()


# # Subplots

# In[3]:


#  subplots
fig, ax = plt.subplots(1, 2, sharey=True, figsize=(15, 8)) #figsize 

ax[0].plot(x, y, color='g', label='Colombia')
ax[0].legend()

ax[1].plot(x2, y2, color='r', label='Argentina')
ax[1].legend()
plt.savefig('Plots/Line_Sub.jpg')
plt.show()

# ------


# fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(10, 10))

# ax[0][0].plot(x, y, 'o-', c='r', label='Colombia') 
# ax[0][2].plot(x2, y2, 'v--', c='b', label='Argentina') 

# plt.show()


# # Bar Plots

# In[4]:


plt.figure(figsize=(15,8))
x = ['Argentina', 'Colombia', 'Peru'] 
y = [40, 50, 33] 

plt.bar(x, y)
plt.savefig('Plots/Bar.jpg')
plt.show()


# # Pie Chart

# In[5]:


plt.figure(figsize=(15,8))
plt.pie(y, labels=x, autopct='%.0f %%') # "autopct" 
plt.savefig('Plots/Pie.jpg')
plt.show()


# # Histogram

# In[6]:


plt.figure(figsize=(15,8))

val = [15, 16, 17, 20, 21, 21, 22, 23, 24 ,25, 26, 30, 31, 32, 35]
bins = [15, 20, 25, 30, 35] 

plt.hist(val, bins, edgecolor='black')
plt.savefig('Plots/Hist.jpg')
plt.show()


# # Box Plot

# In[7]:


plt.figure(figsize=(15,8))

val = [15, 16, 17, 20, 21, 21, 22, 23, 24 ,25, 26, 30, 31, 32, 35, 70] # 70 es un valor atípico en esta lista

plt.boxplot(val)
plt.savefig('Plots/Box.jpg')
plt.show()


# # Scatter Plot

# In[8]:


plt.figure(figsize=(15,8))

a = [1, 2, 3, 4, 5, 4, 3 ,2 ,2, 4, 5, 6, 7]
b = [7, 2, 3, 5, 5, 7, 3, 2, 1, 4, 6, 3, 2]

plt.scatter(a, b)
plt.savefig('Plots/Scatter.jpg')
plt.show()

