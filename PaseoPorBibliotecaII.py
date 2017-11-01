# PASEO POR LA BIBLIOTECA II

#FORMATO DE SALIDA
import reprlib
print(reprlib.repr(set('supercalifragilisticoespialidoso')))

# GENERADOR DE IMPRESIONES CON FORMATO
import pprint
t = [[[['negro', 'turquesa'], 'blanco', ['verde', 'rojo']], [['magenta', 'amarillo'], 'azul']]]
pprint.pprint(t, width=30)

import textwrap
doc = """El método wrap() es como fill(), excepto que devuelve una lista de strings en lugar de una gran string con saltos de línea como separadores."""
print(textwrap.fill(doc, width=40))

import locale
print(locale.setlocale(locale.LC_ALL, ''))
conv = locale.localeconv() # obtener un mapeo de convenciones
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))

# PLANTILLAS

from string import Template
t = Template('${village} folk send $$10 to $cause.')
print(t.safe_substitute(village='Nottingham', cause='the ditch fund'))

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
print(t.safe_substitute(d))

"""
Cambiar el delimitador de las plantillas, de $ a %
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
  delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
  base, ext = os.path.splitext(filename)
  newname = t.substitute(d=date, n=i, f=ext)
  print('{0} --> {1}'.format(filename, newname))
"""

# MULTI HILOS
"""
import threading, zipfile
class AsyncZip(threading.Thread):
  def __init__(self, arch_ent, arch_sal):
    threading.Thread.__init__(self)
    self.arch_ent = arch_ent
    self.arch_sal = arch_sal
  def run(self):
    f = zipfile.ZipFile(self.arch_sal, 'w', zipfile.ZIP_DEFLATED)
    f.write(self.arch_ent)
    f.close()
    print('Terminó zip en segundo plano de: ', self.arch_ent)

seg_plano = AsyncZip('misdatos.txt', 'miarchivo.zip')
seg_plano.start()
print('El programa principal continúa la ejecución en primer plano.')
seg_plano.join() # esperar que termine la tarea en segundo plano
print('El programa principal esperó hasta que el segundo plano terminara.')
"""

# El módulo logging
import logging
logging.debug('Información de depuración')
logging.info('Mensaje informativo')
logging.warning('Atención: archivo de configuración %s no se encuentra', 'server.conf')
logging.error('Ocurrió un error')
logging.critical('Error crítico -- cerrando')

# REFERENCIAS DÉBILES

import weakref, gc
class A:
  def __init__(self, valor):
    self.valor = valor
  
  def __repr__(self):
    return str(self.valor)

a = A(10) # crear una referencia
d = weakref.WeakValueDictionary()
d['primaria'] = a # no crea una referencia
print(d['primaria']) # traer el objeto si aún está vivo
del a # eliminar la única referencia
print(gc.collect()) # recolección de basura justo ahora
# d['primaria'] # la entrada fue automáticamente eliminada

# Array
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

# Collections
from collections import deque
d = deque(["tarea1", "tarea2", "tarea3"])
d.append("tarea4")
print("Realizando", d.popleft())

# Módulo bisect
import bisect
puntajes = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(puntajes, (300, 'ruby'))
print(puntajes)

# Módulo heapq
from heapq import heapify, heappop, heappush
datos = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(datos) # acomodamos la lista a orden de heap
heappush(datos, -5) # agregamos un elemento
print([heappop(datos) for i in range(3)]) # traemos los tres elementos menores

# Aritmética de punto flotante decimal
from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(0.70 * 1.05, 2))
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)
print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10) == 1.0)
getcontext().prec = 36
print(Decimal(1) / Decimal(7))