# las matrizes
a= [
    [10,15,78],
    [7,5,1],
    [8,6,4]
]
b=[
    [874,56,7],
    [8,6,5],
    [4,1,2]
]
filas=len(a)
print(filas)
columnas=len(a[0])
print(columnas)
fil=len(b)
print(fil)
col=len(b[0])
print(col)

# suma de matriz
def sumMatrix(a, b):
    result = []
    for i in range(len(a)):  
        fila = []
        for j in range(len(a[0])):
            fila.append( a[i][j] + b[i][j])
        result.append(fila)
    return result
result = sumMatrix(a,b)
print((result))
# resta de matriz
def resMatrix(a, b):
    result = []
    for i in range(len(a)):  
        fila = []
        for j in range(len(a[0])):
            fila.append( a[i][j] - b[i][j])
        result.append(fila)
    return result
result = resMatrix(a,b)
print((result))
# suma mas un escalar
def sumMatrix(a, b,n):
    result = []
    for i in range(len(a)):  
        fila = []
        for j in range(len(a[0])):
            fila.append(( a[i][j] + b[i][j])+n)
        result.append(fila)
    return result
result = sumMatrix(a,b,10)
print((result))

