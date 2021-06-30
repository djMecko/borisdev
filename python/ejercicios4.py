# add n to elements of the list
def increment(lista, n):
	return

# substract n to elements of the list
def decrement(lista, n):
	return

# Reduce the size of list to the first n elements
def cutlist(lista, firstn):
	return

# Sum in increments
# example1: [1,2,3] => [1, 1+2, 1+2+3] => [1,2,6]
# example2: [1,3,9] => [1, 1+3, 1+3+9] => [1,4,13]
def incrementalsum(lista):
	return

assert(increment([2,3,4],1) == [3,4,5])

assert(decrement([2,3,4],1) == [1,2,3])

assert(decrement([2,3,4,5],2) == [2,3])
assert(decrement([2,3,4,5],3) == [2,3,4])

assert(incrementalsum([1,2,3]) == [1,2,6])
assert(incrementalsum([1,3,9]) == [1,4,13])
