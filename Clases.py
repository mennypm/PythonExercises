# CLASES

# EJEMPLO DE ÁMBITOS Y ESPACIOS DE NOMBRES

def prueba_ambitos():
  def hacer_local():
    algo = "algo local"
  def hacer_nonlocal():
    nonlocal algo
    algo = "algo no local"
  def hacer_global():
    global algo
    algo = "algo global"
  algo = "algo de prueba"
  hacer_local()
  print("Luego de la asignación local:", algo)
  hacer_nonlocal()
  print("Luego de la asignación no local:", algo)
  hacer_global()
  print("Luego de la asignación global:", algo)

prueba_ambitos()
print("In global scope:", algo)

class MiClase:
  """Simple clase de ejemplo"""
  i = 12345
  def f(self):
    return 'hola mundo'

x = MiClase()

class Complejo:
  def __init__(self, partereal, parteimaginaria):
    self.r = partereal
    self.i = parteimaginaria

y = Complejo(3.0, -4.5)
print('parte real =', y.r, 'parte imaginaria =', y.i)

class Perro:
  tipo = 'canino' # variable de clase compartida por todas las instancias
  
  def __init__(self, nombre):
    self.nombre = nombre # variable de instancia única para la instancia
    self.trucos = [] # crea una nueva lista vacía para cada perro
  
  def agregar_truco(self, truco):
    self.trucos.append(truco)

d = Perro('Fido')
e = Perro('Buddy')
print(d.tipo) # compartido por todos los perros
print(e.tipo) # compartido por todos los perros
print(d.nombre) # único para d
print(e.nombre) # único para e
d.agregar_truco('girar')
e.agregar_truco('hacerse el muerto')
print(d.trucos)
print(e.trucos)

class Empleado:
  pass

juan = Empleado() # Crear un registro de empleado vacío
# Llenar los campos del registro
juan.nombre = 'Juan Pistola'
juan.depto = 'laboratorio de computación'
juan.salario = 1000

# Iteradores
for elemento in [1, 2, 3]:
  print(elemento)
for elemento in (1, 2, 3):
  print(elemento)
for clave in {'uno':1, 'dos':2}:
  print(clave)
for caracter in "123":
  print(caracter)
#for linea in open("miarchivo.txt"):
#  print(linea, end='')

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) Levantaría una excepción del tipo StopIteration

# Iterar en reversa
class Reversa:
  """Iterador para recorrer una secuencia marcha atrás."""
  def __init__(self, datos):
    self.datos = datos
    self.indice = len(datos)
    
  def __iter__(self):
    return self
    
  def __next__(self):
    if self.indice == 0:
      raise StopIteration
    self.indice = self.indice - 1
    return self.datos[self.indice]

rev = Reversa('spam')
print(iter(rev))
for char in rev:
  print(char)

# Generadores
def reversa(datos):
  for indice in range(len(datos)-1, -1, -1):
    yield datos[indice]

for letra in reversa('golf'):
  print(letra)

# Expresiones generadoras
print(sum(i*i for i in range(10))) # suma de cuadrados
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec))) # producto escalar

from math import pi, sin
tabla_de_senos = {x: sin(x*pi/180) for x in range(0, 91)}
#palabras_unicas = set(word for line in page for word in line.split())
#mejor_promedio = max((alumno.promedio, alumno.nombre) for alumno in graduados)
data = 'golf'
print(list(data[i] for i in range(len(data) - 1, -1, -1)))