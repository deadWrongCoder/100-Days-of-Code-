from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
page = response.text
soup = BeautifulSoup(page, "html.parser")
print(soup.find(name="span", class_="titleline").getText())
print(soup.find(name="span", class_="score").getText())
