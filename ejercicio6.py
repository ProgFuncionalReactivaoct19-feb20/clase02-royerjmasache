"""
	Ejemplo 5: Uso de función lambda
	@royerjmasache
"""
lista = [10, 2, 3, 5, 1]
# print(min(lista, key=lambda a: a))
# print(min(lista, key=lambda a: a))
funcion = lambda a: a + 100
print(min(list(map(funcion, lista))))
