# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:30:03 2020

@author: HP
"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=art+and+dance+of+france&sp=EgIQAQ%253D%253D")
user_data1 = driver.find_elements_by_xpath('//*[@id="video-title"]')
links1 = []
for i in user_data1:
    links1.append(i.get_attribute('href'))

df17 = pd.DataFrame(columns = ['link', 'title', 'description', 'catagory'])
wait = WebDriverWait(driver, 10)

wait = WebDriverWait(driver, 10)
v_category = "Art & Dance"
for x in links1:
    #Extract dates from for each user on a page
    driver.get(x)
    v_id = x.strip('https://www.youtube.com/watch?v=')
    v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
    v_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
    df17.loc[len(df17)] = [v_id, v_title, v_description, v_category]\

#frames = [df_travel, df_science, df_food, df_manufacturing, df_history, df_artndance]

df_copy = pd.concat(frames, axis=0, join='outer', join_axes=None, ignore_index=True,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)
#df_copy.to_csv("/home/shubhamsingh/Desktop/df_orignal.csv", encoding='utf-8', index=False)









