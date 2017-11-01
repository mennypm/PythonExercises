# -*- coding: UTF-8 -*-

#Intermezzo: Estilo de codificación
# Más sobre Listas
frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
print(frutas.count('manzana'))
print(frutas.count('mandarina'))
print(frutas.index('banana'))
print(frutas.index('banana', 4)) # Encuentra el siguiente item banana comenzando de la posición 4
frutas.reverse()
print(frutas)
frutas.append('uva')
frutas.sort()
print(frutas)
print(frutas.pop())

# Usar listas como pilas
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # llega Terry
queue.append("Graham") # llega Graham
print(queue.popleft()) # el primero en llegar ahora se va
print(queue.popleft()) # el segundo en llegar ahora se va
print(queue)

# Comprensión de listas
cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)
# Es equivalente a:
#combs = []
#for x in [1,2,3]:
  #for y in [3,1,4]:
    #if x != y:
      #combs.append((x, y))

# Listas por comprensión anidadas
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
print(matriz)
transpuesta = [[fila[i] for fila in matriz] for i in range(4)]
print(transpuesta)
# Función predefinida
print(list(zip(*matriz)))

# Instrucción del quita un item de una lista dado su índice en lugar de su valor
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
# del puede usarse también para eliminar variables:
del a

# Tuplas y secuencias
t = 12345, 54321, 'hola!'
print(t[0])
print(t)
# Las tuplas pueden anidarse:
u = t, (1, 2, 3, 4, 5)
print(u)
print("Las tuplas son inmutables, pero pueden contener objetos mutables:")
v = ([1, 2, 3], [3, 2, 1])
print(v)
# También se permite la operación inversa:
x, y, z = t
print(x)
print(y)
print(z)

# Conjuntos
canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
print(canasta) # muestra que se removieron los duplicados
print('naranja' in canasta) # verificación de pertenencia rápida
print('yerba' in canasta)
# veamos las operaciones para las letras únicas de dos palabras
a = set('abracadabra')
b = set('alacazam')
print(a) # letras únicas en a
print(a - b) # letras en a pero no en b
print(a | b) # letras en a o en b o en ambas
print(a & b) # letras en a y en b
print(a ^ b) # letras en a o b pero no en ambos
# está también soportada la comprensión de conjuntos:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# DICCIONARIOS
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
# El constructor dict() crea un diccionario directamente desde secuencias de pares clave-valor:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# Las comprensiones de diccionarios se pueden usar para crear diccionarios:
{x: x ** 2 for x in (2, 4, 6)}
# Aún más sencillo cuando se trata de palabras simples
dict(sape=4139, guido=4127, jack=4098)

# TÉCNICAS DE ITERACIÓN
# Utilizando el método items()
caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
for k, v in caballeros.items():
  print(k, v)
# Utilizando la función enumerate()
for i, v in enumerate(['ta', 'te', 'ti']):
  print(i, v)
# Para iterar sobre dos o más secuencias al mismo tiempo, los valores pueden emparejarse con la función zip()
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']
for p, r in zip(preguntas, respuestas):
  print('Cual es tu {0}? {1}.'.format(p, r))
# Iterar sobre secuencia inversa
for i in reversed(range(1, 10, 2)):
  print(i)
# es más simple y seguro crear una nueva lista:
import math
datos = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
datos_filtrados = []
for valor in datos:
  if not math.isnan(valor):
    datos_filtrados.append(valor)
print(datos_filtrados)