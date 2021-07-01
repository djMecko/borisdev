#ejercicio numero 1
def add(lista,n):
    
    for w in lista:
        print(w)
    return lista.append(n)
    
n = int(input("ingrese un valor"))

print(add([1,2,3,4,5,6,],n))
        
#otra forma
x = [1,2,3,4,5,6,7,8,9]
p =input("ingrese una palabra")
x.append(p)
for g in x:
    print(g)
    
# ejercicio numero 2
u =[1,2,3,4,5,6,7,8,9,10]
k=0
for i in u:
    u[k] -= 1
    k+=1
print(u)

# ejercicio numero 3

x =[1,2,3,4,5,6,7,8,9]
n =int(input("ingrese en indice que desea borrar"))
x.pop(n)
print(x)
#metodo 2
x =[1,2,3,4,5,6,7,8,9]
del x[1:8]
print(x)

#ejercicio 4
o = [1,2,3,4,5,6,7,8,9]
r = 0
for t in o:
    r=r+t
    print(r)
print(r)
#solo sumar pracial o total