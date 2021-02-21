# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 07:03:42 2020

@author: HP
"""

import time
from bs4 import BeautifulSoup 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import urllib.request



#Categories=['Gaming','Romance','Racing','Food','Health','UFC']
Categories=['UFC']


Id=[]
title=[]
Comments=[]
for i in range(len(Categories)):
    url=f'https://www.youtube.com/results?search_query={Categories[i]}'
    options = Options()
    options.headless = True
    driver= webdriver.Chrome(options=options)
    driver.get(url)
    data= driver.page_source
    soup= BeautifulSoup(data,'html.parser')
    container= soup.find_all('div',{'id':'dismissable'})
    for item in container:
        link= item.find('a',{'id':'video-title'})['href']
        title.append(item.find('yt-formatted-string',{'class':'style-scope ytd-video-renderer'}).text)
        driver.get('http://www.youtube.com'+link)
        item_data=driver.page_source
        soup2=BeautifulSoup(data,'html.parser')      
        Id.append(link)
        comment_container= soup2.find_all('div',{'id':'contents'})
        i=1
        com_list=[]
        for comment in comment_container:
            i+=1
            com_list.append(comment.find_element_by_xpath("//*[@id='content-text']"))
            break

        

        

    
    
    
    
    
    






































