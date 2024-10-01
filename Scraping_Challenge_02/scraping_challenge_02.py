import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

# Logging in the Quotes to Scrapes website
basic = HTTPBasicAuth('user', 'pass')
requests.get('https://quotes.toscrape.com/login', auth=basic)

page_counter = 1

# Extraction of the html code of the homepage
URL = "https://quotes.toscrape.com/"
page = requests.get(URL)

# Parsing the navigation pager
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("nav")
pager_next = results.find("li", class_="next")
url_next = pager_next.find("a")["href"]

# Counting the total number of pages on the website
while url_next != "":

    page_counter += 1

    # Searching next page url
    next_page_url = URL+url_next
    page = requests.get(next_page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("nav")
    # Checks if there is a "next" button. If not, then the program exits the while loop
    if results.find("li", class_="next"):
        pager_next = results.find("li", class_="next")
        url_next = pager_next.find("a")["href"]
    else:
        break

# Displays in the console the total number of pages
print("Number of pages:", page_counter)
