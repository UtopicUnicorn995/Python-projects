from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

article_tag = soup.select_one(".titleline a")

print(article_tag.getText())
# getText()
print(article_tag.text)
# text
print(article_tag.string)
# .string
# Results are the same

article_link = article_tag.get("href")
article_upvote = soup.find(name="span", id="score_37390184").string
print(article_link)
print(article_upvote)
