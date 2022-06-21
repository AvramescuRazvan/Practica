from bs4 import BeautifulSoup
import requests

baseurl = "https://altex.ro"

r = requests.get('https://altex.ro/cauta/filtru/price/0-50/?q=tastaturi').text

soup = BeautifulSoup(r, 'lxml')

print(soup)

listaproduse = soup.find_all('a',class_="Product  flex flex-col relative hover:shadow-mixRedYellow")

listalink = []

for item in listaproduse:
	listalink.append(baseurl + link['href'])
	
print(listalink)




