"""
Programa que usan las clases declaradas en el archivo clases.py
Fecha: 02/09/2024
Ultima modificación. 03/09/24
"""
import clases as cl
#Crear objetos de la clase persona 
per1 = cl.persona ("Juan", 70)
per2 = cl.persona ("María", 55)
#Asignar valor a las propiedades 
per1.peso = 75
per2.peso = 57
per2.nombre += " Elena"
#Usar los métodos
per1.caminar()
per2.comer()
per2.comer()
print (per1)
print (per2)

per1.caminar(16)
print (per1)
per1.caminar()
print (per1)
per3 = cl.persona ()

print (per1)
print (per2)
print (per3)

#Crear atletas
atl1 = cl.Atleta("José", 70)
atl2 = cl.Atleta("Rosa", 50)
print (atl1)
print (atl2)

atl1.estatura = 1.65
atl2.estatura = 1.60
print (atl1)
print (atl2)
print ('Atleta: {}, IMC = {:.2f}'.format(atl1.nombre, atl1.calular_imc()))
print ('Atleta: {}, IMC = {:.2f}'.format(atl2.nombre, atl2.calular_imc()))

