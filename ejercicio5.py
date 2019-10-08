"""
	Ejemplo 5: Uso de función lambda
	@royerjmasache
"""
datos = (
		(100, 170),
		(200, 180),
		)
edades = lambda a: a[0]
estatura = lambda a: a[1]
funcion = lambda a: (edades(a)/12.0, estatura(a)/100)
print(list(map(funcion, datos)))
