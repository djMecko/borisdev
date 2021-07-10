
def printMatrix(mat):
    for i in range(len(mat)):  
        print(mat[i])

# Add two matrix => A + B = C
def sumMatrix(mat1, mat2):
    result = []
    for i in range(len(mat1)):  
        fila = []
        for j in range(len(mat1[0])):
            fila.append( mat1[i][j] + mat2[i][j])
        result.append(fila)
    return result

result = sumMatrix([[1,1],[1,1]],[[1,1],[0,0]])
printMatrix(result)

# Substract one matrxix => A - B = C
def substracMatrix(mat1, mat2):
    return 

result = substracMatrix([[1,1],[1,1]],[[1,1],[0,0]])
printMatrix(result)

# Add one scalar to matrix A + a = B
# ([[1,1],[1,1]], 2) => [[3, 3],[3 ,3]]
def addScalar(mat, number):
    return 

result = addScalar([[1,1],[1,1]], 2)
printMatrix(result)