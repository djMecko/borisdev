l=[4,2,7]
m=[5,3,6]
n=int(input("ingrese un valor +1 , -1"))
def maximin(l,m,n):
    if n ==1:
        max=[(l[i] if l[i]>m[i]  else m[i] ) for i in range(0,len(l))]
        return max
    elif n ==-1:
        min= [(l[i] if  l[i] < m[i] else m[i]) for i in range(0,len(l))]
        return min
    else:
        print("ingreso invalido")
print(maximin(l,m,n))



def selectorlist(list1, lista2, option):
	if n == 1:
		return [(l[i] if l[i]>m[i]  else m[i] ) for i in range(0,len(l))]
	elif n == -1:
		return [(l[i] if  l[i] < m[i] else m[i]) for i in range(0,len(l))]
	else:
		print("ingreso invalido")
		return None

print(selectorlist(l,m,n))