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
 
if __name__ == '__main__':
 unittest.main()