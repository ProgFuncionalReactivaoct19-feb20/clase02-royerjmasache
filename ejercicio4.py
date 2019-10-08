"""
	Ejemplo 4: Uso de función lambda
	@royerjmasache
"""
datos = ((30, 1.79), (25, 1.60), (35, 1.68))
dato = lambda a: a[2]
edad = lambda a: a[1] * 100
print(edad(dato(datos)))
