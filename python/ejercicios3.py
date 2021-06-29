# Palindromo es cuando una palabra se lee igual de izquiera a derecha y viceversa
def isPalindromo(word):
	return

# Retorna true si todos los numeros que contiene son primos
def fullPrimes(list):
	return

# Retorna una lista de booleanos con True en todos los valores menores a un numero dado
def lessto(list, number):
	return

# Calcula el score final de un juego con las siguientes reglas:
# La lista tiene puntajes positivos y negativos
# Suma todos los valores de la lista
# Cada vez que hay un cambio de signo en el siguiente valor de la lista
# - Si cambia a positivo debera agregar 2 al resultado final
# - Si cambia a negativo debera restar 1 al resultado final
# Ejemplo 1:
# [5,10,-1] resultado sera 5 + 10 -1 = 14, un cambio de signo de +10 a -1,
# entonces restaremos 1 al resultado final 13, la funcion retornara 13
# Ejemplo 2:
# [5,-10,+15] resultado sera 5 - 10 + 15 = 10, 
# Un cambio de signo entre 5 y -10, debemos restar 1 al resultado final
# Un cambio de signo entre -10 y +15, debemos agregar 2 al resultado final
# resultado final 10 -1 +2 = 11
def finalscore(list)
	return

assert(isPalindromo("uwu") == True)
assert(isPalindromo("casa") == False)
assert(isPalindromo("kook") == True)


assert(fullPrimes([1,5,7]) == True)
assert(fullPrimes([1,5,7,9]) == False)

assert(lessto([1,5,7],6) == [True, True, False])
assert(lessto([1,5,7,9],7) == [True, True, False, False])

assert(finalscore([5,10,-1]) == 13)
assert(finalscore([5,-10,+15]) == 11)
