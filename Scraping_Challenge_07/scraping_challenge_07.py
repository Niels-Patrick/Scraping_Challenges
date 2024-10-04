from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

# Seting up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Opening the webpage
URL = "https://quotes.toscrape.com/search.aspx"
driver.get(URL)

# Waiting for page to load
driver.implicitly_wait(10)

try:
    # Finding the author drop-down element on the page
    dropdown_author = driver.find_element(By.ID, 'author')
    # Selecting 'Albert Einstein' for the author
    select_author = Select(dropdown_author)
    select_author.select_by_visible_text('Albert Einstein')
    # Waiting for the tag dropdown to be filled (it is necessary to select the author first)
    time.sleep(5)

    # Finding the tag drop-down element on the page
    dropdown_tag = driver.find_element(By.ID, 'tag')
    # Selecting 'music' for the tag
    select_tag = Select(dropdown_tag)
    select_tag.select_by_visible_text('music')
    time.sleep(5)

    # Clicking on the search button
    search_button = driver.find_element(By.NAME, 'submit_button')
    search_button.click()
    time.sleep(5)

    # Getting the quote and printing it in the command terminal
    quote_element = driver.find_element(By.CLASS_NAME, 'content').text
    print(quote_element)
except:
    print("A problem occurred")
finally:
    driver.quit()
