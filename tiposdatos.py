"""
Tipos de datos incorporados
En programación, el tipo de datos es un concepto importante.

Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacer cosas  diferentes.

Python tiene los siguientes tipos de datos integrados de forma predeterminada, en estas categorías:

*Tipo de texto:		str
*Tipos númericos:	int, float, complex
*Tipos de secuencia: 	list, tuple, range
*Tipo de mapeo:		dict
*Establecer tipos:	set, frozenset
*Tipo booleano:		bool
*Tipos binarios: 	bytes, bytearray, memoryview

Obtener el tipo de datos
Puede obtener el tipo de datos de cualquier objeto utilizando la función type()

Configuración del tipo de datos
En Python, el tipo de datos se establece cuando asigna un valor de una variable:

Ejemplo						Data Type
x = 'Hello world'				str
x = 20						int
x = 20.5					float
x = 1j						complex
x = ['apple', 'banana', 'cherry'] 		list
x = ('apple', 'banana', 'cherry')		tuple
x = range(6) 					range
x = {'name' : 'John', 'age' :  36}		dict
x = {'apple', 'banana', 'cherry}		set
x = frozenset({'apple', 'banana', 'cherry'})	frozenset
x = True 					bool
x = b'Hello'					bytes
x = bytearray(5)				bytearray
x = memoryview(bytes(5))			memoryview

Configuración del tipo de datos específico
Si desea específicar el tipo de datos, puede utilizar las siguientes funciones de contrucción.

Example 					Data Type
x = str('Hello world') 				str
x = int(20)					int
x = float(20.5)					float
x = complex(1j)					complex
x = list(('apple', 'banana', 'cherry'))		list
x = tuple(('apple', 'banana', 'cherry'))	tuple
x = range(6)					range
x = dict(name='John', age=36)			dict
x = ser(('apple', 'banana', 'cherry'))		set
x = frozenset(('apple','banana','cherry'))	frozenset
x = bool(5)					bool
x = bytes(5)					bytes
x = bytearray(5)				bytearray
x = memoryview(bytes(5))			memoryview

"""
