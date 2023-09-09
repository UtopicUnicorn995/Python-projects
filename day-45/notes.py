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

all_a_tag = soup.find_all(name="a")
# Gets all a tag
print(all_a_tag)

for tag in all_a_tag:
    print(tag.get_text())
    # gets all text from a tag
    print(tag.get("href"))
    # gets all the links from the a tag

heading = soup.find(name="h1", id="name")
# gets the specific element
# first because it's just .find() method
print(heading)

section_heading = soup.find(name="h3", class_="heading")
# class is a reserverd keyword
# use class_
print(section_heading)

company_url = soup.select_one(selector="p em a")
# Can use css selectors

headings = soup.select(".heading")
# Can use id or classname
print(company_url)

print(headings)
