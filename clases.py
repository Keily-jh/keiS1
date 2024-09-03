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
        if len(args) > 0:
            self.peso -= args [0] / 8
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
    def calular_imc(self):
        return self.peso / (self.estatura * self.estatura)
    def __str__(self):
        return 'Atleta (nombre = {}, peso = {}, estatura={})'.format( self.nombre, self.peso, self.estatura)
