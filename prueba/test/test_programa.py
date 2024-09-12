'''
Modulo de prueba unitarias para progamas.py
Fecha: 09/09/2024
'''

import unittest
from programa import suma, es_mayor

class Test_Programa(unittest.TestCase):
    #Métodos de prueba
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 4), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -4), -6)
    def test_suma_dentro_de_un_rango(self):
       self.assertIn(suma(2,5),[1,2,4,6,7])
#Desarrollar pruebas para la función "es mayor"
    def test_esmayor(self):
       self.assertTrue(es_mayor (4,2))
    def test_verifica_nomayor(self):
       self.assertFalse(es_mayor(5,10))
#Desarrollar pruebas para la división de números
 
    def test_suma_parametrizada(self):
       test_cases =[(1,2,3), (-1,-2,-3), (0,0,0), (1,-1,0)]
       for x, y, resultado in test_cases:
          with self.subTest(x=x, y=y, resultado=resultado):
             self.assertEqual(suma(x,y), resultado)
if __name__ == '__main__':
 unittest.main()