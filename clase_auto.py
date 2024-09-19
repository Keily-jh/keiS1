#Simula el funcionamiento de un auto
class Auto:
    #función para definir el constructor
    def __init__(self, marca, disp_gasolina):
        self.marca = marca
        self.disp_gasolina = disp_gasolina

    #funciones para definir los métodos
    def avanzar(self, km):
        self.disp_gasolina -= km / 40
    def retroceder (self, km):
        self.disp_gasolina -= km / 20
#crear objetos

auto1 = Auto("Toyota", 15)
auto2 = Auto("Ford", 10)
print("Auto1: " + auto1.marca + ", Gas: "+ str(auto1.disp_gasolina))
print("Auto2: " + auto2.marca + ", Gas: "+ str(auto2.disp_gasolina))

#recorrer los autos
auto1.avanzar(130)

auto2.avanzar(160)
print("Auto1: " + auto1.marca + ", Gas: "+ str(auto1.disp_gasolina))
print("Auto2: " + auto2.marca + ", Gas: "+ str(auto2.disp_gasolina))