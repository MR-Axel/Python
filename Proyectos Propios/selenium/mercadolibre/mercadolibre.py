import csv, unittest
from logging import exception
from ddt import ddt, data, unpack
from selenium import webdriver
from time import sleep
import re

class TestingMercadoLibre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome (executable_path=r'C:/selenium/chromedriver.exe')
        driver = self.driver
        driver.get('https://mercadolibre.com/')
        driver.maximize_window()


    def test_search_switch(self):
        driver = self.driver

        country = driver.find_element_by_id('AR')
        country.click()
        sleep(3)
        
        searchbar = driver.find_element_by_name('as_word')
        searchbar.click()
        searchbar.clear()
        searchbar.send_keys('Nintendo switch')
        searchbar.submit()
        sleep(3)

        close_one = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div[2]/button[1]/span')
        close_one.click()
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(3)

        location = driver.find_element_by_xpath('//*[@id="root-app"]/div/div[1]/aside/section/dl[19]/dd[1]/a/span[1]')
        location.click()
        sleep(3)
    
        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        higher_price = driver.find_element_by_css_selector('#root-app > div > div.ui-search-main.ui-search-main--exhibitor.ui-search-main--only-products > section > div.ui-search-view-options__container > div > div > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > a > div > div')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[1]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)

            price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[1]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
            prices.append(price)


        print(articles, prices)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)