"""
	Ejercicio con función lambda: Cadena personalizada
	@royerjmasache
"""
# Función anónima que acumula cadena
cadena = lambda a: "%s es la capital de %s" % (a[0], a[1])
# Presentación de resultados
print(cadena(["Cuenca", "Azuay"]))
