import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = 'C:/selenium/chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Selenium')

        self.assertEqual('Selenium', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)