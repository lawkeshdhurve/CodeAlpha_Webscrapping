import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/s?k=iphone"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}
r = requests.get(url, headers=headers)
r.raise_for_status() 
soup = BeautifulSoup(r.content, 'html.parser')
title_elements = soup.select("h2.a-size-medium.a-color-base.a-text-normal, span.a-size-medium.a-color-base.a-text-normal")

if not title_elements:
    print("No titles found. Amazon's HTML structure has changed.")
    # print(soup.prettify())

for title_element in title_elements:
    print(title_element.get_text(strip=True))