# Python le permite asignar valores a múltiples variables en una linea:
# Ejemplo

x, y, z, = 'Orange', 'Banana', 'Cherry'
print(x)
print(y)
print(z)

# Un valor para múltiples variables
# Puede asignar el mismo valor a múltiplpes varibales en una linea:

x = y = z = 'Orange'
print(x)
print(y)
print(z)

# Desempaquetar una colección
# Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer los valores en variables. Esto se llama desempacar

fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x)
print(y)
print(z) 
