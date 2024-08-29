#Crear la clase persona y comparar datos pra dos objetos persona 
class Persona:
    #Atributos o propiedades declarados
    nombre = ""
    apellido = ""
    peso = 0
    #Métodos u operaciones 
    def comer(self):
        self.peso += 1
    def caminar(self):
        self.peso -= 0.5
#Realizar operaciones con clases y objetos
persona1 = Persona()
persona2 = Persona()
print(persona1.nombre + ", " + persona1.apellido + ", peso: " + str(persona1.peso))
#asignar valores a las propiedades
persona1.nombre= "María"
persona1.apellido = "Ramos"
persona1.peso = 55

persona2.nombre= "Juan"
persona2.apellido = "Perez"
persona2.peso = 70
print(persona1.nombre + ", " + persona1.apellido + ", peso: " + str(persona1.peso))
#usar los métodos de la clase 
persona1.comer()
persona1.comer()

persona2.caminar()
print(persona1.nombre + ", " + persona1.apellido + ", peso: " + str(persona1.peso))
print(persona2.nombre + ", " + persona2.apellido + ", peso: " + str(persona2.peso))


