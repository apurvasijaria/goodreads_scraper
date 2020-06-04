# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:11:07 2020

@author: a.sijaria
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import os
import time
import re


def about_book(b_id):
    title = []
    info =[]
    today_date = datetime.datetime.now()
    page_link = ''.join(["https://www.goodreads.com/book/show/",b_id])  
    print (page_link)
    try:
        page_response = requests.get(page_link, timeout=10)
    except:
        time.sleep(5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    try:
        title.append('Book Name')
        info.append(page_content.find("h1",attrs={'id':'bookTitle'}).text.strip())
    except:
        info.append(0)
    try:
        title.append('Book Series')
        s = page_content.find("h2",attrs={'id':'bookSeries'}).text
        info.append(s[s.find("(")+1:s.find(")")])
    except:
        info.append(0)
    try:
        title.append('Authors')
        s = page_content.find("div",attrs={'id':'bookAuthors'}).text
        info.append(s[s.find("by")+2:].strip())
    except:
        info.append(0)
    try:
        title.append('Rating')
        info.append(page_content.find("span",attrs={'itemprop':'ratingValue'}).text.strip())
    except:
        info.append(0)
    try:
        title.append('Total Ratings')
        info.append(page_content.find("meta",attrs={'itemprop':'ratingCount'}).text.strip().split("\n")[0])
    except:
        info.append(0)
    try:
        title.append('Total Reviews')
        info.append(page_content.find("meta",attrs={'itemprop':'reviewCount'}).text.strip().split("\n")[0])
    except:
        info.append(0)
    try:
        title.append('Summary')
        info.append(page_content.find("div",attrs={'id':'description'}).text.strip())
    except:
        info.append(0)
    try:
        title.append('Edition Format')
        info.append(page_content.find("span",attrs={'itemprop':'bookFormat'}).text.strip())
    except:
        info.append(0)    
    try:
        title.append('Edition Info')
        info.append(page_content.find("span",attrs={'itemprop':'bookEdition'}).text.strip())
    except:
        info.append(0)     
    try:
        title.append('Pages')
        info.append(page_content.find("span",attrs={'itemprop':'numberofPages'}).text.strip())
    except:
        info.append(0) 
    
    otherinfo = page_content.find("div",attrs ={'id':'bookDataBox'})
    allinfo = otherinfo.findAll("div",attrs = {'class':'clearFloats'})
    for i in allinfo:
        try:
            title.append(i.find("div",attrs = {'class':'infoBoxRowTitle'}).text.strip())
        except:
            title.append(0)
        try:
            info.append(i.find("div",attrs = {'class':'infoBoxRowItem'}).text.strip())
        except:
            info.append(0)
    book_info = pd.DataFrame({'title': title ,'info': info})    
    book_info.to_csv(''.join([b_id,"_info_",str(today_date.strftime("%b%Y")),".csv"]))
    print("--------------------------")
    print("All Info available, ",len(book_info['title'])," information found")
    print("Book Info Extracted")
    
def quotes_from_book(b_id):
    today_date = datetime.datetime.now()
    quotes =[]
    title =[]
    likes = []
    page_link = ''.join(["https://www.goodreads.com/work/quotes/",b_id])
    page_response = requests.get(page_link, timeout=10)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    pgs = int((int(page_content.find('span',attrs = {'class':'smallText'}).text.strip().split(" ")[-1].replace(",", "")))/30)
    for i in range(1,pgs+1):
        page_link = ''.join(["https://www.goodreads.com/work/quotes/",b_id,"?page=",str(i)])
        try:
            page_response = requests.get(page_link, timeout=10)
        except:
            print("skipped a page")
            time.sleep(5)
            continue
        print (''.join(["Crawling page: ",str(i)," Remaining: ",str(pgs-i)]))
        #page_response = requests.get(page_link, timeout=10)
        page_content = BeautifulSoup(page_response.content, "html.parser")    
        allquotes = page_content.findAll('div',attrs={"class":"quote"}) 
        for q in allquotes:
            try:
                quotes.append(q.find('div',attrs = {"class":"quoteText"}).text.strip().split("\n")[0])
            except:
                quotes.append(0)
            try:
                title.append(q.find('span',attrs = {"class":"authorOrTitle"}).text.strip())
            except:
                title.append(0)
            try:
                likes.append(q.find('a',attrs = {"class":"smallText"}).text.split(" ")[0])
            except:
                likes.append(0)
    book_quotes = pd.DataFrame({'quotes': quotes ,'title': title ,'likes': likes})
    book_quotes.to_csv(''.join([a_id,"_quotes_",str(today_date.strftime("%b%Y")),".csv"]))
    print("--------------------------")
    print("All Quotes available, ",len(book_quotes['quotes'])," quotes found")
    print("Quotes Extracted")