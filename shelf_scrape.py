# -*- coding: utf-8 -*-
"""
Created on Sun May 31 00:19:19 2020
@author: a.sijaria
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import time

today_date = datetime.datetime.now()
g_id = '42442765-apurva-sijaria'
g_shelf = 'read'

def books_on_shelf(g_id,g_shelf,books=1000):
    bookname=[]
    author=[]
    date_added=[]
    imgurl=[]
    avgrating=[]
    goodreads_url=[]
    isbn=[]
    numpg=[]
    datepub =[]
    pg = int(books/30)+1
    for i in range (1,pg):
        page_link = ''.join(["https://www.goodreads.com/review/list/",g_id,"?page=",str(i),"&per_page=30&shelf=",g_shelf,"&utf8=%E2%9C%93"])  
        try:
            page_response = requests.get(page_link, timeout=10)
        except:
            time.sleep(5)
            continue
        print (''.join(["Crawling page: ",str(i)," Remaining: ",str(pg-i)]))
        page_content = BeautifulSoup(page_response.content, "html.parser")    
        allbooks = page_content.findAll('tr',attrs={"class":"bookalike review"}) 
        for x in allbooks:
            try:
                bookname.append(x.find('td',attrs = {"class":"field title"}).find('a').text.strip())
            except:
                bookname.append(0)
            try:
                author.append(x.find('td',attrs = {"class":"field author"}).find('a').text.strip())
            except:
                author.append(0)
            try:
                date_added.append(x.find('td',attrs = {"class":"field date_added"}).find('div').text.strip())
            except:
                date_added.append(0)
            try:
                imgurl.append(x.find('img')['src'])
            except:
                imgurl.append(0)
            try:
                avgrating.append(x.find('td',attrs = {"class":"field avg_rating"}).find('div').text.strip())
            except:
                avgrating.append(0)
            try:
                goodreads_url.append(''.join(['https://www.goodreads.com',x.find('td',attrs = {"class":"field title"}).find('a')['href']]))
            except:
                goodreads_url.append(0)
            try:
                isbn.append(x.find('td',attrs = {"class":"field isbn"}).find('div').text.strip())
            except:
                isbn.append(0)
            try:
                numpg.append(x.find('td',attrs = {"class":"field num_pages"}).find('nobr').text.strip())
            except:
                numpg.append(0)
            try:
                datepub.append(x.find('td',attrs = {"class":"field date_pub"}).find('div').text.strip())
            except:
                datepub.append(0)
    g_shelf_data = pd.DataFrame({'bookname': bookname ,
    'author': author ,
    'date_added': date_added ,
    'imgurl': imgurl ,
    'avgrating': avgrating ,
    'goodreads_url': goodreads_url ,
    'isbn': isbn,
    'numpg': numpg,
    'datepub': datepub})
        
    g_shelf_data.to_csv(''.join([g_id,"_",g_shelf,"_", str(today_date.strftime("%b%Y")),".csv"]))
    print("---------------------")
    print("Shelf info available, ",len(g_shelf_data['bookname'])," books found")
    print(''.join(["Filename: ",g_id,"_",g_shelf,"_", str(today_date.strftime("%b%Y")),".csv"]))