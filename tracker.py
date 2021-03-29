# Hi, nice to meet u. My name is Daniel

# ASIN: https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number

import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
import requests
import time
from time import sleep



def check(url):
    print(f'Checking: {url}')
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

    page = requests.get(url, headers = headers)

    soup = BeautifulSoup(page.content, features="lxml")
    sleep(1)
    try:
        title = soup.find(id='productTitle').get_text().strip()
    except:
        title = 'No Title detected'
    
    try:
        price = float(soup.find(id='priceblock_ourprice').get_text().replace('.', '').replace('€', '').replace(',', '.').strip())
    except:
        price = 'No Price detected'
    
    try:
        stock = soup.find(id='availability')[0].get_text().strip()
    except:
        stock = 'No Availability detected'

    return title, stock, price
    


def main():
    print('\n\n')
    print('Welcomeeeee')
    print()

    eighties = pd.read_csv('asins.csv')
    eighties.columns = ['ASIN', 'link']

    for ele in eighties['ASIN']:
        title, availability, price = check(url = 'https://www.amazon.it/dp/' + str(ele))
        print(f'\tProduct: \t{title}')
        print(f'\tStock: \t\t{availability}')
        print(f'\tPrice: \t\t{price}\n')





if __name__ == "__main__":
    main()

