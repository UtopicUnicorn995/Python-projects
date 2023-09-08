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
article_upvote = soup.find(name="span", class_="score").string
print(article_link)
print(article_upvote)

articles = soup.select(".titleline a")

article_text = []
article_links = []
article_upvotes_score = []
article_upvotes = [score.string for score in soup.find_all(name="span", class_="score")]

for article in articles:
    article_links.append(article.get("href"))
    article_text.append(article.getText())

for upvote in article_upvotes:
    article_upvotes_score.append(int(upvote.split(" ")[0]))


print(article_upvotes_score)

max = 0

for num in range(len(article_upvotes_score)):
    if article_upvotes_score[num] > max:
        max = article_upvotes_score[num]
        index = num

print(article_text[index])
print(article_links[index])
