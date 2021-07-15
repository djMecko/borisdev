# Add one scalar to matrix A + a = B
# ([[1,1],[1,1]], 2) => [[3, 3],[3 ,3]]
# OJO: que solo es 1 matris mas 1 escalar, no dos matrices mas un escalar
def addScalar(mat, number):
    return 

# Return true if two matrix are equal, in other case return false
def areEqual(mat1, mat2):
    return

# Return true if all elements of matrix is 0
def equaltozero(mat1):
    for row in mat1:
        for item in row:
            if item != 0:
                return False
    return True

# Return true if all values of matrix are equals, in other case return false
def allElementsAreEquals(mat1):
    firstItem = mat1[0][0]
    for row in mat1:
        for item in row:
            if item != firstItem:
                return False
    return True

matrixA = [[1,1],[1,1]]
matrixB = [[0,0],[0,0]]

print(equaltozero(matrixB))
print(allElementsAreEquals(matrixA))
