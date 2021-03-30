# Hi, nice to meet u. My name is Daniel

# ASIN: https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number

import pandas as pd
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import telegram, requests


def check(url):
    driver = webdriver.Chrome('./files/chromedriver')

    driver.get(url)
    product_info = {}
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//span[@id="productTitle"]')))
    try:
        title = driver.find_element_by_xpath('//span[@id="productTitle"]').text.strip()
    except:
        title = 'No Title detected'

    try:
        # "(//span[contains(@class,'a-size-medium a-color-success')])[1]"
        stock = driver.find_element_by_xpath("(//span[contains(@class,'a-size-medium a-color-success')])[1]").text.strip()
        # find if 
    except:
        try:
            stock = driver.find_element_by_xpath("(//span[contains(@class,'a-size-medium a-color-state')])[1]").text.strip()
        except:
            stock = 'Non disponibile'

    if (stock != 'Non disponibile'):
            try:
                price = driver.find_element_by_id('priceblock_dealprice').text
                price = float(price.strip('€'))
            except Exception as e:
                price = 'No Price detected'
                print(e)
    else:
        price = 'No Price'
    
    driver.quit()

    return title, stock, price
    



def alert(info, bot):
    print('Sending')
    message = info['Title'] + '\n\nUrl: ' + 'https://www.amazon.it/dp/' + info['ASIN'] + '\n\nStock: ' + info['Stock'] + '\n\nPrice: ' + info['Price']
    bot.sendMessage(chat_id = 488262439, text = message)
    print('Sent')


def start_bot():
    with open('./files/token.txt') as reader:
        token = reader.readline()
    bot = telegram.Bot(token = token)
    return bot


def main():
    print('\n\n')
    print('Welcomeeeee')
    print()

    # bot = start_bot()

    eighties = pd.read_csv('./files/asins.csv')
    eighties.columns = ['ASIN', 'link']

    while True:
        for ele in eighties['ASIN']:
            print(ele)
            title, availability, price = check(url = 'https://www.amazon.it/dp/' + str(ele))
            print(f'\tProduct: \t{title}')
            print(f'\tStock: \t\t{availability}')
            print(f'\tPrice: \t\t{price}\n')

            if (availability != 'Non disponibile'):
                if (price != 'No Price detected' and price != 'No Price'):
                    if (price < 1000):
                        print('alerting')
                        # alert({'ASIN':str(ele), 'Title':title, 'Stock':availability, 'Price':price}, bot)





if __name__ == "__main__":
    main()

