
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import os
import time
import re

def books_by_author(a_id,books =500):
    today_date = datetime.datetime.now()
    bookname =[]
    author =[]
    avgrating=[]
    totalratings=[]
    editions=[]
    datepub =[]
    pgs = int(books/30)+1
    for i in range(1,pgs):
        page_link = ''.join([" https://www.goodreads.com/author/list/",a_id,"?page=",str(i),"&per_page=30"])  
        try:
            page_response = requests.get(page_link, timeout=10)
        except:
            time.sleep(5)
            continue
        print (''.join(["Crawling page: ",str(i)," Remaining: ",str(pgs-i)]))
        page_content = BeautifulSoup(page_response.content, "html.parser")    
        allbooks = page_content.findAll('tr',attrs={"itemtype":"http://schema.org/Book"}) 
        for x in allbooks:
            x_info = x.find('td',attrs = {"width":"100%"})
            try:
                bookname.append(x_info.find('span').text.strip())
            except (AssertionError,IndexError):
                bookname.append(0)
                continue
            try:
                author.append(', '.join([a.text for a in x_info.find('span',attrs = {"itemprop":"author"}).findAll('span',attrs = {"itemprop":"name"})]))
            except (AssertionError,IndexError):
                author.append(0)
                continue
            try:
                avgrating.append(x_info.find('span',attrs = {"class":"minirating"}).text.split('—')[0].strip().split(" ")[0])
            except (AssertionError,IndexError):
                avgrating.append(0)
                continue
            try:
                totalratings.append(x_info.find('span',attrs = {"class":"minirating"}).text.split('—')[1].strip().split(" ")[0])
            except (AssertionError,IndexError):
                totalratings.append(0)
                continue
            try:
                editions.append(x_info.find('span',attrs = {"class":"greyText smallText uitext"}).text.strip().split("\n")[-1].strip().split(" ")[0])
            except (AssertionError,IndexError):
                editions.append(0)
                continue
            try:
                datepub.append(x_info.find('span',attrs = {"class":"greyText smallText uitext"}).text.strip().split("\n")[3].strip())
            except (AssertionError,IndexError):
                datepub.append(0)
                continue
    author_books = pd.DataFrame({'bookname': bookname ,'author': author ,'avgrating': avgrating ,'totalratings': totalratings ,'editions': editions,'datepub': datepub})
    author_books.to_csv(''.join([a_id,"_books_",str(today_date.strftime("%b%Y")),".csv"]))
    print("--------------------------")
    print("Books info available, ",len(author_books['bookname'])," books found")
    print("Book Information Extracted")
    
def quotes_by_author(a_id):
    today_date = datetime.datetime.now()
    quotes =[]
    title =[]
    likes = []
    page_link = ''.join(["https://www.goodreads.com/author/quotes/",a_id])
    page_response = requests.get(page_link, timeout=10)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    pgs = int((int(page_content.find('span',attrs = {'class':'smallText'}).text.strip().split(" ")[-1].replace(",", "")))/30)
    for i in range(1,pgs+1):
        page_link = ''.join(["https://www.goodreads.com/author/quotes/",a_id,"?page=",str(i)])
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
    author_quotes = pd.DataFrame({'quotes': quotes ,'title': title ,'likes': likes})
    author_quotes.to_csv(''.join([a_id,"_quotes_",str(today_date.strftime("%b%Y")),".csv"]))
    print("--------------------------")
    print("All Quotes available, ",len(author_quotes['quotes'])," quotes found")
    print("Quotes Extracted")
    
def about_author(a_id):
    title = []
    info =[]
    today_date = datetime.datetime.now()
    page_link = ''.join(["https://www.goodreads.com/author/show/",a_id])  
    print (page_link)
    try:
        page_response = requests.get(page_link, timeout=10)
    except:
        time.sleep(5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    try:
        title.append('Author Name')
        info.append(page_content.find("h1",attrs={'class':'authorName'}).text.strip())
    except:
        info.append(0)
    try:
        title.append('followers')
        info.append(int(re.findall('\d+', page_content.findAll("h2",attrs={'class':'brownBackground'})[0].text.replace(",",""))[0]))
    except:
        info.append(0)
    alltitles = page_content.findAll("div",attrs ={'class':'dataTitle'})
    allinfo =page_content.findAll("div",attrs ={'class':'dataItem'})
    for t in alltitles:
        try:
            title.append(t.text)
        except:
            title.append(0)
    for i in allinfo:
        try:
            info.append(i.text.strip())
        except:
            info.append(0)
    about_class = ''.join(["freeTextContainerauthor",a_id.split(".")[0]])
    try:
        title.append('about')
        info.append(page_content.find("span",attrs = {'id':about_class}).text)
    except:
        info.append(0)
    author_info = pd.DataFrame({'title': title ,'info': info})
    author_info.to_csv(''.join([a_id,"_info_",str(today_date.strftime("%b%Y")),".csv"]))
    print("--------------------------")
    print("All Info available, ",len(author_info['title'])," information found")
    print("Author Info Extracted")
    
    