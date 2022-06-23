#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable
from tkinter import *


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

sub400 = []
intre400_600 = []
peste600 = []

sub400_pret = []
intre400_600_pret = []
peste600_pret = []

for i in range(numar_produse):
	if(preturi[i]<400):
		sub400.append(nume_produse[i])
		sub400_pret.append(preturi[i])
	elif(preturi[i]<600):
		intre400_600.append(nume_produse[i])
		intre400_600_pret.append(preturi[i])
	else:
		peste600.append(nume_produse[i])
		peste600_pret.append(preturi[i])

def run1():
	if(len(sub400)==0):
		text = Label(text = "Nu exista adidasi cu pretul in intervalul ales", fg = "red")
		text.pack()
	else:
		for i in range(len(sub400)):
			text = Label(text = sub400[i]+" - "+str(sub400_pret[i]), fg = "Black")
			text.pack()

def run2():
	if(len(intre400_600)==0):
		text = Label(text = "Nu exista adidasi cu pretul in intervalul ales", fg = "red")
		text.pack()
	else:
		for i in range(len(intre400_600)):
			text = Label(text = intre400_600[i]+" - "+str(intre400_600_pret[i]), fg = "Black")
			text.pack()

def run3():
	if(len(peste600)==0):
		text = Label(text = "Nu exista adidasi cu pretul in intervalul ales", fg = "red")
		text.pack()
	else:
		for i in range(len(peste600)):
			text = Label(text = peste600[i]+" - "+str(peste600_pret[i]), fg = "Black")
			text.pack()

def clear():
	text.after(100, text.destroy())

screen = Tk()
screen.title("Informatii")
screen.geometry("800x800")

welcome_text = Label(text = "Selectati suma maxima", fg = "white", bg = "grey", font = "none 12 bold")
welcome_text.pack()

buton1 = Button(text = "Sub 400", command = run1)
buton1.place(x = 10, y = 50)

buton2 = Button(text = "Intre 400 si 600", command = run2)
buton2.place(x = 10, y = 100)

buton3 = Button(text = "Peste 600", command = run3)
buton3.place(x = 10, y = 150)

buton4 = Button(text = "Clear", command = clear)
buton4.place(x = 10, y = 200)

screen.mainloop()