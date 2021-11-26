import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.getmetar.com/LIRA")
soup = BeautifulSoup(page.text, 'html.parser')

title = soup.find_all('h4')[1]
data1 = soup.find_all('ul')[1]

print(title.get_text())

for li in data1.find_all('li'):
    print(li.get_text())
