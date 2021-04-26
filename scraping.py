# -*- coding: utf-8 -*-
import pandas as pd
import requests

from bs4 import BeautifulSoup

base_url = 'https://ipon.hu/shop/termek/'
product_links = []
product_prices = []

# az összes oldalon végig iterálva elmentjük a linkeket és az árakat
for page in range(1, 22):
    r = requests.get(f'https://ipon.hu/shop/group/4055/product/data?page={page}')
    data = r.json()
    items = data['items']
    
    # a termék linkeket és a termék árakat hozzáadjuk a tömbökhöz
    for i in range(len(items)):
        product_links.append(base_url + data['items'][i]['slug'] + '/' + str(data['items'][i]['id']))
        product_prices.append(data['items'][i]['grossPrice'])

# a linkeken található információkat eltároljuk
ssd_array = []
for idx, link in enumerate(product_links):
    # print(idx, ' ', link)
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    
    # termék neve
    name = ' '.join(soup.find('h2', class_='product__title').text.split())
    
    # termék specifikációit tartalmazó táblázat
    try:
        table = soup.find('table', attrs={'class':'product-table'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        
        values_array = []
        cols_array = []
        for row in rows:
            cols = row.find_all('td')
            cols_array.append(' '.join(cols[0].text.split()))
            values_array.append(' '.join(cols[1].text.split()))
    except:
        continue
    
    # dictionary az adatok párosításához
    ssd = {}
    ssd['Megnevezés'] = name
    for i in range(len(cols_array)):
        ssd[cols_array[i]] = values_array[i]
    ssd['Ár (FT)'] = product_prices[idx]
    
    ssd_array.append(ssd)

# kimentjük az adatokat
df = pd.DataFrame(ssd_array)
df.to_csv('ssd.csv', index=False, encoding='utf-8')

