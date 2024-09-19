'''
PACTICA 01
FECHA: 19/09/2024
ALUMNA: SOPLIN ORDOÑEZ KEILY JHAMYLET
CODIGO: 202411882
'''
class Soplin_Persona:
    def __init__(self, soplin_nombre, soplin_distancia_recorrida):
        self.soplin_nombre = soplin_nombre
        self.soplin_distancia_recorrida = soplin_distancia_recorrida
    def soplin_caminar (self):
        pass
    def __str__(self):
        return f'Persona => soplin_nombre: {self.soplin_nombre} soplin_distancia_recorrida: {self.soplin_distancia_recorrida}'

class Soplin_Atleta(Soplin_Persona):
    def __init__(self, soplin_nombre, soplin_distancia_recorrida, soplin_calorías_consumidas):
        super().__init__(soplin_nombre, soplin_distancia_recorrida)
        self.soplin_calorías_consumidas = soplin_calorías_consumidas
    def soplin_entrenar(self, km):
        self.soplin_calorías_consumidas -= km/500 #imprime reserva actual
    def soplin_competir(self, km):
        self.soplin_calorías_consumidas -= km/750
    def __str__(self):
        return super().__str__() + f'soplin_calorías_consumidas: {self.soplin_calorías_consumidas}'

#prueba
atl1 = Soplin_Atleta('Joel', 10, 10)
atl2 = Soplin_Atleta('jhamy', 20, 80)
atl1.soplin_entrenar(20)
print("Atleta: "+ atl1.soplin_nombre + ", distancia recorrida:  " + str(atl1.soplin_distancia_recorrida) + " calorías consumidas: " + str(atl1.soplin_calorías_consumidas))