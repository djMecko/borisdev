# [1, 2, 3] =>  1 + 4 + 9 => 14
def sumaOfSquares(lista):
	return sum([x**2 for x in lista])

print(sumaOfSquares([1,2,3]))

# (1, 2, 5) => (x, -x)
def generalFormule(a, b, c):
	if ((b**2)-4*a*c) < 0:
  		return 0, 0
	else:
	  	x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
	  	x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
		return x1, x2

print(generalFormule(1,2,3))

# [1, 3, 4, 6] => 1 - 3 + 4 - 6 => -4
def sumAndSubstract(lista):
	total = 0
	for i, item in enumerate(lista):
		if i%2 == 0:
			total += item
		else:
			total -= item
	return total

print(sumAndSubstract([1, 3, 4, 6]))

# [1, 2, 2, 1] => True
# [1, 2, 3, 1] => False
def isPalindromo(lista):
	lista2 = lista
	lista2.reverse()
	return lista == lista2

print(isPalindromo([1,2,2,1]))

# [0,0,0,0,0,0] => True
# [0,0,0,0,1,0] => False
def isZeros(lista):
	for item in lista:
		if item != 0:
			return False;
	return True

print(isZeros([0,0,0,0]))

# [1, 2, 1, 1, 1] => False
# [2, 2, 2, 2, 2] => True
def areEquals(lista):
	firstelement = lista[0]
	for item in lista:
		if item != firstelement:
			return False;
	return True

print(areEquals([2,2,2,2,2,2]))
# ("camita", "cam") => True
# ("camita", "ita") => True
# ("camita", "mta") => False
def isSubString(word, substring):
	return substring in word

print(isSubString("cancha","can"))