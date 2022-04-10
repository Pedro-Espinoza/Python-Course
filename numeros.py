"""
Hay tres tipos numéricos en Python
* int
* float
* complex

Las variables de tipo numérico se crean cuando les asignas un valor:

""" 
x = 1 # int
y = 2.8 # float
z = 1j #compex

# Para verificar el tipo de cualquier objeto en Python, use la función type()
print(type(x))

"""
Entero
Int o entero, es un número entero, positivo o negativo, sin decimales, de longitud ilimitad

Ejemplo  
"""
a = 1 
print(type(a))

"""
Float
Flotante, o 'numero  de punto flotante es un número, positivo o negativo que contiene una o mas decimales

Ejemplo 
"""

b = 1.10
print(type(b))

"""
El float también puede ser un número científico con una 'e' para indicar la potencia de 10.

Ejemplo
"""
c = 35e3
print(type(c))

"""
Complex
Los números complejos se escriben con una 'j' como parte imaginaria;

Ejemplo
"""
d = 3 + 5j
print(type(d))

"""
Conversión de tipo
Puede convertir de un tipo a otro con los metodos int(), float() y complex():

Ejemplo
""" 
e = 1 #int
f = 2.8 #float
g = 1j #complex

#convert from int to float
h = float(e)

#convert from float to int
i = int(f)

#convert from int to complex
j = complex(e)

print(h)
print(type(h))
print(i)
print(type(i))
print(j)
print(type(j))


