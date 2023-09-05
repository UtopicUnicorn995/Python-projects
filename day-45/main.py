from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "lxml")
# html.parser does not work on all websites, use lxml

print(soup.title.string)
# <soup.title.title> Gets the element name
# <soup.title.string> Gets the content of the elment

print(soup.prettify())
# Adds indentations in the html content
