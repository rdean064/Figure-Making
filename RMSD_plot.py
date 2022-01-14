#!/usr/bin/python3
#Author: Rebecca Dean
#script for converting a CSV file into an array and then plotting as a matrix
#used for comparing backbone RMSDs but can be adapted
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib as mpl
#set axis text and tick size
mpl.rc('xtick', labelsize=10) 
mpl.rc('ytick', labelsize=10)
#load csv file. Make sure no strings present. 
df = pd.read_csv('name.csv')
#set figure size
fig, ax = plt.subplots(figsize=(12, 8))
#arrange data into matrix showing only 1/2 of triangle
np.ones_like(df, dtype=np.bool)
mask = np.triu(np.ones_like(df, dtype=np.bool))
#converts data into heatmap, set colour, min and max of scale and size of line between boxes and sets the colour bar according to specifications such as colorscale, range, and placing of tickmarks
cmap = mpl.cm.seismic
cax = ax.imshow(df, cmap=cmap, vmin=0, vmax=6, )
cbar = fig.colorbar(cax, ticks=[1, 3, 5], orientation='vertical')
cbar.ax.set_yticklabels(['1', 'Mean', '5']) 
#axis labels
xticks_labels = ['set1', 'set2', 'set3', 'set4', 'set5']
plt.xticks(np.arange(5), labels=xticks_labels)
yticks_labels = ['set1', 'set2', 'set3', 'set4', 'set5']
plt.yticks(np.arange(5), labels=yticks_labels, rotation=360)
#set title
title= 'RMSD Ca Backbone (Ǻ)\n'.upper()
plt.title(title, loc='center')
#plt.show()
fig.savefig('name.png')
