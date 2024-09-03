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

perX= cl.persona ("Andrea", 50)
perX.caminar() #Método caminar sin argumentos
print(perX)
perX.caminar(24) #Método caminar con  1 argumento
print (perX)
perX.caminar(12, "campo")  #Método caminar con  2 argumentos
print(perX)

atlX = cl.Atleta ("Rodrigo", 75) #Constructor con dos argumentos
print (atlX)
print("IMC: {}" .format(atlX.calular_imc()))
atlX.estatura=1.73
print(atlX)
atlY = cl.Atleta("Ximena", 52, 1.60) #Constructor con tres argumentos
print(atlY)
print("IMC: {:.2f}" .format(atlY.calular_imc()))
print("IMC: {:.2f}" .format(atlX.calular_imc()))