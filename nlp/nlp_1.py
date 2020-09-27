# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:09:57 2020

@author: HP
"""

import pandas as pd
variables=[]
pd.set_option('display.max_rows',1000)
data= pd.read_csv('news_dataset_v3_FE.csv')
data['content3']= data['content3'].apply(lambda x :x.lower())
variables.append('data : dataframe')
#creating a frequency count of words according to categories
freqs={}
df= data[['category','content3']]
for i in range(len(data)):
    counts= pd.Series(df['content3'].loc[i].split()).value_counts()
    category= df['category'].loc[i]
    d= dict(zip(counts.index,counts.values))
    for k,v in d.items():
        if (category,k) in freqs:
            freqs[(category,k)]= freqs[(category,k)]+ v
        else:
            freqs[(category,k)]= v
category=[]
words=[]
counts=[]
for k,v in freqs.items():
    category.append(k[0])
    words.append(k[1])
    counts.append(v)

import plotly.express as px
import plotly.graph_objects as go
data_f= pd.DataFrame({'category':category,'word':words,'count':counts})

cats= data_f.category.value_counts().index
cats_val= data_f.category.value_counts().values
fig= px.pie(names=cats,values= cats_val)
fig.show()