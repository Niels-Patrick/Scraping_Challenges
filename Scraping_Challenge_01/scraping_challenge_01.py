import requests
from bs4 import BeautifulSoup

# Extraction of the HTML code of the homepage of the Books to Scrape website
URL = "https://books.toscrape.com/index.html"
page = requests.get(URL)

# Parsing the book categories list
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="nav nav-list")
categories = results.find_all("li")

# Finding all category urls
category_url = []
for category in categories:
    category_url.append(category.find("a")["href"])

# Scraping process for all category pages
for i in range(1, len(category_url)): # Needs to start at index 1, because index 0 is the "all books" page
    # Extraction of the HTML code of a category page
    category = category_url[i]
    URL_category = "https://books.toscrape.com/"+category
    page_category_page = requests.get(URL_category)
    soup_page = BeautifulSoup(page_category_page.content, "html.parser")

    # Searching total number of pages for the current category
    page_total_number = 0
    page_number_html = soup_page.find("li", class_="current") # Scraping of the "Page x of y"

    # If there is only one page in the current category, there is no "Page x of y" displayed on this page
    # and if there is no "Page x of y" displayed, then it means there is only one page in the
    # current category
    if page_number_html is not None:
        page_number_string = page_number_html.text.strip()
        page_total_number_string = page_number_string[-1]
        page_total_number = int(page_total_number_string)
    else:
        page_total_number = 1

    # Creating a list of all pages URLs for the current category
    URL_pages_list = []
    if page_total_number != 1:
        URL_pages_list.append(URL_category)
        for i in range (2, page_total_number+1):
            URL_pages_list.append(URL_category.replace("index", f"page-{i}"))
    else:
        URL_pages_list.append(URL_category)

    # Scraping process for all pages in the current category
    category_name = "" # The name that will be displayed for the current category
    books_number = 0 # The total number of books that will be displayed for the current category
    prices = [] # List of prices of all books in the current category
    avg_price = 0.00 # The average price of books in the current category
    for URL_page in URL_pages_list:
        page_category_page = requests.get(URL_page)
        soup_page = BeautifulSoup(page_category_page.content, "html.parser")
        results_category = soup_page.find("ol")
        books_category = results_category.find_all("li")
    
        # Creating a list of books to count them and filling the list of prices to calculate
        # the average price in each category
        books = []
        for book in books_category:
            books.append(book.find("h3"))

            price = book.find("p", class_="price_color")
            price_string = (price.text.strip())
            prices.append(float(price_string[1:]))

        # Calculation of the number of books in the current category
        books_number += len(books)
    
    # Average price of books in the current category
    avg_price += round((sum(prices) / len(prices)), 2)
    # Name of the current category
    category_name = soup_page.find("h1")

    # Diplays the name, the total number of books and the average price for the current category
    print(category_name.text.strip(), books_number, avg_price)
