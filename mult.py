# multiplicado por un escalar
def mul(a,n):
    result=[]
    for i in range(len(a)):
        fila=[]
        for j in range(len(a[0])):
            fila.append((a[i][j])*n)
        result.append(fila)
    return result
n=int(input("ingrese el numero entero a multuiplicar ala matriz"))
result=mul([[1,2],[3,2]],n)
print(result)

# sumar todos los elementos de una matriz
matriz = [1, 1, 1, 1, 1]
sum = 0
for i in range(0, len(matriz)):    
   sum = sum + matriz[i];    
     
print("suma de todos los elementos de la matriz " + str(sum));    

# sumar la diagonal de una matriz
n = 3
a = [[11,2,4],[4,5,6],[10,8,-12]]
diagonal= sum(a[i][i] for i in range(n))
print(str(diagonal)) 
# si un elemento esta en una matriz true or false
matriz = [1, 2, 3]
existe = 2 in range(len(matriz))
print(existe)
True
existe = 5 in matriz
print(existe)
False






