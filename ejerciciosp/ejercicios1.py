# ejercicio1
print("Hola mundo puppy")

# ejercicio 2
f = "Hola mundo"
print (f)

# ejercicio 3
a = input("ingrese su nombre")
print("Hola" + a)

# ejercicio 4

a = (((3+3)/(2*5))**2)
print(a)

# ejercicio 5

x = int(input("ingrese el numero de horas trabajadas"))
y = int(input("ingrese el coste por cada hora"))
paga = x*y
print("el sueldo que le corresponde es" , paga)

# ejercicio 6

n = int(input("ingrese un entero positivo"))
resultado=((n*(n+1))/2)
print(resultado)


# ejercicio 7

peso=input("ingrese su peso en kg")
altura=input("ingrese su estatura en m")
imc=round(float(peso)/float(altura)**2.2)
print("tu indice de masa corporal es" , str(imc))

# ejercicio 8

x =int(input("ingrese un numero entero"))
y = int(input("ingrese otro numero enero"))
cociente=(x/y)
residuo=(cociente*y)
print("el numero ingresado es" , x , "el segundo numero ingresado es" , y , "el cociente de esta divicion es" , cociente , "y el resididuo es" , residuo)

# ejercicio 9

cantidad=int(input("ingrese la cantidad de dinero a invertir"))
interes=int(input("ingrese el interes de cuanto es"))
años=int(input("ingrese el numero de años"))
CapitalObt = ((cantidad+interes)*(años))
print(CapitalObt)


# ejercicio 10

x = int(input("ingrese el numero total de payasos vendidos"))
y = int(input("ingrese el numero de muñecas  vendidas"))

payasos = 112
muñeca = 70
paquete= ((payasos*x) + (muñeca*y))
print("el paquete tiene un peso total de" , paquete , "debido a que su interior consta de" , x , "payasos" , y , "muñecas")

# ejercicio 11

deposito = int(input("ingrese la cantidad a invertir"))
interes= (deposito*0.4)
paño= (interes + deposito)
saño= (paño*2) 
taño=(paño*3)
print("el deposito es de" , deposito , "lo recaudado en el primer año sera" , paño , "lo recaudado segundo año sera" , saño , "lo recaudado tras 3 años es" , taño)

# ejercicio 12

barras=int(input("ingrese el numero de barras vendidas del pan no fresco"))
barrasf =int(input("ibgrese el numero de barras de pan fresco vendidas"))
panfresco = 3.49
panpasado = (panfresco - (panfresco*0.6))
coste=((barrasf*panfresco) + (barras*panpasado))
print("el coste total es " , round(coste,2))
