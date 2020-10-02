from bs4 import BeautifulSoup
import requests

#loc = ("C:/IT Workshop/BeautifulSoup/HTMLSample1/asubtlegreen/index.html")
loc = ("C:/IT Workshop/BeautifulSoup/HTMLSample1.html")
with open(loc) as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup)
#prettify -> shows tabbing and structure
print(soup.prettify())
#take out title
match = soup.title
print(match)
#take out title.text
match = soup.title.text
print(match)
#take out first div
match = soup.div
print(match)
#take out first div
match = soup.find('div', class_='footer')
print(match)