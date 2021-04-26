# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 05:31:16 2020

@author: HP
"""

#selenium for Moving around and automate the beahviour of a website
#BeautifulSoup for extracting information
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    
    
#beautifull soup good for extracting html content
from bs4 import BeautifulSoup
import urllib.request


#delay=10 Seconds
wait= webDriverWait(driver,delay)

#wait untill the following elements is loaded-- untill the website is loaded then scrap
#entire form
wait.untill(EC.presence_of_all_elements_located(By.ID,'Searchform') )    

#every box in grid has result row
posts=driver.find_elements_by_Class_name('result-row')
#it will return what type of object they are

so,    
    
posts= driver.find_elements_by_Class_name('result-row')
titles=[]
for post in posts:
    titles.append(post.text)
    

#using beautiful soup
# loading all html content in a variable
url_list=[]
html_page= urllib.request.urlopen(self.url)
soup= BeautifulSoup(html_page,'lxml')# will throw warnings if not used lxml

#fininf elements within the the soup-- in this way it makes easier
for link in soup.findAll('a',{'class':'result-title hdrnlink'}):
    print(link)

    
--------------------------------------------------------------------
Data Science Dojo:

Beautiful Soup:
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")

page_soup.h1 # it will grab the first header


uClient.close()

1- Find the outer container ,so that you can loop
# finds each product from the store page
#Each product contain info after the product: eg: photo,price,stars,etc
containers = page_soup.findAll("div", {"class": "item-container"})
# find all Div --> that has class: item-container
#it will return the HTML of the area
#

2-containers[0] will five the html code of first item

3- 
item= container[0]
item.a['class']

x=item.findAll('li',{'li':'item-shipping'})
x[0].text


----------------------------------------------
    
Beautiful Soup compete:
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
#Each product contain info after the product: eg: photo,price,stars,etc
containers = page_soup.findAll("div", {"class": "item-container"})

# name the output file to write to local disk
out_filename = "graphics_cards.csv"
# header of csv file to be written
headers = "brand,product_name,shipping \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

# loops over each product and grabs attributes about
# each product
for container in containers:
    # Finds all link tags "a" from within the first div.
    make_rating_sp = container.div.select("a")

    # Grabs the title from the image title attribute
    # Then does proper casing using .title()
    brand = make_rating_sp[0].img["title"].title()

    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    product_name = container.div.select("a")[2].text

    # Grabs the product shipping information by searching
    # all lists with the class "price-ship".
    # Then cleans the text of white space with strip()
    # Cleans the strip of "Shipping $" if it exists to just get number
    shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    # prints the dataset to console
    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

    # writes the dataset to file
    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

f.close()  # Close the file
---End of code---

    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    