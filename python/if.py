def mayus(palabra):
    return palabra.upper()
def minu(palabra):
    return palabra.lower()
def ti(palabra):
    return palabra.title()
palabra=input("ingrese una palabra")
print(mayus(palabra) + "\n" + minu(palabra) + "\n" + ti(palabra))

def si(palabra,vocal):
    if vocal in palabra:
        print("true")
    else:
        print("false")
palabra=input("ingrese una palabra")
vocal=input("ingrese una voacal")
print(si(palabra , vocal))

