'''
Clases Lista, pila y cola
'''
class lista:
    def __init__(self):
        self.elementos = []
    def sacar(self):
        pass
    def mostrar (self):
        return self.elementos
    def poner(self, dato):
        self.elementos.append(dato)
    def vacío(self):
        len(self.elementos) == 0
    def primero(self):
        if not self.vacío():
            return self.elementos[0]
        return "La lista está vacía"
    def último(self):
        if not self.vacío():
            return self.elementos[-1]
        return "la lista está vacía"

class pila(lista):
    def sacar(self):
        self.elementos.pop() #Elimina el último
class cola(lista):
    def sacar (self):
        self.elementos.pop(0) #Elimina el perimer elemento

