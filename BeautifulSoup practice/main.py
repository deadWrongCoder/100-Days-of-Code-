from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
page = response.text
soup = BeautifulSoup(page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_names = [value.find(name="a").getText() for value in articles]

article_links = [value.find(name="a")["href"] for value in articles]


article_scores = soup.find_all(name="span", class_="score")

for i in range(0, len(article_scores)):
    article_scores[i] = article_scores[i].getText()

print(article_names)
print(article_links)
print(article_scores)
