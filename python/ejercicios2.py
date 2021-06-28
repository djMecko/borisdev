def concat(lista1, lista2):  # [1,2,3], [2,3] => [1,2,3,2,3]
	return lista1 + lista2

def find(lista, number): # [1,2,4,6], 8 => false, [1,2,4,8], 8 => true
	return

def counter(lista, number): # [1,2,1,6], 1 => 2, [1,2,1,6], 2 => 1 
	return

def power(lista, number): # [1,2,1,6], 2 => [1,4,1,36]
	return


assert(concat([1,2,3],[4,5,6]) == [1,2,3,4,5,6])

assert(find([1,2,4,6],8) == False)
assert(find([1,2,4,8],8) == True)

assert(counter([1,2,1,6],1) == 2)

assert(power([1,2,1,6],2) == [1,4,1,36])
