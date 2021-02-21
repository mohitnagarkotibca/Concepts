# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:01:26 2020

@author: Lenovo
"""
import time
from bs4 import BeautifulSoup 
from urllib.request import urlopen as uReq  
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#string='Data Science Tutorial'.replace(' ','+')
url=f'https://www.youtube.com/channel/UCrC8mOqJQpoB7NuIMKIS6rQ/videos'
#uClient = uReq(url)
#soup = BeautifulSoup(uClient.read(), "html.parser")
#uClient.close()
#container= soup.find_all()

driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)
for i in range(1):
    driver.execute_script('window.scrollTo(0,(window.pageYOffset+5000))')
    time.sleep(3)
data=driver.page_source    

soup = BeautifulSoup(data,"html.parser")
container= soup.find_all('div',{'id':'dismissable'})

video_titles=[]
views=[]
duration=[]
for item in container:
    video_titles.append(item.find('a',{'id':'video-title'}).text)
    views.append( item.find('span',{'class':'style-scope ytd-grid-video-renderer'}).text )
    duration.append(item.find('span',{'class':'style-scope ytd-thumbnail-overlay-time-status-renderer'}).text)


df= pd.DataFrame({'video_titles':video_titles,'views':views,'duration':duration})































