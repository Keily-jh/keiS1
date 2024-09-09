"""
Clases a usar en nuestros proyectos 
Fecha: 02/09/2024
Ultima modificación. 03/09/24
"""
class persona: 
    #def __init__(self, nombre, peso):
     #   self.nombre= nombre
      #  self.peso = peso
    def __init__(self, *args):
        if len (args) == 0:
            self.nombre = "Sin nombre"
            self.peso = 0
        else:
            self.nombre = args[0]
            self.peso = args [1]

    def caminar (self, *args):
        if len(args) == 1:
            self.peso -= args [0] / 8
        elif len(args) ==2:
            if (args[1]== "campo"):
                self.peso -= args[0]/6
            else:
                self.peso -= args[0]/8
        else:
            self.peso -= 0.5
    def comer (self):
        self.peso += 1
    def __str__(self):
        return 'persona (nombre= {}, peso= {})'.format(self.nombre, self.peso)

"""
Nueva clase: Atleta
"""
class Atleta(persona):
    estatura = 0.0
    def __init__(self, *args):
        super().__init__(args[0], args[1]) #Súper se refiere a 
        if len(args)== 3:
            self.estatura = args[2]
        else: 
            self.estatura = 0.0
    
    def calular_imc(self):
        if self.estatura == 0:
            return "No se puede calcular, estatura = 0"
        return self.peso / (self.estatura * self.estatura)
    def __str__(self):
        return 'Atleta (nombre = {}, peso = {}, estatura={})'.format( self.nombre, self.peso, self.estatura)

"""
Clase: Persona parametrizada
Objetivo: usar parámetros en métodos y constructor para sobrecarga
Fecha: 05/09/2024
"""
class Persona_parametrizada:
    #definir el constructor
    def __init__(self, nombre=None, peso = None):
        if nombre:
            self.nombre = nombre
        else:
            self.nombre = "Desconocido"
        if peso:
            self.peso = peso
        else: 
            self.peso= 0 
    def caminar (self, distancia=None, lugar="ciudad"):
        if distancia is not None:
            self.peso -= distancia/8
        else:
            self.peso -= 0.5
        match (lugar):
            case "campo":
                self.peso -= 0.1
            case "ciudad":
                pass
    def __str__(self):
        return 'Persona_parametrizada (nombre: {}, peso: {})'.format(self.nombre, self.peso)

"""
Clase: Clase empleado
Atributos: nombre, edad, profesión
Fecha: 05/09/2024
"""
class Empleado:
    def __init__(self, nombre ="", edad =None, profesión =None):
        self.nombre=""
        self.edad=0
        self.profesión= "Desconocida"
        if nombre: 
            self.nombre = nombre
        if edad:
            self.edad= edad
        if profesión:
            self.profesión= profesión
    def __str__(self):
        return 'Empleado (nombre: {}, edad: {}, profesión: {})'.format(self.nombre, self.edad, self.profesión)