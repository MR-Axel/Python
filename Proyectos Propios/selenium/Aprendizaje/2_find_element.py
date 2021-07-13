import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome (executable_path=r'C:/selenium/chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)
        
    def test_search_text_field(self):    #buscar elemento por su ID
        search_field = self.driver.find_element_by_id("search")
       
    def test_search_text_field_by_name(self):    #buscar elemento por su nombre
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_by_class_name(self):  #buscar elemento por nombre de clase
        search_field = self.driver.find_element_by_class_name("input-text required-entry")

    def test_search_button_enabled(self):    #buscar botón del campo search
        search_field = self.driver.find_element_by_class_name("button search-button")

    def test_count_of_promo_banner_images(self): #buscar lista de imágenes
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_element_by_tag_name("img")    #busco en la lista los elementos img
        self.assertEqual(3, len(banners))   #compruebo con una aserción que la longitud de banners es 3

    def test_vip_promo(self):   #buscar elemento por el xpath, cuando no se consigue otro método
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')
    
    def test_shopping_cart(self):   #buscar por css
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
