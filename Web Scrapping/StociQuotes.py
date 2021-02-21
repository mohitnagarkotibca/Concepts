# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:41:17 2020

@author: HP
"""

from bs4 import BeautifulSoup 
from urllib.request import urlopen as uReq  
import pandas as pd
quotes=[]
authors=[]
likes=[]

for page in range(1,10):
    url=f'https://www.goodreads.com/quotes/tag/stoicism?page={page}'
    uClient = uReq(url)

    soup = BeautifulSoup(uClient.read(), "html.parser")
    uClient.close()
    container= soup.find_all('div',attrs={'class':'quoteDetails'})
    for item in container:
        quotes.append(item.find('div',attrs={'class':'quoteText'}).text.split('\n')[1].strip().strip().strip('“ ”'))
        authors.append(item.span.text.strip().rstrip())
        likes.append(item.find('a',attrs={'class':'smallText'}).text.split()[0])


quotes=pd.Series(quotes)
authors=pd.Series(authors)
likes=pd.Series(likes)
df=pd.DataFrame({'Quote':quotes,'Authors':authors,'Likes':likes})













