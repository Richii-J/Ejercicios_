import requests
from bs4 import BeautifulSoup
#///////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/#


response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, 'html.parser')

divs = soup.select('div[Class="quote"]')
for div in divs:
    print()

if len(divs) > 0:
    # Imprimir el texto del primer div
    print("Primer div:", divs[0].text.strip())

if len(divs) > 1:
    # Imprimir el texto del 2do div
    print("2do div:", divs[1].text.strip())

if len(divs) > 2:
    # Imprimir el texto del 3er div
    print("3r div:", divs[2].text.strip())
