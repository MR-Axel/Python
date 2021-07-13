import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguagesOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome (executable_path=r'C:/selenium/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element_by_id('select-language'))

        self.assertEqual(3, len(select_language.options))

        #Chequeo que las opciones en el listado sean iguales a las que puse manualmente
        for option in select_language.options:
            act_options.append(option.text)
        self.assertListEqual(exp_options, act_options)

        #Chequeo que la primera opción coincida
        self.assertEqual('English', select_language.first_selected_option.text)

        #Selecciono la primera opción por el texto y compruebo si está en la URL correctamente
        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)

        #Selecciono otra opción por su index
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)