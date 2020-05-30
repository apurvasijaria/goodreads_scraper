# goodreads_scraping
Codes to scrape information about reader's shelf, books stats, reviews, author's info etc. using Beautiful Soup

## Code 1: shelf_scrape.py

Extracts information of books on a user's particular shelf

### Information extracted:
- Bookname
- Author name
- Date Added to the shelf
- Book image url
- Average Rating on Goodreads
- Goodreads url of book 
- ISBN Information
- Number of Pages
- Date published

#### Information that needs to be updated in code:
- **g_id**: Goodreads ID of the user (Example: 12345-firstname-lastname )
- **g_shelf**: shelf name 
  - Common shelves:
    - **Read**: 'read'
    - **Currently Reading**: 'currently-reading'
    - **Want to Read**: 'to-read'
  - User Specific shelves:
    - to be named as it is, without any change
    - example: 'english-literature'/'kindle'/'audiobooks' etc
    
## Other codes to be updated soon 

## Resources:

- **[Goodreads](https://www.goodreads.com/)**
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**
- **[HTML Parser](https://docs.python.org/3/library/html.parser.html)**
