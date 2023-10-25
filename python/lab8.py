import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.nike.com/t/club-fleece-mes-winterized-crew-n72KLW/FB8378-010").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find('h1', id='pdp_product_title')
title = span.text
span = soup.find("div", {"class":"product-price__wrapper css-13hq5b3"})
price = span.text
print("The item %s has a price of %s on Nike.com" % (title, price))