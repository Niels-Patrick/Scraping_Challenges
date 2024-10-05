import requests
from bs4 import BeautifulSoup
import time
import timeit

URL = "https://quotes.toscrape.com/random"

def scrape_quote():
    '''
    Scrape the quote displayed on the page

    return:
    quote_text: the text of the scraped quote
    '''
    try:
        # Fetching the webpage
        page = requests.get(URL)

        if page.status_code == 200:
            # Parsing the webpage
            soup = BeautifulSoup(page.content, "html.parser")
            # Getting the quote text
            quote_text = soup.find("span", class_="text").get_text()
            # Returning the quote text
            return quote_text
        
        else:
            print(f"Failed to retrieve page: Status code {page.status_code}")
            return None
        
    except:
        print("A problem occurred")

def scrape_all_quotes():
    '''
    Scrapes all the 100 quotes of the website
    '''
    quote_list = []

    try:
        # Put the quote in quote_list if the quote doesn't exists, then repeats
        # until all 100 quotes are in the list
        while len(quote_list) != 100:
            quote = scrape_quote()

            if quote:
                if quote not in quote_list:
                    quote_list.append(quote)

    except:
        print("A problem occurred")

# Measuring the time needed to scrape the entire content of the website
elapsed_time = timeit.timeit(scrape_all_quotes, number=1)

print(f"Approximate time needed to scrape the entire content of the website: {elapsed_time} seconds")
