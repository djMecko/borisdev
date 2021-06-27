# calculando impares
numero = [1, 2 , 3, 4, 5 , 6 ,7, 8, 9]
def impares(lista):
    impar = []
    
    for w in lista:
        if w %2 != 0:
            impar.append(w)
            
    return impar

resultado = impares(numero)

print(resultado)
    
    
# calculando pares

def pares(listas):
    par = []
    for s in listas:
        if s %2 == 0:
            par.append(s)
    return par

resultados = pares(numero)
print(resultados)

# calculando doble
numbers = [1 , 2, 3 ,4 ,5 ,6 , 7, 8, 9,10]
def multi(numeros):
    producto = []
    for ñ in numeros:
        producto.append(ñ*2)
    return producto
print(multi(numbers))

# calculando el triple

numerales = [1 , 2, 3 ,4 ,5 ,6 , 7, 8, 9,10]
def multi(numeros):
    producto = []
    for ñ in numeros:
        producto.append(ñ*3)
    return producto
print(multi(numerales))

# calculando el cuadruple

numerotes = [1 , 2, 3 ,4 ,5 ,6 , 7, 8, 9,10]
def multi(numeros):
    producto = []
    for ñ in numeros:
        producto.append(ñ*4)
    return producto
print(multi(numerotes))


# numeros primos

numero = 1
while numero <= 10:
    contador = 1
    x = 0
    while contador<= numero:
        if numero % contador ==0:
            x = x+1
        contador = contador+1
    if x ==2:
        print(numero)
    numero=numero+1

def double_list(lista)
    return [2*x for x in lista]

def mutiply_list(lista, n)
    return [n*x for x in lista]