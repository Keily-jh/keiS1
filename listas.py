'''
Gestión de listas, colas y pilas
Fecha: 23/09/2024
'''
#declaración de una lista
alumnos = []
print (alumnos)
#agregar valores a la lista
alumnos.append('Juan')
alumnos.append('Rosa')
alumnos.append('María')
alumnos.append('José')
alumnos.append('Luis')
print(alumnos)
#mostrar los elementos en forma iterativa
for i in range(len(alumnos)):
    print (alumnos[i])
#quitar un elemento de la lista
#sentencia del <<elem>>
#lista.pop()   # elimina el último elemento sin parámetro o lo que se le indique
alumnos.pop()
print(alumnos)
alumnos.pop(2)
print(alumnos)
del alumnos[0]
print(alumnos)
#Modificar un elemento de la lista
alumnos[0] += " María"
print(alumnos)

#Prueba de pila y cola:
from clases_lista import lista, cola, pila
cursos = pila()
cursos.poner('TDS1')
cursos.poner('ADS')
cursos.poner('BD1')
cursos.poner('BD2')
print(cursos.mostrar())
cursos.sacar() # saca el último elemento porque es pila
print(cursos.mostrar())

escuelas = cola()
escuelas.poner('Ingeniería')
escuelas.poner('Medicina')
escuelas.poner('Derecho')
escuelas.poner('Biología')
print(escuelas.mostrar())
escuelas.sacar() #saca el primer elemento porque es cola 
print(escuelas.mostrar())
