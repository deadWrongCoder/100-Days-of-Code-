from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
page = response.text
soup = BeautifulSoup(page, "html.parser")
article_tag = soup.find(name="span", class_="titleline")
article_name = article_tag.find(name="a").getText()
article_link = article_tag.find(name="a")["href"]
article_score = soup.find(name="span", class_="score").getText()
print(article_tag)
print(article_name)
print(article_link)
print(article_score)

