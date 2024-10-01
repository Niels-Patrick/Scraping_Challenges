from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Seting up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Opening the webpage
url = "https://quotes.toscrape.com/js/page/10/"
driver.get(url)

# Waiting for page to load
driver.implicitly_wait(10)

try:
    # Finding the first quote element by its class name
    first_quote = driver.find_element(By.CLASS_NAME, "quote")

    # Extracting the quote text and author
    quote_text = first_quote.find_element(By.CLASS_NAME, "text").text

    print(f"First quote: {quote_text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
