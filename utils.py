import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def hist_box_plot(data, column):
    fig = plt.figure(figsize=(7, 6)) #dpi= 80
    grid = plt.GridSpec(2, 1, hspace=0.4, wspace=0.2)

    # Define the axes
    ax_main = fig.add_subplot(grid[0])
    ax_bottom = fig.add_subplot(grid[-1]) 
    
    ax_main.hist(column, alpha=.9, data=data, color='#336666')
    sns.boxplot(data[column], ax=ax_bottom, orient="h", color='#336666')

    ax_main.set(title='Destribution of ' + column, xlabel=column, ylabel='Count')
    ax_bottom.set(xlabel='')

    # Set font size of different components
    ax_main.title.set_fontsize(14)
    for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
        item.set_fontsize(12)

    plt.show()
    
def clusters_count_plot(labels):
    '''group distribution of clustring'''
 
    plt.figure(figsize=(5,4))
    sns.countplot(x=labels, palette= 'Set2')
    plt.title("Size of clusters", fontdict={'fontsize':14})
    plt.xlabel('Clusters')
    plt.show()

def pairplot_clusters(data, labels, n_clusters, num_col_plot):
    ds = data.copy()
    ds['Clusters'] = labels
    plt.figure()
    sns.pairplot(ds[num_col_plot+['Clusters']], hue= 'Clusters', palette='Set2') 
    plt.show()

def plot_cat_features_clusters(data, cat_col_plot, labels):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.countplot(data[cat_col_plot[0]], hue=labels, palette='Set2', ax=axes[0])
    sns.countplot(data[cat_col_plot[1]], hue=labels, palette='Set2', ax=axes[1])

    plt.show()

