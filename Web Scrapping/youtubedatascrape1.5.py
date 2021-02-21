# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:21:38 2020

@author: HP
"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup 

Categories=['Batman','Khan Academy','Keanu reevs']
#data= pd.DataFrame({'id':ids,'titles':titles,'links':links,'description':description})
data= pd.DataFrame(columns=['id','titles','links','description'])
frames=[] 
for search in Categories:
        
    url=f'https://www.youtube.com/results?search_query={search}'
    options = Options()
    options.headless = True
    driver= webdriver.Chrome(options=options)
    driver.get(url)
    data= driver.page_source
    soup= BeautifulSoup(data,'html.parser')
    
    titles_container=soup.find_all('a',{'id':'video-title'})
    titles=[]
    for title in titles_container:
        titles.append(title.text.strip('\n'))
    if '' in titles:
        titles.remove('')
    
    links=[]
    links_container= soup.find_all('a',{'id':'video-title'})
    for link in links_container:
        links.append(link['href'])    
    if '' in links:
        links.remove('')

    ids=[]
    for item in links:
        ids.append( item.strip( '/watch?v= '))
    if '' in ids:
        ids.remove('')

    description=[]
    desc_container= soup.find_all('yt-formatted-string',{'id':'description-text'})
    for desc in desc_container:
        description.append(desc.text)
    if '' in description:
        description.remove('')
    temp= pd.DataFrame({'id':ids,'titles':titles,'links':links,'description':description})
    frames.append(temp)





