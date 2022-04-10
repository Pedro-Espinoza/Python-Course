"""
Las variables que se cerean fuera de una función, se conocen como variables globales.
Las variables globales pueden ser utilizadas por todos, tanto dentro como fuera de las funciones.

Ejemplo
Crear una variable fuera de una función y utilizarla dentro de la función
"""  
x = 'awesome'

def myfunc():
	print('Python is ' + x)

myfunc()

"""
Si crea una variable con el mismo nombre dentro de una función, esta variable será  local y solo se puede usar dentro de la función.
La variable global con el mismo nombre quedara como estaba, global y con el valor original.

Ejemplo
Crear una variable dentro de una función, con el mismo nombre que la variable global
"""

x = 'awesome'
def func():
	x = 'fantastic'
	print('Python is ' + x)

func()

print('Python is ' + x)

"""
Normalmente, cuando crea una variable dentro de una función, esa variable es local y solo se puede usar dentro de esa función .
Para crear una variable global dentro de una función, puede usar la palabra clave global

Ejemplo
Si usa la palabra clave global, la variable pertenece al ámbito global

"""
def globalfunc():
	global x
	x = 'fantastic'

globalfunc()

print('Python is ' + x)

"""
Además, use la palabra clave global si desea cambiar una variable global dentro de una función.

Para cambiar el valor de una variable global dentro de una función, consulte la variable usando la palabra clave global.

Ejemplo  
"""

x = 2

def cambio():
	global x
	x = 4

cambio()

print ('Cambio del valor 2 al ', x)

  
