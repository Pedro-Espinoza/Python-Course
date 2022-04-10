"""
Variables
En python, las variables se crean cuando le asignas un valor.
Python no tiene ningún comando para declarar una variable.
Una variable se crea en el momento en que le asigna un valor por primera vez.
"""
x = 5
y = 'Hello world'
"""
No es necesario declarar las variables con ningún tipo en particular,
e incluso pueden cambiar de tipo después de que se hayan establecido 
"""
x = 4	# x is of type int  
print('X es de tipo ',type(x)) 
x = 'Sally'	# x is now of type str
print('X es de tipo ',type(x))
"""
Fundición
Si desea especificar el tipo de datos de una variable, puede hacerlo con la conversión .
Ejemplo
"""
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

"""
Para obtener el tipo de dato de una variable, utilizamos la función type.
Ejemplo
""" 
x = 5
y = 'John'
print(type(x))
print(type(y))
"""
Los nombres de las variables distinguen entre mayúsculas y minúsculas
Ejemplo
"""
a = 4
A = 'Sally'
print(A,' tiene ',a,'años') 
