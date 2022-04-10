"""
String in python

Las cadenas en python están entre comillas simples o comillas dobles.

'hola' es lo mismo que  "hola".

Puede mostrar un literal de cadena con la función print().

Ejemplo 
"""
print("Hello")
print('Hello')

"""
Asignar cadena a una variable
La asignación de una cadena a una variable se realiza con el nombre de la variable seguido de un signo igual y la cadena:
Ejemplo
"""
a = 'Hello'
print(a)

"""
Cadena multilínea
Puede asignar una cadena de varias líneas a una variable usando tres comillas:
Ejemplo
"""
a = """Lorem ipsum dolor sit amet,
consectetus adispiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """
print(a)

"""
O tres comillas simples:
Ejemplo
"""
b = '''Lorem ipsum dolor sid amet,
consectus adispiscing elit,
sed do eiusmod tempor inicida
ut labore et doore magna aliqua. '''
print(b) 
"""
Nota: en el resultado los saltos de línea se insertan en la misma posición que en el código.

Las cadenas son matrices

Como muchos otros lenguajes de programación populares, las cadenas en Python son matrices de bytes que representan caracteres Unicode.
Sin embargo, Python no tiene un tipo de datos de caracteres, un solo caractes es simplemente una cadena con una longitud 1.
Se pueden usar corchetes para acceder a elementos de la cadena.

Ejemplo 
Obtenga el carácter en la posición 1(recuerdeq que el primer carácter tiene la posición 0):

"""
c = 'Hello, World!'
print(c[1])

"""
Bucle a través de una cadena
Dado que las cadenas son matrices, podemos recorrer los caracteresde una cadena, con un bucle for.

Ejemplo
Repasa las letras de la palabra 'banana':
"""
for letra in 'banana':
	print(letra)

"""
Longitud de cadenas
Para obtener la longitud de una cadena, use la función len().

La función len() devuelve la longitud de una cadena: 
"""
d = 'Hello, society'
print(len(d))

"""
Comprobar cadena
Para verificar si una determinada frase o carácter está presente en una cadena, podemos usar la palabra clave in.

Ejemplo
Compruebe si 'free' está presente en el siguiente texto:
""" 
txt = 'The best things in life are free'
print('free' in txt)

"""
Uselo en una declaración if:
Ejemplo
Imprima solo si 'free' está presente:
"""
txt = 'The best things in life are free'
if 'free' in txt:
	print("Yes, 'free' is present.")

"""
Para determinar si una determinada frase o carácter NO está presente en una cadena, podemos usar la palabra clave not in.

Ejemplo
Compruebe si 'expensive' NO esta presente en el siguiente texto:
"""
txt = 'The best thing in life are free'
print('expensive' not in txt)

"""
Ejemplo
Imprima solo si 'expensive' no está presente:
""" 
txt = 'The best things in life are free'
if 'expensive' not in txt:
	print("NO,  'expensive' in NOT PRESENT")
