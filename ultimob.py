# ejercicio 1
palabra = input("Introduce una palabra: ")
for i in range(10):
    print(palabra)
    
# ejercicio 2

edad = int(input("¿Cuántos años tienes? "))
for i in range(edad):
    print("Has cumplido " + str(i+1) + " años")
    
# ejercicio 3
 
numero = int(input("Introduce un número entero positivo: "))
for i in range(1, numero+1, 2):
    print(i, end=", ")


# ejercicio 4

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")
    
# ejercicio 5

monto = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
for i in range(años):
    monto *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(monto, 2)))
    
#ejercicio 6

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")
    
# ejercicio 7

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
    
# ejercicio 8

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
    
# ejercicio 9

clave = "contraseña"
contraseña =""
while contraseña != clave:
    contraseña = input("Introduce la contraseña: ")
print("Contraseña correcta")

# ejercicio 10

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
    
# ejercicio 11

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])
    
#ejercicio 12

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])