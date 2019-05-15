import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'googlebot'}

sitemap_link = 'http://www.site.com.ua/product-sitemap.xml' # Link for sitemap.xml file

s = requests.get(sitemap_link, headers=headers)
sitemap = BeautifulSoup(s.content, 'lxml')
links = [link.find("loc").text for link in sitemap.find_all("url")]

print(links)


# Script Info

# Collect all links from xml file to list
# Python 3
# pip install install beautifulsoup4 (docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
# pip install lxml (github: https://github.com/lxml/lxml)
