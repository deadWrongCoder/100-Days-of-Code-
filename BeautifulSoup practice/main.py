from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
page = response.text
soup = BeautifulSoup(page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_names = [value.find(name="a").getText() for value in articles]

article_links = [value.find(name="a")["href"] for value in articles]


article_scores = [score.getText() for score in soup.find_all(name="span", class_="score")]

article_points = [int(score.split(" ")[0]) for score in article_scores]

largest_score = max(article_points)
index = article_points.index(largest_score)
print(article_names)
print(article_links)
print(article_scores)
print(article_points)
print(largest_score)
print(article_names[index])


