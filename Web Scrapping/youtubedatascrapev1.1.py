# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 07:03:53 2020

@author: HP
"""

from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.get('https://www.youtube.com/results?search_query=Khan Academy')

user_data= driver.find_elements_by_xpath('//*[@id="video-title"]')

links=[]

for x in user_data:
    links.append(x.get_attribute('href'))

df = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])

wait = WebDriverWait(driver, 10)
v_category = "CATEGORY_NAME"


for x in links:
            driver.get(x)
            v_id = x.strip('https://www.youtube.com/watch?v=')
            
            v_title = wait.until(EC.presence_of_element_located(
                           (By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
            v_description =  wait.until(EC.presence_of_element_located(
                                         (By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
            df.loc[len(df)] = [v_id, v_title, v_description, v_category]





