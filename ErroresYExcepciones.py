# ERRORES Y EXCEPCIONES

# ERRORES DE SINTAXIS
#while True print('Hola mundo')

# MANEJANDO EXCEPCIONES
while True:
  try:
    x = int(input("Por favor ingrese un número: "))
    break
  except ValueError:
    print("Oops! No era válido. Intente nuevamente...")
class B(Exception):
  pass

class C(B):
  pass

class D(C):
  pass

for cls in [B, C, D]:
  try:
    raise cls()
  except D:
    print("D")
  except C:
    print("C")
  except B:
    print("B")

def esto_falla():
  x = 1/0
# La declaración raise permite al programador forzar a que ocurra una excepción específica
try:
  raise NameError('Hola')
except NameError:
  print('Voló una excepción!')
  # Si necesitas determinar cuando una excepción fue lanzada pero no quieres manejarla, raise permite relanzarla:
  #raise

try:
  esto_falla()
except ZeroDivisionError as err:
    print('Manejando error en tiempo de ejecución:', err)

# EXCEPCIONES DEFINIDAS POR EL USUARIO

class Error(Exception):
  """Clase base para excepciones en el módulo."""
  pass

class EntradaError(Error):
  """Excepción lanzada por errores en las entradas.
  
  Atributos:
    expresion -- expresión de entrada en la que ocurre el error
    mensaje -- explicación del error
  """
  
  def __init__(self, expresion, mensaje):
    self.expresion = expresion
    self.mensaje = mensaje

class TransicionError(Error):
  """Lanzada cuando una operacion intenta una transicion de estado no
  permitida.
  
  Atributos:
    previo -- estado al principio de la transición
    siguiente -- nuevo estado intentado
    mensaje -- explicación de por qué la transición no está permitida
  """
  def __init__(self, previo, siguiente, mensaje):
    self.previo = previo
    self.siguiente = siguiente
    self.mensaje = mensaje

# DEFINIENDO ACCIONES DE LIMPIEZA
def dividir(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("¡división por cero!")
  else:
    print("el resultado es", result)
  finally:
    print("ejecutando la clausula finally")
    
dividir(2, 1)
dividir(2, 0)