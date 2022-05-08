from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
#import bokeh
#from bokeh.plotting import figure
#from bokeh.io import show, output_notebook, reset_output
#from bokeh.models import  ColumnDataSource, Legend, HoverTool, Title
import pyreadr
#import pandas as pd
#import numpy as np
#import re
#import matplotlib.pyplot as plt
#import matplotlib
#import seaborn as sns
#import warnings
#from pandas.api.types import CategoricalDtype
#from sklearn.preprocessing import LabelEncoder
#from sklearn.model_selection import train_test_split
#from imblearn.under_sampling import RandomUnderSampler
#from sklearn.ensemble import RandomForestClassifier
#from sklearn import metrics, tree
#from sklearn.metrics import ConfusionMatrixDisplay
#from bokeh.io import output_file, show
#from bokeh.plotting import figure
#from bokeh.layouts import layout
#from bokeh.models.widgets import Tabs, Panel

#Data preprocessing
# read the second file
# for each WDPAID, the number of unique users and photo per users per year for each treatment level
result = pyreadr.read_r(r'_MPA/alldata_user_photo_share.RData') 
df2 = result[list(result.keys())[0]]

# read the third file
# text data associated with photos used for the STM. the photo ID is the unique flickr id of the photo, the owner ID was removed.
#df3 = pd.read_csv('_MPA/photo_description_STM.csv', encoding = 'cp1252', engine = 'python', on_bad_lines = 'warn')

# read the fourth file
# this file includes the list of MPA WDPAID and whether the MPA was included in the analysis of total photo counts or not
df4 = pd.read_csv('_MPA/MPAincluded_share.csv')

# list of all the included WDPAID's
included = list(df4['WDPAID'][df4['included']==True])

# read the fifth file
# total photo count for retained MPAs and associated control areas per year included MPA size
df5 = pd.read_csv('_MPA/total_photos_count_share.csv')

# fill nan values with zeroes
df2['user.count'] = df2['user.count'].fillna(0)
df2['photouser.count'] = df2['photouser.count'].fillna(0)

#convert WDPA_PID to numbers
df2['WDPA_PID'] = df2['WDPA_PID'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)

# Get a list of continents and countries from dataframe
continents = list(df2.continent.unique())
countries = list(df2.country.unique())

# Creating a subset of dataframe 2 for counting the number of marine protected areas in the dataset
d = df2.drop_duplicates(subset='WDPA_PID', keep="first")

# drop index Unnamed: 0
df3 = df3.drop(columns = 'Unnamed: 0')

# fill nan values with zeroes
df3['title'] = df3['title'].fillna(0)
df3['tags'] = df3['tags'].fillna(0)

#Convert WDPA_PID to int
df3['WDPA_PID'] = df3['WDPA_PID'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)

# deleting data with duplicate WDPA_PIDs
df3.drop_duplicates(subset=['id'], inplace=True)

# create the df3_con dataframe that additionally to the df3 contains also the continent 
df3_con = df3.copy()
df3_con = df3_con.merge(df2[['WDPA_PID', 'country', 'continent']].drop_duplicates(), on='WDPA_PID', how='left')
# or
#df3_con = df3_con.set_index('WDPA_PID').join(df1[['WDPA_PID', 'continent']].drop_duplicates().set_index('WDPA_PID'))

# Manually adding some country names and continents found in https://www.protectedplanet.net/
#df3_con.loc[df3_con['WDPA_PID'] == 365015, 'country'] = '0'
df3_con.loc[df3_con['WDPA_PID'] == 365015, 'continent'] = 'Europe & Central Asia'
df3_con.loc[df3_con['WDPA_PID'] == 478048, 'country'] = 'NZL'
df3_con.loc[df3_con['WDPA_PID'] == 478048, 'continent'] = 'East Asia & Pacific'
df3_con.loc[df3_con['WDPA_PID'] == 478297, 'country'] = 'NZL'
df3_con.loc[df3_con['WDPA_PID'] == 478297, 'continent'] = 'East Asia & Pacific'
df3_con.loc[df3_con['WDPA_PID'] == 555512062, 'country'] = 'NZL'
df3_con.loc[df3_con['WDPA_PID'] == 555512062, 'continent'] = 'East Asia & Pacific'
df3_con.loc[df3_con['WDPA_PID'] == 555515499, 'country'] = 'NZL'
df3_con.loc[df3_con['WDPA_PID'] == 555515499, 'continent'] = 'East Asia & Pacific'

