from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
