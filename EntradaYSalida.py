# ENTRADA Y SALIDA

s = 'Hola mundo.'
print(str(s))
print(print())
print(str(1 / 7))
x = 10 * 3.25
y = 200 * 200
s = 'El valor de x es ' + repr(x) + ', y es ' + repr(y) + '...'
print(s)
# El repr() de una cadena agrega apóstrofos y barras invertidas
hola = 'hola mundo\n'
holas = repr(hola)
print(holas)
# El argumento de repr() puede ser cualquier objeto Python:
print(repr((x, y, ('carne', 'huevos'))))

# Dos maneras de escribir cuadrados y cubos
for x in range(1, 11):
  print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
  # notar el uso de 'end' en la linea anterior
  print(repr(x * x * x).rjust(4))
for x in range(1,11):
  print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
# srt.zfill() rellena una cadena numérica a la izquierda con ceros
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
print('{0} y {1}'.format('carne', 'huevos'))
print('{1} y {0}'.format('carne', 'huevos'))
print('Esta {comida} es {adjetivo}.'.format(comida='carne', adjetivo='espantosa'))
print('La historia de {0}, {1}, y {otro}.'.format('Bill', 'Manfred', otro='Georg'))
tabla = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for nombre, telefono in tabla.items():
  print('{0:10} ==> {1:10d}'.format(nombre, telefono))

# LEYENDO Y ESCRIBIENDO ARCHIVOS
f = open('archivodetrabajo', 'w')
print(f)
f.close()
del (f)
with open('archivodetrabajo') as f:
  datos_leidos = f.read()
  for linea in f:
    print(linea, end='')
f.closed

# GUARDAR DATOS ESTRUCTURADOS
import json
my_string = json.dumps([1, 'simple', 'lista'])
print(my_string)