from bs4 import BeautifulSoup
import requests

request = requests.get("https://news.ycombinator.com/news")
yc = request.text
soup = BeautifulSoup(yc,'html.parser')


article_text = soup.find(name="span", class_="titleline").find("a").get_text()
article_link = soup.find(name="span", class_="titleline").find("a").get("href")
article_votes = soup.find(name="span", class_="score").get_text()
print(article_text)
print(article_link)
print(article_votes)


# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.header.h1.string)
# find all anchor tags
# all_tags = soup.find_all(name="a")
# for tag in all_tags:
#     print(tag.get("href"))

# find the about section
# tag_about = soup.find(name="h2", id="about")
# print(tag_about)

# find the contents with class name "subtext"
# targets = soup.find_all(name="p", class_="subtext")
# for target in targets:
    # print(target.get_text())
    # pass

# use drill down
# header = soup.select_one("header h1")
# print(header)

# about = soup.select_one(selector="#about")
# print(about)

# class_subtext = soup.select(selector=".subtext")
# print(class_subtext)
