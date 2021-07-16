# This function return a matrix multiplied by an scalar
# ([[1,2],[1,3]], 3) => [[3,6],[3,9]]
def multiplyByScalar(mat, number):
	return 

# Sum all elements of matrix and return this result
# [[1,2],[1,3]] => 7
def sumAllElements(mat):
	counter = 0
	for row in mat:
		counter += sum(row)
	return counter

# Sum the diagonal of matrix
# [[1,2],[1,3]] => 1 + 3 = 4
def sumDiagonal(mat):
	counter = 0
	for index, item in enumerate(mat):
		counter += mat[index][index]
	return counter

# Find an element in the matrix
# [[1,2],[1,3]], 3) => True
# [[1,2],[1,3]], 4) => False
def findElement(mat, number):
	for row in mat:
		for item in row:
			if item == number:
				return True
	return False

print(sumAllElements([[1,2],[1,3]]))

#print(sumDiagonal([[1,2],[1,3]]))

#print(findElement([[1,2],[1,3]], 4))
#print(findElement([[1,2],[1,3]], 3))

