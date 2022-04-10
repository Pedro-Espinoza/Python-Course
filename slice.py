"""
Slicing
Puede devolver un rango de caracteres utilizando la sintaxis de división.
Especifique el índice inicial y el índice final, separados por dos puntos, para devolver una parte de la cadena.

Ejemplo
Obtenga lo caracteres de la posición 2 a la posición 5(incluidos): 
"""
b = 'Hello, world'
print(b[2:5])

"""
Cortar desde el principio
Al omitir el índice de inicio, el rango comenzará en el primer carácter:

Ejemplo 
Consigue los caracteres desde el inicio hasta la posición 5(incluidos):
"""
b = 'Hello world'
print(b[:5])

"""
Cortar hasta el final 
Al omitir el índice final, el rango ira hasta el final:

Ejemplo
"""
b = 'Hello world'
print(b[2:])

"""
Indexación negativa
Utilice índices negativos para iniciar el segmento desde el final de la cadena:

Ejemplo
"""
b = 'Hello, World!'
print(b[-5:-2])

