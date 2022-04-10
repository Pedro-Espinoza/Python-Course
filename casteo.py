"""
Casting en Python
Especificar un tipo de variable

Puede haber ocasiones en las que desee especificar un tipo en una variables. 
Esto se puede hacer con casting. 
Python es un lenguaje orientadoo a objetos y, como tal, utiliza clases para definir tipos de datos, incluidos sus tipos primitivos.

Por lo tanto, la conversión en python  se realiza mediante funciones de constructor:

*int(): contruye un número entero a partir de un literal entero, un literal flotante(eliminando todos los decimales) o  un literal de cadena(siempre que la cadena represente un número entero).
*float(): contruye un número flotante a partir de un literal entero, un literal flotante o un literal de cadena(siempre que la cadena represente un flotante o entero).
*str(): contruye una cadena a partir de una amplia variedad de tipos de datos, incluidas cadenas, literales enteros y literales flotantes.

Ejemplo enteros: 
"""
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

"""
Ejemplo float:
"""
a = float(1) # a will be 1.0
b = float(2.8) # b will be 2.8
c = float("3") # c will be 3.0
d = float("4.2") # d will be 4.2

"""
Ejemplo string:
"""
e = str("s1") # e will be 's1'
f = str(2) # f will be '2'
g = str(3.0) # g will be '3.0'
