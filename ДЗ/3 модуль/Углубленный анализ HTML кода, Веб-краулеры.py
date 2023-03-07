from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://docs.python.org/3/library/index.html")
bs = BeautifulSoup(html,"html.parser")

links = bs.find_all("div",{"class":"toctree-wrapper compound"})