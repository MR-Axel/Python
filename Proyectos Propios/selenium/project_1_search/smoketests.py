from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTests
from searchtests import SearchTests

#variables con las que se irán cargando los CPs
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)  #clase de assertions.py
search_test = TestLoader().loadTestsFromTestCase(SearchTests)  #clase de searchtests.py

smoke_test = TestSuite([assertions_test, search_test])  #listas de vars donde se cargaron las pruebas

kwargs = {  #indicar parámetros para generar el reporte a través de un diccionario
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)   #para generar el reporte deseado
runner.run(smoke_test)