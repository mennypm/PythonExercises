# -*- coding: UTF-8 -*-

i = 256*256
print('El valor de i es', i)

a, b = 0, 1
while b < 1000:
  print(b, end=',')
  a, b = b, a+b

print('\n')
# MÁS HERRAMIENTAS PARA CONTROL DE FLUJO

# LA SENTENCIA if
x = int(input("Ingresa un entero, por favor: "))
if x < 0:
  x = 0
  print('Negativo cambiado a cero')
elif x == 0:
  print('Cero')
elif x == 1:
  print('Simple')
else:
  print('Más')

# LA SENTENCIA FOR
palabras = ['gato', 'ventana', 'perro']
for p in palabras:
  print(p, len(p))
for p in palabras[:]: # hace una copia por rebanada de toda la lista
    if len(p) > 6:
      palabras.insert(0, p)
print(palabras)

# LA FUNCIÓN RANGE
for i in range(5):
  print(i)
print(range(5, 10))
print(range(0, 10, 3))
print(range(-10, -100, -30))
a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
  print(i, a[i])
print(list(range(5)))

# LAS SENTENCIAS BREAK, CONTINUE Y ELSE EN LOS LAZOS
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'es igual a', x, '*', n//x)
      break
  else: # sigue el bucle sin encontrar un factor
    print(n, 'es un numero primo')

# La declaración continue, también tomada de C, continua con la siguiente iteración del ciclo
for num in range(2, 10):
  if num % 2 == 0:
    print("Encontré un número par", num)
    continue
  print("Encontré un número", num)

# Se usa normalmente para crear clases en su mínima expresión:
#class MyEmptyClass:
#  pass

def initlog():
  pass # Recuerda que debes implementar esto

# DEFINIENDO FUNCIONES
def fib(n): # escribe la serie de Fibonacci hasta n
  """Escribe la serie de Fibonacci hasta n."""
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
    print()
 
fib(2000)

def fib2(n): # devuelve la serie de Fibonacci hasta n
  """Devuelve una lista conteniendo la serie de Fibonacci hasta n."""
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a) # ver abajo
    a, b = b, a+b
  return result
f100 = fib2(100) # llamarla
print (f100) # escribir el resultado

# Argumentos con valores por omisión
def pedir_confirmacion(prompt, reintentos=4, recordatorio='Por favor, intente nuevamente!'):
  while True:
    ok = input(prompt)
    if ok in ('s', 'S', 'si', 'Si', 'SI'):
      return True
    if ok in ('n', 'no', 'No', 'NO'):
      return False
    reintentos = reintentos - 1
    if reintentos < 0:
      raise ValueError('respuesta de usuario inválida')

# Los valores por omisión son evaluados en el momento de la definición de la función
i = 5
def f(arg=i):
  print(arg)
i = 6
print(f())

def f(a, L=[]):
  L.append(a)
  return L
print(f(1))
print(f(2))
print(f(3))

# Si no se quiere que el valor por omisión sea compartido entre subsiguientes llamadas, se pueden escribir la función así
def f(a, L=None):
  if L is None:
    L = []
  L.append(a)
  return L

# Listas de argumentos arbitrarios
def concatenar(*args, sep="/"):
  return sep.join(args)

print(concatenar("tierra", "marte", "venus"))
print(concatenar("tierra", "marte", "venus", sep = "."))

# Desempaquetado de una lista de argumentos
list(range(3, 6)) # llamada normal con argumentos separados
args = [3, 6]
list(range(*args)) # llamada con argumentos desempaquetados de la lista

# Del mismo modo, los diccionarios pueden entregar argumentos nombrados con el operador **
def loro(tension, estado='rostizado', accion='explotar'):
  print("-- Este loro no va a", accion, end=' ')
  print("si le aplicas", tension, "voltios.", end=' ')
  print("Está", estado, "!")

d = {"tension": "cinco mil", "estado": "acabado", "accion": "VOLAR"}
loro(**d)

# Expresiones Lambda
def hacer_incrementador(n):
  return lambda x: x + n
f = hacer_incrementador(42)
print(f(0))
print(f(1))

# CADENAS DE TEXTO DE DOCUMENTACIÓN
def mi_funcion():
  """No hace mas que documentar la funcion.
  
  No, de verdad. No hace nada.
  """
  pass

print(mi_funcion.__doc__)

# ANOTACIÓN DE FUNCIONES
def ann(jamon: str, huevos: str = 'huevos') -> str:
  print("Anotaciones:", ann.__annotations__)
  print("Argumentos:", jamon, huevos)
  return jamon + ' y ' + huevos
ann('carne')