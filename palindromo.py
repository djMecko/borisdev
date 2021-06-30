# si una palabra es palindroma
#primera forma
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
# segunda forma
x =input("ingresa una palabra para ver si es palindroma")
y = x[::-1]
if y == x:
    print("es una plabra palindroma")
else:
    print("no es un palindromo")
    
# ejercicio 2 si son primos o no
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
    
#ejercicios 3
x =[1,2,3,4,5,6,7,8,9]
y=int(input("ingrese un valor")
for y in x:
    if y > 10:
        print("false")
    elif y <=10:
        print("true")

lista =[1,2,3,4,5,6,7,8,9]
valor=int(input("ingresar un valor entero"))
resultado=all(n>=valor for n in lista)
print(resultado)

def tru(lista,numero):
    for numero in lista:
        if numero>= 9:
            print("false")
        else:
            print("true")
print(tru([1,2,3,4,5,6,7,8,9], 8))

#ejercicio 4

lista=[1,2,3,4,5,-1,-2,-3]
def sumar(lista):
    if lista ==[]:
        suma = 0
    else:
        suma = lista[0] + sumar(lista[1:])
    return suma
print(sumar(lista))




