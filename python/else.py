# ejercicio 1
def pote(p):
    suma=0
    for y in p:
        suma=suma+((y**2))
    print(suma)
print(pote([1,2,3]))

#ejercicio f.general
def f_general(a,b,c):
    m=((-b+(((b**2)-(4*a*c))**0.5))/(2*a))
    return m
A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))
x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)


#ejercicio 4
def palindromo(lista):
    if str(lista)==str(lista[::-1]):
        return True
    else:
        return False
print(palindromo([1,2,2,1]))
print(palindromo([1,2,3,4]))

# ejercicio 5

def zero(lista):
    for d in lista:
        if d ==0:
            return True
        else:
            return False
    
print(zero([1,2,3,4,1]))
print(zero([0,0,0,0,0,0,0]))
print(zero([1,2,5,4,0]))

# ejercicio 6

def iqual(lista):
    if len(lista)!=len(set(lista)):
        return True
    else:
        return False
    
print(iqual([1,2,3,4,5,6]))
print(iqual([1,1,1,1,1,1]))
print(iqual([1,1,2,2,3,4,5]))

#ejercicio 7 estan no tan bien
def sub(palabra,sustr):
    for sustr in palabra:
        return True
    else:
        return False

      
    
        
        

