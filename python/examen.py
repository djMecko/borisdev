# Ingresaran 2 listas y un numero que puede ser 1 o -1
# Como resultado la funcion debe restornar una lista con los elementos maximos o minimos
# en cada posicion segun sea la opcion enviada en el tercer parametro.

# ejemplo1:

# ([1,5,3], [2,3,4], 1) => [2,5,4] # Retorna el mayor en cada posicion
# ([1,5,3], [2,3,4], -1) => [1,3,3] # Retorna el menor en cada posicion

# ejemplo2:

# ([3,4,5], [1,9,2], 1) => [3,9,5] # Retorna el mayor en cada posicion
# ([3,4,5], [1,9,2], -1) => [1,4,2] # Retorna el menor en cada posicion

def selectorlist(list1, lista2, option):
	return