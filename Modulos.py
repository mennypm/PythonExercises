# MÓDULOS

import fibo
# importa el módulo de fibo

fibo.fib(1000)
fibo.fib(100)
fibo.__name__

# Si la función es usada muy frecuentemente se puede asignar a un nombre local
fib = fibo.fib
fib(500)
# Importa los nombres del módulo directamente al espacio de nombres del módulo que hace la importación
from fibo import fib, fib2
fib(500)

import sys
sys.ps1 = 'C> '
print('Yuck!')
print(__name__)
print(dir(sys))

import builtins
print(dir(builtins))