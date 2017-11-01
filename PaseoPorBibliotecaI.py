# Interfaz al Sistema Operativo

"""
import os
os.getcwd() # devuelve el directorio de trabajo actual
os.chdir('/server/accesslogs') # cambia el directorio de trabajo
os.system('mkdir today') # ejecuta el comando 'mkdir' en el sistema

Para administración de archivos a más alto nivel se utiliza el módulo shutil:

import shutil
shutil.copyfile('datos.db', 'archivo.db')
"""

# Comodines de Archivos
import glob
glob.glob('*.py')

# Argumentos de línea de órdenes
import sys
print(sys.argv)

# Redirección de la salida de error y finalización del programa
sys.stderr.write('Alerta, archivo de log no encontrado\n')

# Expresiones regulares
import re
print(re.findall(r'\bt[a-z]*', 'tres felices tigres comen trigo'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'gato en el el sombrero'))
print('te para tos'.replace('tos', 'dos'))

# Matemáticas
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

# Módulo random
import random
print(random.choice(['manzana', 'pera', 'banana']))
print(random.sample(range(100), 10)) # elección sin reemplazo
print(random.random()) # un float al azar
print(random.randrange(6)) # un entero al azar tomado de range(6)

# Módulo statistics
import statistics
datos = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(datos))
print(statistics.median(datos))
print(statistics.variance(datos))

# Acceso a Internet
"""
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
  for line in response:
    line = line.decode('utf-8') # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line: # look for Eastern timer
      print(line)

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('manuel.peralta@cimat.mx', 'peraltammanuel@gmail.com',
"\"\"To: manuel.peralta@cimat.mx
   From: peraltammanuel@gmail.com

   Ojo al piojo.
"\"\")
server.quit()
"""

# Fechas y tiempos
# las fechas son fácilmente construidas y formateadas
from datetime import date
hoy = date.today()
print(hoy)

# nos aseguramos de tener la info de localización correcta
import locale
print(locale.getdefaultlocale())
print(hoy.strftime("%m-%d-%y. %d %b %Y es %A. hoy es %d de %B."))

# Las fechas soportan aritmética de calendario
nacimiento = date(1994, 8, 30)
edad = hoy - nacimiento
print(edad.days)

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(t)
zlib.decompress(t)
print(zlib.crc32(s))

# Medición de rendimiento
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# Control de calidad
def promedio(valores):
  """Calcula la media aritmética de una lista de números.
  >>> print(promedio([20, 30, 70]))
  40.0
  """
  return sum(valores) / len(valores)

import doctest
print(doctest.testmod()) # valida automáticamente las pruebas integradas