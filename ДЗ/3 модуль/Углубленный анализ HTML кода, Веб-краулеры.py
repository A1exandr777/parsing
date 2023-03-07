import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://docs.python.org/3/library/index.html")
bs = BeautifulSoup(html, "html.parser")
links = bs.find_all("a")
for i in links:
    a = i.get("href")
    match = re.search(r"https.*", a)
    list = [match[0] if match else None]
    for b in range(len(list)):
        if list[b] == None:
            continue
        else:
            print(list[b])


