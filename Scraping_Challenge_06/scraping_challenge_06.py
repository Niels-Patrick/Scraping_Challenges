import requests
from bs4 import BeautifulSoup

# Extracting the page
URL = "https://quotes.toscrape.com/tableful/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Filtering the page to get the tags
results = soup.find("table")
tags_list = results.find_all("a")

# Creating a string list of the tags on the page
tags = []
for i in range(10, len(tags_list)-1):
    tags.append(tags_list[i].get_text(strip=True))

# Creating a set of tags without duplicates
unique_tags = set(tags)

# Counting the number of occurences of a tag and comparing it with the previous tag
# to get the most common one
counter = 0
most_common_tag = ""
for tag in unique_tags:
    tag_count = tags.count(tag)

    if counter < tag_count:
        counter = tag_count
        most_common_tag = tag

# Printing the most common tag in the console
print(f"The most common tag on the page is: {most_common_tag}")
