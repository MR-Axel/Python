import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By #ayudará a llamar excepciones

class AssertionsTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:/Python38/Webdriver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))


    def tearDown(self):
        return super().tearDown()

    #para identificar cuando está presente un elemento según sus parámetros
    #how tipo de elementos, what que es lo que tiene
    def is_element_present(self, how, what):    
        try:
            self.driver.find_element(by= how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)

