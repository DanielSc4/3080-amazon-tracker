# Hi, nice to meet u. My name is Daniel

# ASIN: https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number

import pandas as pd
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check2(url):
    driver = webdriver.Chrome('./chromedriver')

    driver.get(url)
    product_info = {}
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//span[@id="productTitle"]')))
    try:
        title = driver.find_element_by_xpath('//span[@id="productTitle"]').text.strip()
    except:
        title = 'No Title detected'

    try:
        price = driver.find_element_by_xpath("(//span[contains(@class,'a-color-price')])[1]")
    except:
        price = 'No Price detected'

    try:
        stock = driver.find_element_by_xpath('//span[@id="availability"]').text.strip()
    except:
        stock = 'No Title detected'
    
    driver.quit()

    return title, stock, price


def main():
    print('\n\n')
    print('Welcomeeeee')
    print()

    eighties = pd.read_csv('asins.csv')
    eighties.columns = ['ASIN', 'link']

    for ele in eighties['ASIN']:
        title, availability, price = check2(url = 'https://www.amazon.it/dp/' + str(ele))
        print(f'\tProduct: \t{title}')
        print(f'\tStock: \t\t{availability}')
        print(f'\tPrice: \t\t{price}\n')





if __name__ == "__main__":
    main()

