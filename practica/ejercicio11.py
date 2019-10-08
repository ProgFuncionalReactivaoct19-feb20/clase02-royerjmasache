"""
	Ejercicio con función lambda: Raíz cuadrada | Cuadrado de un número
	@royerjmasache
"""
import math
# Creación de estructura
lista  = ((10, 2), (8, 7), (5, 4), (3, 11), (10, 11))
# Función anónima para calcular la raíz
raiz = lambda a: math.sqrt(a[0])
# Función anónima para elevar al cuadrado
cuadrado = lambda a: a[1] ** 2
# Función almacenadora
funcion = lambda a: (raiz(a), cuadrado(a))
# Prensentación de resultados
print(list(map(funcion, lista)))
 