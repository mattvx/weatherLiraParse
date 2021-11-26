import requests, sys
from bs4 import BeautifulSoup

airportCode = sys.argv[1]

def meteo(airportCode):
    page = requests.get("https://www.getmetar.com/" + airportCode)
    soup = BeautifulSoup(page.text, 'html.parser')

    if page.status_code == 200:
        title = soup.find_all('h4')[1]
        metar = soup.find_all('h4')[0]
        data1 = soup.find_all('ul')[1]

        print('---- ' + title.get_text() + ' ----\n')
        print('----' + metar.get_text() + '----\n')
        for li in data1.find_all('li'):
            print('-' + li.get_text())
    else:
        print('Airport not found!')

meteo(airportCode)
