from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Seting up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Opening the webpage
url = "https://quotes.toscrape.com/js-delayed/page/5/"
driver.get(url)

# Waiting for page to load
driver.implicitly_wait(15)

try:
    # Finding the first quote element by its class name
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    # Selecting the fifth quote
    fifth_quote = quotes[4]

    # Extracting the quote text and author
    quote_text = fifth_quote.find_element(By.CLASS_NAME, "text").text

    print(f"Fifth quote: {quote_text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
