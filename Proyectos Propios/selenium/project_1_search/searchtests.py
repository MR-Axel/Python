import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome (executable_path = r'C:/Python38/Webdriver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()    #limpia el campo

        search_field.send_keys('tee')   #escribe en el campo
        search_field.submit()   #envía el dato

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()
