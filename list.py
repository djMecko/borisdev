#ejercicio 1 concatenar

x=[1,2,3,4,5]
y =[6,7,8,9,10]
print(x+y)

#ejercicio2 si un valor existe en una lista

x=[1,2,3,4,5]
y =[6,7,8,9,10]

z=int(input("ingrese un valor entero"))

if z in x:
    print("el valor se encuentra en la lista x")
    
elif z in y:
    print("se encuentra en la lista y")
else:
    print("su valor no se encuentra en ninguna lista")


# ejercicio 3 cuantas veces se repite un elemento en una lista

p=[1,2,3,1,2,3,5,4,1,4,5,6]
m=[1,1,2,3,4,1,2,4,5,8,4,1,2,]
frecuencia={}
for z in p:
    if z in frecuencia:
        frecuencia[z] += 1
    else:
        frecuencia[z] = 1
for w in m:
    if w in frecuencia:
        frecuencia[w] += 1
    else:
        frecuencia[w] = 1
print(frecuencia)

# ejercicio 4 potenciar a la lista

x =[1,2,3,4,5]
def potencia(x,exponente):
    contador = 1
    elevado = 1
    while contador<= exponente:
        elevado= elevado* x
        contador=contador + 1
    return elevado


print(potencia(1, 2)) 
print(potencia(2, 2))  
print(potencia(3, 2))  
print(potencia(4, 2))  
print(potencia(5, 2))

# 5 twocomponents
