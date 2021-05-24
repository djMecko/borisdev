# ejercicio 1
x = int(input("ingrese su edad"))
if x >= 18:
    print("es usted mayor de edad")
else:
    print("es usted menor de edad")
    
# ejercicio 2

x = "contraseña"
y =input("ingrese la contraseña")

if x == (y) :
    print("la contraseña coincide por lo tanto es correcto")
else:
    print("su contraseña no coincide")
    
# ejercicio 3

x = int(input("ingrese un primer numero"))
y = int(input("ingrese un segundo numero"))

if y == 0:
    print("no se puede hacer la divicon")
    
else:
    print(x/y)
    
# ejercicio 4

x = int(input("ingrese un numero entero"))
if x % 2 ==0 :
    print("es un numero par")
else:
    print("es un numero impar")
    
# ejercicio 5

x = int(input("ingrese su edad"))
y = int(input("ingrese sus ingresos mensuales"))

if (x > 16 and y > 1000):
    print("usted debe tributar")
else:
    print("usted no tiene la edad ni el sueldo para tributar")
    
#ejercicio 6
 m = input ( "ingrese su nombre ")
genero = input("¿Cuál es tu sexo (M o H)? ")
if genero == "M":
    if m.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if m.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

# ejercicio 7

renta = float(input("¿Cuál es tu renta anual? "))
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')

# ejercicio 8 

bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))


    