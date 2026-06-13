import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")

print("TOP NEWS HEADLINES\n")

for i, headline in enumerate(headlines[:5]):
    print(f"{i+1}. {headline.text}")