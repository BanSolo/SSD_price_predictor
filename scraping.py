# -*- coding: utf-8 -*-
import pandas as pd
import requests

from bs4 import BeautifulSoup

base_url = 'https://edigital.hu/'
url = 'https://edigital.hu/notebook-szamitastechnika/adathordozok/ssd-meghajto-c27548'

productlinks = []

for i in range(1, 8):
    r = requests.get(f'https://edigital.hu/notebook-szamitastechnika/  \
                     adathordozok/ssd-meghajto-c27548?page={i}')
    soup = BeautifulSoup(r.content, 'lxml')
    
    productlist = soup.find_all('div', class_ ='name fitIn') 
    
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(base_url + link['href'])


ssd_array = []
for link in productlinks:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    
    name = soup.find('h1', class_='main-title').text
    
    try:
        price = soup.find('strong', class_='price price--large price--discount').text.replace('Ft', '')
    except:
        pass
    try:
        price = soup.find('strong', class_='price price--large').text.replace('Ft', '')
    except:
        pass
    
    print(price)
    values_array = []
    values = soup.find_all('dd', class_='property-group__value')
    for i in values:
        values_array.append(i.text)
    
    cols_array = []
    cols = soup.find_all('dt', class_='property-group__name')
    for i in cols:
        cols_array.append(i.text)
    
    
    ssd = {}
    ssd['name'] = name
    for i in range(len(cols_array)):
        ssd[cols_array[i]] = values_array[i]
    ssd['price'] = price
            
    ssd_array.append(ssd)
    

df = pd.DataFrame(ssd_array)

df.to_csv('ssd.csv', encoding='utf-8')