df3_con.loc[df3_con['WDPA_PID'] == 555624307, 'country'] = 'MEX'
df3_con.loc[df3_con['WDPA_PID'] == 555624307, 'continent'] = 'Latin America & Caribbean'
#df3_con.loc[df3_con['WDPA_PID'] == '555624810', 'country'] = '0'
df3_con.loc[df3_con['WDPA_PID'] == 555624810, 'continent'] = 'ABNJ'
df3_con.loc[df3_con['WDPA_PID'] == 555629253, 'country'] = 'FJI'
df3_con.loc[df3_con['WDPA_PID'] == 555629253, 'continent'] = 'East Asia & Pacific'
df3_con.loc[df3_con['WDPA_PID'] == 555637698, 'country'] = 'CAN'
df3_con.loc[df3_con['WDPA_PID'] == 555637698, 'continent'] = 'North America'
df3_con.loc[df3_con['WDPA_PID'] == 555645309, 'country'] = 'AUS'
df3_con.loc[df3_con['WDPA_PID'] == 555645309, 'continent'] = 'East Asia & Pacific'


# Converting 'datetaken' column to datetime format
df3_con['datetaken'] = pd.to_datetime(df3_con['datetaken'], format = '%Y-%m-%d %H:%M:%S')

# Add following columns to dataframe
df3_con['year'] = df3_con.datetaken.dt.year
df3_con['month'] = df3_con.datetaken.dt.month_name()
df3_con['day'] = df3_con.datetaken.dt.day
df3_con['weekday'] = df3_con.datetaken.dt.day_name()
df3_con['hour'] = df3_con.datetaken.dt.hour


# make 'month' col categorical in order to sort it
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
cat_type_month = CategoricalDtype(categories = months, ordered = True)
df3_con['month'] = df3_con['month'].astype(cat_type_month)

# make 'weekday' col categorical in order to sort it
weekdays = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cat_type_wday = CategoricalDtype(categories = weekdays, ordered = True)
df3_con['weekday'] = df3_con['weekday'].astype(cat_type_wday)


st.set_page_config(page_title="Marine Protected Areas", page_icon="🌊", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.image("images.jpg", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
"""
# Welcome to Marine Protected Areas Project!
This website is here to introduce you to Marine protected areas and guide you through the Flickr dataset about the MPAs...

"""

        
st.markdown("## Introduction")
'''
Marine protected areas (MPAs) are advocated as a key tool to manage the restoration and sustainable use of the oceans.[1]
'''
st.markdown("## Basic statistics")
'''
Text for basic stats
'''
st.markdown("## Data Analysis")
'''
Text for data analysis
'''
st.markdown("### Temporal Data")
'''
Text for Temporal data
'''
# Temporal plots using Bokeh



# reset_output() # If you are having issues with visualizing Bokeh plots in the notebook try to uncomment this line
output_notebook() # This is to make sure that bokeh plots in the notebook


def create_df(col):
    #Compute number total number of samples
    df_ = df3_con.groupby([col, 'treatment']).count()[['id']].rename({'id':'count'}, axis = 1).reset_index()
    df_ = df_.pivot_table(index = col, values='count', columns='treatment').reset_index().rename_axis(None, axis=1).astype('str')
    
    return df_
    
def create_bokeh(df_,col):
    #Convert your DataFrame to Bokeh ColumnDataSource
    src = ColumnDataSource(df_)

    #Define the columns to use for each bar
    bar_cols = ['control', 'MPA']
    #Create an empty figure
    p = figure(x_range=list(df_[col]), plot_width = 800, plot_height = 500, title = 'N. samples by '+col,
               x_axis_label = col , y_axis_label = 'N. of samples') 
    
    p.add_layout(Title(text="Figure 1: Interactive bar plot showing Number of Samples by year, month, day, weekday, hour . ", align="left"), "below")
    colors = ['red', 'blue']
    bar ={} 
    for indx,i in enumerate(bar_cols):
        #Add bars by using p.var
        bar[i] = p.vbar(x=col,  top=i, source= src, width=0.8, 
                        legend_label=bar_cols[indx], color=colors[indx], muted = True, name = i)

    #This is to manage the legend in plot
    p.legend.visible = True
    p.add_tools(HoverTool(renderers=[bar['control']],tooltips = [
                (col, f'@{col}'),
                ('No. of MPA records', '@MPA'),
                ('No. of Control records', '@control')
            ],mode='mouse'))
    #add the legend outside the plot
    p.add_layout(p.legend[0], 'right')
    p.legend.click_policy = "mute" 
    return(p)



# Show Bokeh

from bokeh.layouts import layout
from bokeh.models.widgets import Tabs, Panel
time = ['month', 'day', 'weekday', 'hour']
tabs = []
for t in time:
    df__ = create_df(t)
    p__ = create_bokeh(df__,t)
    l__ = layout([[p__]])
    tabs.append(Panel(child=l__,title=t))
ftabs = Tabs(tabs=tabs)
st.bokeh_chart(ftabs, use_container_width=True)

st.markdown("### Spatial Data")
'''
Text for spatial data
'''
st.markdown("### Machine Learning")
'''
Text for machine learning
'''
st.markdown("### Conclusion")
'''
Text for conclusion
'''

st.markdown("### Referrences")
'''
[1]: Marine Protected Areas provide more cultural ecosystem services than other adjacent coastal areas
Emily Erskine,1 Rosie Baillie,1 and David Lusseau1
'''