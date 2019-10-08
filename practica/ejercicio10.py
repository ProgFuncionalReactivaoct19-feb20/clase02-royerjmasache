"""
	Ejercicio con función lambda: Tercera potencia
	@royerjmasache
"""
# Creación de estructura
lista = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
# Función lambda para elevar al cubo
potencia = lambda a: a ** 3
# Presentación de resultados
print(list(map(potencia, lista)))