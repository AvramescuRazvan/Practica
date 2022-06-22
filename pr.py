#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable


r = requests.get('https://www.nike.com/ro/w/mens-shoes-3enojz4595xz7by28z7wkbpz8i2jvz8nb9wzahvdnzavc0iznik1zy7ok?sort=newesti').text

soup = BeautifulSoup(r, 'lxml')


produse = soup.find_all('a', class_='product-card__link-overlay')

link = []

for item in produse:
	link.append(item['href'])

nume_produse = []
preturi = []
culori_disponibile = []

for item in link:
	pr = requests.get(item).text
	soup = BeautifulSoup(pr, 'lxml')
	
	nume_produse.append(soup.find('h1', class_='headline-2 css-16cqcdq').text.strip())
	
	if(soup.find('div', class_='product-price css-11s12ax is--current-price css-tpaepq')):
		pret = (soup.find('div', class_='product-price css-11s12ax is--current-price css-tpaepq').text.strip())
		pret = float(pret.replace("RON", ""))
		preturi.append(pret)
	else:
		pret = (soup.find('div', class_='product-price__wrapper css-13hq5b3').text.strip())
		x = pret.split("D")
		pret = float(x[0].replace("RON", ""))
		preturi.append(pret)




	culori_disponibile.append(soup.find('li', class_='description-preview__color-description ncss-li').text.strip())	

numar_produse = len(preturi)


for i in range(numar_produse-1):
	for j in range(0, numar_produse-i-1):
		if(preturi[j]>preturi[j+1]):
			preturi[j],preturi[j+1] = preturi[j+1],preturi[j]
			culori_disponibile[j],culori_disponibile[j+1] = culori_disponibile[j+1],culori_disponibile[j]
			nume_produse[j],nume_produse[j+1] = nume_produse[j+1],nume_produse[j]
			link[j],link[j+1] = link[j+1],link[j]


f = open("Informatii.txt", "w")



table = PrettyTable(["Denumire", "Pret", "Culori Disponibile", "LInk"])

for i in range(numar_produse):
	table.add_row([nume_produse[i], preturi[i], culori_disponibile[i], link[i]])

f.write(str(table))


