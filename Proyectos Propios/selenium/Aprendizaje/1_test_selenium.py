# Con unittest nos podemos traer todas nuestras pruebas
import unittest # Ayuda a orquestar cada una de las pruebas que estaremos, ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner # Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class HelloWorld(unittest.TestCase):    #suitecase
    
    #test fixture inicial, Realiza todo lo necesario antes de empezar la prueba
    @classmethod    # Decorador para que las distintas paginas corran en una sola pestaña
    def setUpClass(cls):    #el classmethod y cls sirve para no cerrar las ventanas
        cls.driver = webdriver.Chrome (executable_path=r'C:/selenium/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)  # esperamos 10 seg antes de realizar la siguiente accion
        #return super().setUp()

    #pruebas unitarias
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.com')

    #test fixture final, cerrando navegador
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  
        #return super().tearDown()   

if __name__ == "__main__":
    unittest.main(verbosity = 2, 
        testRunner = HTMLTestRunner(
            output = 'reportes',     #me genera reporte con el nombre mencionado
            report_name = 'hello-world-report'
            )
    )


