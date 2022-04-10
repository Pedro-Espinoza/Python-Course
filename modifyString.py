"""
Modify Strings
Python tiene un conjunto de métodos integrados que puede usar en cadenas.

Mayúsculas

Ejemplo
El método upper() devuelve la cadena en mayúsculas:
"""
a = 'Hello, World!' 
print(a.upper())

"""
Minúscula
El método lower() devuelve la cadena en minúsculas:
"""
a = 'Hello, World!'
print(a.lower())

"""
Eliminar espacios en blanco
El espacio en blanco es el espacio antes y/o después del texto real, muy a menudo se desea eliminar este espacio.

Ejemplo
El método strip() elimina cualquier espacio en blanco desde el principio o el final: 
"""
a = ' Hello, World! '
print(a.strip()) # returns 'Hello, World'

"""
Reemplazar cadena

Ejemplo
El método replace() reemplaza una cadena con otra cadena:
"""
a = 'Hello, World!'
print(a.replace('H', 'J'))

"""
Cadena dividida
El método split() devuelve una lista donde el texto entre el separador especificado se convierte en los elementos de la lista.

Ejemplo
El metodo split() divide la cadena en subcadenas si encuentra instancias del separador:
"""
a = 'Hello, World!'
print(a.split(',')) # returns ['Hello', ' World!'] 


