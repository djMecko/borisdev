def concat(l1, l2):  # [1,2,3], [2,3] => [1,2,3,2,3]
	return l1 + l2

def findList(l, n): # [1,2,4,6], 8 => false, [1,2,4,8], 8 => true
	return n in l

def counter(lista, number): # [1,2,1,6], 1 => 2, [1,2,1,6], 2 => 1 
	count = 0;
	for item in lista:
		if item == number:
			count += 1
	return count

def power(lista, number): # [1,2,1,6], 2 => [1,4,1,36]
	return [pow(item, number) for item in lista]

def power2(lista, number):
	result = []
	for item in lista:
		result.append(item**number)
	return result

assert(concat([1,2,3],[4,5,6]) == [1,2,3,4,5,6])

assert(findList([1,2,4,6],8) == False)
assert(findList([1,2,4,8],8) == True)

assert(counter([1,2,1,6],1) == 2)

assert(power([1,2,1,6],2) == [1,4,1,36])
assert(power2([1,2,1,6],2) == [1,4,1,36])
