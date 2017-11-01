# -*- coding: UTF-8 -*-

# UNA INTRODUCCIÓN INFORMAL A PYTHON
    
el_mundo_es_plano = True
if el_mundo_es_plano:
    print "¡Ten cuidado de no caer!"

# este es el primer comentario
spam = 1 # y este es el segundo comentario
 # ... y ahora un tercero
text = "# Este no es un comentario"

# NÚMEROS
#Usando Python como calculadora
2 + 2
50 - 5 * 6
(50 - 5 * 6) / 4
8 / 5 # # la división simpre retorna un número de punto flotante
17 // 3 # la división entera descarta la parte fraccional
17 % 3 # el operado % retorna el resto de la división
5 ** 2 # 5 al cuadrado
2 ** 7 # 2 a la potencia de 7
# La última expresión impresa es asignada a la variable _
impuesto = 12.5 / 100
precio = 100.50
precio * impuesto
#12.5625
#precio + _
#round(_, 2)
#Python también tiene soporte integrado para númreos complejos, y usa el sufijo j o J para indicar la parte imaginaria (por ejemplo 3+5j

# CADENAS DE CARACTERES
'huevos y pan' # comillas simples
'doesn\'t' # usa \' para escapar comillas simples...
"doesn't" # ...o de lo contrario usa comillas dobles
'"Si," le dijo.'
"\"Si,\" le dijo."
'"Isn\'t," she said.'
print('"Isn\'t," she said.')
s = 'Primerea línea.\nSegunda línea.' # \n significa nueva línea
print(s) # con print(), \n produce una nueva línea
print('C:\algun\nombre') # aquí \n significa nueva línea!
print(r'C:\algun\nombre') # nota la r antes de la comilla
print("""\
Uso: algo [OPTIONS]
 -h         Muestra el mensaje de uso
 -H         nombrehost Nombre del host al cual conectarse
""")
# Esta característica es particularmente útil cuando quieres separar cadenadas largas:
texto = ('Escribe muchas cadenas dentro de paréntesis '
'para que sean unidas.')
palabra = 'Python'
palabra[0] # caracter en la posición 0
palabra[5] # caracter en la posición 5
palabra[-1] # último caracter
palabra[-2] # ante último caracter
palabra[0:2] # caracteres desde la posición 0 (incluída) hasta la 2 (excluída)
palabra[2:5] # caracteres desde la posición 2 (incluída) hasta la 5 (excluída)
palabra[:2] + palabra[2:]
palabra[:4] + palabra[4:]
palabra[:2]
palabra[4:]
# Índices fuera de rango en rebanadas son manejados satisfactoriamente
palabra[4:42]
s = 'supercalifrastilisticoespialidoso'
print len(s)

# LISTAS
cuadrados = [1, 4, 9, 16, 25]
cuadrados[0] # índices retornan un Item
cuadrados[-3:] # rebanadas retornan una nueva lista
cuadrados + [36, 49, 64, 81, 100] # Concatenación
cubos = [1, 8, 27, 65, 125] # hay algo mal aquí
cubos[3] = 64 # reemplazar el valor incorrecto
cubos.append(216) # agregar el cubo de 6
cubos.append(7 ** 3) # y el cubo de 7
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print len(letras) # La función predefinida len() también sirve para las listas
letras[2:5] = ['C', 'D', 'E'] # reemplazar algunos valores
letras[2:5] = [] # ahora borrarlas
letras[:] = [] # borrar la lista reemplzando todos los elementos por una lista vacía
# Es posible anidar listas (crear listas que contengan otras listas)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print x[0]
print x[0][1]
print 'Series de Fibonacci:'
# la suma de dos elementos define el siguiente
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b