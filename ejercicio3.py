"""
	Ejemplo 3: Uso de función lambda
	@royerjmasache
"""
# Cada elemento de datos tiene edad y estatura
datos = ((30, 1.79), (25, 160),(35, 1.68))
dato = lambda a: a[2]
print(dato(datos))