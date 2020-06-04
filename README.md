# goodreads_scraper
Codes to scrape information about [Goodreads](https://www.goodreads.com/) reader's shelf, books stats, reviews, author's info etc. using Beautiful Soup

### Modules:
- __shelf_scrape.py__ : Extracts information of all book on a user's particular shelf.
- __author_scrape.py__: Extracts infomation about the author, books by the author, quotes by the author.
- __books_scrape.py__: Extracts information about the book and quotes from the book (other information like similar books, highlights etc WIP)

#### Module 1: shelf_scrape.py

Extracts information of all the books on a user's particular shelf

##### Information extracted:
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
g_id = '1234-firstname-lastname'
g_shelf = 'to-read'
book_count = 2000 #optional argument, need to be updated if book_count>1000)
books_on_shelf(user_id,shelf_name,book_count)
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
- **book_count**: optional argument, default value =2000
    
## Documentation : WIP

## Resources:

- **[Goodreads](https://www.goodreads.com/)**
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**
- **[HTML Parser](https://docs.python.org/3/library/html.parser.html)**
