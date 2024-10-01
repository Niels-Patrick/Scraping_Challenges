from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Setting up the Chrome WebDriver
service = Service('C:\\Users\\tiger\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Opening the webpage
    driver.get("https://quotes.toscrape.com/scroll")

    # Scrolling down to load quotes
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scrolling down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new quotes to load

        # Calculating new scroll height and comparing with last height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Finding all quotes on the page
    quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")
    print(f"Number of quotes: {len(quotes)}")

finally:
    driver.quit()
