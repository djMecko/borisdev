# add n to elements of the list
def increment(lista, n):
	return [item + n for item in lista]

# substract n to elements of the list
def decrement(lista, n):
	return [item - n for item in lista]

# Reduce the size of list to the first n elements
def cutlist(lista, firstn):
	return lista[:firstn]

# Sum in increments
# example1: [1,2,3] => [1, 1+2, 1+2+3] => [1,2,6]
# example2: [1,3,9] => [1, 1+3, 1+3+9] => [1,4,13]
def incrementalsum(lista):
	newlist = []
	counter = 0
	for item in lista:
		counter += item
		newlist.append(counter)
	return newlist

assert(increment([2,3,4],1) == [3,4,5])

assert(decrement([2,3,4],1) == [1,2,3])

assert(cutlist([2,3,4,5],2) == [2,3])
assert(cutlist([2,3,4,5],3) == [2,3,4])

assert(incrementalsum([1,2,3]) == [1,3,6])
assert(incrementalsum([1,3,9]) == [1,4,13])
