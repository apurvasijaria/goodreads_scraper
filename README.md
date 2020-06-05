# goodreads_scraper
Codes to scrape information about [Goodreads](https://www.goodreads.com/) reader's shelf, books stats, reviews, author's info etc. using Beautiful Soup

## Modules:
- __[shelf_scrape.py](#module-1-shelf_scrapepy)__ : Extracts information of all book on a user's particular shelf.
    <br /> - _[books_on_shelf](#books_on_shelf)_
- __[author_scrape.py](#module-2-author_scrapepy)__: Extracts infomation about the author, books by the author, quotes by the author.
 <br /> - _[about_author](#about_author)_
 <br /> - _[books_by_author](#books_by_author)_
 <br /> - _[quotes_by_author](#quotes_by_author)_
- __[books_scrape.py](#module-3-books_scrapepy)__: Extracts information about the book and quotes from the book (other information like similar books, highlights etc WIP)
 <br /> - _[about_book](#about_book)_
 <br /> - _[quotes_from_book](#quotes_from_book)_
 

## Module 1: shelf_scrape.py

### *books_on_shelf*
Extracts information of all the books on a user's particular shelf

###### Information extracted:
- Bookname
- Author name
- Date Added to the shelf
- Book image url
- Average Rating on Goodreads
- Goodreads url of book 
- ISBN Information
- Number of Pages
- Date published

```python
import books_on_shelf from shelf_scrape

#define userid and shelf name
g_id = '42442765-apurva-sijaria' #'1234-firstname-lastname'
g_shelf = 'to-read'
books = 2000 #optional argument, need to be updated if book_count>1000)
books_on_shelf(g_id,g_shelf,books)
```

###### Arguments for books_on_shelf:
- **g_id**: Goodreads ID of the user (Example: 12345-firstname-lastname )
- **g_shelf**: shelf name 
  - Common shelves:
    - **Read**: 'read'
    - **Currently Reading**: 'currently-reading'
    - **Want to Read**: 'to-read'
    - **All** - 'all'
  - User Specific shelves:
    - to be named as it is, without any change
    - example: 'english-literature'/'kindle'/'audiobooks' etc
- **book_count**: optional argument, default value =1000
    
## Module 2: author_scrape.py

### *about_author*
Extracts all information about the Author

###### Information extracted:
- Information Type (Date of Birth, Twitter ID, Website etc. as per availability on Author's Goodreads page)
- Information Value

```python
import about_author from author_scrape

#define Author ID
a_id = '3472.Margaret_Atwood' #'1234.firstname_lastname'
about_author(a_id)
```

###### Arguments for about_author:
- **a_id**: Goodreads ID of the Author from Goodreads Page URL (Example: 1234.firstname_lastname )

### *books_by_author*
Extracts information of all the books by an Author

###### Information extracted:
- Bookname
- Author names
- Average Rating on Goodreads
- Total Ratings count for the book
- Number of editions
- Date published

```python
import books_by_author from author_scrape

#define author ID and book count
a_id = '3472.Margaret_Atwood' #'1234.firstname_lastname'
books = 2000 #optional argument, need to be updated if book_count>500)
books_by_author(a_id,books)
```

###### Arguments for books_by_author:
- **a_id**:  Goodreads ID of the Author from Goodreads Page URL (Example: 1234.firstname_lastname )
- **book_count**: optional argument, default value =500

### *quotes_by_author*
Extracts all Quotes by the Author

###### Information extracted:
- Quote
- Author name and Book Title
- Total Likes on the quote

```python
import quotes_by_author from author_scrape

#define Author ID
a_id = '3472.Margaret_Atwood' #'1234.firstname_lastname'
quotes_by_author(a_id)
```

###### Arguments for quotes_by_author:
- **a_id**: Goodreads ID of the Author from Goodreads Page URL (Example: 1234.firstname_lastname )

## Module 3: books_scrape.py

### *about_book*
Extracts all information about a book

###### Information extracted:
- Information Type (ISBN, Date Published, Editions, Number of Pages etc. as per availability on the Book's Goodreads page)
- Information Value

```python
import about_book from books_scrape

#define Book ID
b_id = '38447.The_Handmaid_s_Tale' #example
about_book(b_id)
```

###### Arguments for about_book:
- **b_id**: Goodreads ID of the Book from book's main page url 

### *quotes_from_book*
Extracts all quotes from a book

###### Information extracted:
- Quote
- Author name and Book Title
- Total Likes on the quote

```python
import quotes_from_book from books_scrape

#define Book ID
b_id = '1119185-the-handmaid-s-tale'
quotes_from_book(b_id)
```

###### Arguments for quotes_from_book:
- **b_id**: Goodreads ID of the Book from book's quotes page url 

## Resources:

- **[Goodreads](https://www.goodreads.com/)**
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**
- **[HTML Parser](https://docs.python.org/3/library/html.parser.html)**
