#!/usr/bin/python3
#Author: Rebecca Dean
#script for converting a CSV file into an array and then plotting as a matrix
#plots a greater number of chains with white gridlines
#used for comparing backbone RMSDs but can be adapted
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
#set axis text and tick size
mpl.rc('xtick', labelsize=10) 
mpl.rc('ytick', labelsize=10)
#load csv file. Make sure no strings present. 
df = pd.read_csv('name.csv')
#set figure size
fig, ax = plt.subplots(figsize=(10, 10))
fig.subplots_adjust(top=0.99, bottom=0.02)
#arrange data into matrix showing only 1/2 of triangle
np.ones_like(df, dtype=np.bool)
mask = np.triu(np.ones_like(df, dtype=np.bool))
#converts data into heatmap, set colour, min and max of scale and size of line between boxes and sets the colour bar according to specifications such as colorscale, range, and placing of tickmarks
cmap = mpl.cm.seismic
extent = (0, df.shape[1], df.shape[0], 0)
cax = ax.imshow(df, cmap=cmap, vmin=0, vmax=6, extent=extent)
cbar = ax.figure.colorbar(cax, ticks=[1, 3.5, 5.5], orientation='vertical')
cbar.ax.set_yticklabels(['1', 'Mean', '5.5'])
# Gridlines based on minor ticks
ax.grid(color='w', linewidth=1)
#axis labels
xticks_labels = ['set1_A', 'B', 'C', 'D', 'E','set2_A', 'B', 'C', 'D', 'E', 'set3_A', 'B', 'C', 'D', 'E', 'set4_A', 'B', 'C', 'D', 'E', 'set5_A', 'B', 'C', 'D', 'E']
plt.xticks(np.arange(25, step=1), labels=xticks_labels, rotation=90)
yticks_labels = ['set1_A', 'B', 'C', 'D', 'E','set2_A', 'B', 'C', 'D', 'E', 'set3_A', 'B', 'C', 'D', 'E', 'set4_A', 'B', 'C', 'D', 'E', 'set5_A', 'B', 'C', 'D', 'E']
plt.yticks(np.arange(25, step=1), labels=yticks_labels, rotation=360)
#set title
title= 'name (Ǻ)\n'.upper()
plt.title(title, loc='center')
#plt.show()
fig.savefig('name.png')
