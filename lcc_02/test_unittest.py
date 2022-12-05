import unittest
from main_LRG import cuadrado, factorial, encuentra_maximo

#Test con unittest
class TestCuadrado(unittest.TestCase):
    
    def test1(self):
        resultado=cuadrado((100))
        self.assertEqual(resultado,10000)
        
    def test2(self):
        resultado=factorial(3)
        self.assertAlmostEqual(resultado,6)
        
    def test3(self):
        resultado=factorial(0)
        self.assertAlmostEqual(resultado,1)
    
    def test4(self):
        resultado=encuentra_maximo(10,20,30)
        self.assertAlmostEqual(resultado,30)
        
    def test5(self):
        resultado=encuentra_maximo(10,20,"treinta")
        self.assertAlmostEqual(resultado,"Debes introducir números")


if __name__=='__main__':
        unittest.main()