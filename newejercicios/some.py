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


# ejercicios de cadenas
# ejercicio 1
a = input("ingrese su nombre")
b = int(input("ingrese un numero entero"))
print((a + "\n") * (b))

# ejercicio 2

s = input("igrese su nombres y apellidos")
print(s.title())
print(s.lower())
print(s.upper())

# ejercicio 3

x = input("ingrese su nombre")
print("el nombre ingresado es" + (x.upper()) + "y tiene" + str(len(x)) + "letras" )

# ejercicio 4

x = input("ingrese el numero de telefono con la siguiente forma +xx-xxxxxxxxx-xx")
print("el numero ingresado es" , x[4,:-3])

# ejercicio 5

v = input("ingrese una frase")
print(v[::-1])

# ejercicio 6

f = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(f.replace(vocal, vocal.upper()))

# ejercicio 7

email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')

# ejercicio 8
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

#ejercicio 9 

fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])

#ejercicio 10
 
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))

# ejercicio 11

producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))


# ejercicios de prueva

def doble(n):
       return 2*n
print(doble(4))

def triple(n):
    return 3*n
print(triple(5))

s =[23,58,7,95,7,5]

def restar(s):
    q = 1
    for r in s:
        q *= r
    return q
print(restar(s))

