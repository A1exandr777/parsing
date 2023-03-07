from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.python.org/")
bs = BeautifulSoup(html, "html.parser")
image = bs.find_all("img", {"class": "python-logo"})
t = bs.find("div", {"class": "psf-widget"})

for i in image:
    print(i["src"])  # ссылка на картинку

print(t.text.strip())  # текст из div
