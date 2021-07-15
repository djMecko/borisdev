# sumar un escalar a una sola matriz 
def sumam(a,b):
    result=[]
    for i in range(len(a)):
        fila=[]
        for j in range(len(a[0])):
            fila.append((a[i][j])+b)   
        result.append(fila)
    return result
b=int(input("ingrese un numero entero a sumar a la matriz"))
result=sumam([[1,1],[2,2]],b)
print(result)

# si 2 matrizes son iguales
def same(a,b):
    if a==b:
        return True
    else:
        return False
print(same([[1,1],[1,1]],[[1,1],[1,2]]))



# ejercicio 4 si todos los elementos de una matriz son iguales
def iguales(matriz):
    matriz = iter(matriz)
    try:
        primero = next(matriz)
    except StopIteration:
        return True
    return all(primero == x for x in matriz)
print(iguales([[1,1,1],[1,1,1]]))
        








