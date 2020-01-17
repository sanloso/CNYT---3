from sys import stdin
import math

def convertor(tupla1):
    la = modulo(tupla1)
    phi = math.atan(tupla1[1]/tupla1[0])
    phi = round(phi, 3)
    c = [la,phi]

    return c

def conjugado(tupla1):
    tupla1[1] = tupla1[1] * -1

    return tupla1
    
def modulo (tupla1):
    a = tupla1[0]**2
    b = tupla1[1]**2
    suma = a+b
    
    c = abs(math.sqrt(suma))
    c = round(c,3)

    return c

def dividir(tupla1, tupla2):
    aux = tupla2[:]
    aux[1] = aux[1] * -1
    res = multiplicar (tupla1, aux)
    res2 = multiplicar (tupla2, aux)
    a = res[0] / res2[0]
    b = res[1] / res2[0]
    
    c = [a, b]

    return c

def multiplicar(tupla1, tupla2):
    res1 = tupla1[0] * tupla2[0]
    res2 = tupla1[0] * tupla2[1]
    res3 = tupla1[1] * tupla2[0]
    res4 = tupla1[1] * tupla2[1]

    rest = res2 + res3
    res4 = res4 * -1

    res1 = res1 + res4

    c = [res1, rest]

    return c

def resta(tupla1, tupla2):
    restreal = tupla1[0] - tupla2[0]
    restimg = tupla1[1] - tupla2[1]
    
    c = [restreal, restimg]

    return c
    
    
def suma(tupla1, tupla2):
    
    sumreal = tupla1[0] + tupla2[0]
    sumimg = tupla1[1] + tupla2[1]

    c = [sumreal,sumimg]

    return c
    

def menu():
    opc = int(stdin.readline().strip())
    while (opc != 0):
        if opc == 1:
            tupla1 = [ float(x) for x in stdin.readline().split(",") ]
            tupla2 = [float(x) for x in stdin.readline().split(",") ]
            suma(tupla1, tupla2)
            opc = int(stdin.readline().strip())
        elif opc == 2:
            tupla1 = [ float(x) for x in stdin.readline().split(",") ]
            tupla2 = [float(x) for x in stdin.readline().split(",") ]
            resta(tupla1, tupla2)
            opc = int(stdin.readline().strip())
        elif opc == 3:
            tupla1 = [ float(x) for x in stdin.readline().split(",") ]
            tupla2 = [float(x) for x in stdin.readline().split(",") ]
            multiplicar(tupla1, tupla2)
            opc = int(stdin.readline().strip())
        elif opc == 4:
            tupla1 = [ float(x) for x in stdin.readline().split(",") ]
            tupla2 = [float(x) for x in stdin.readline().split(",") ]
            dividir(tupla1, tupla2)
            opc = int(stdin.readline().strip())
        elif opc == 5:
            tupla1 = [ float(x) for x in stdin.readline().split(",") ]
            modulo(tupla1)
            opc = int(stdin.readline().strip())
        elif opc == 6:
            tupla1 = [ float(x) for x in stdin.readline().split(",") ]
            conjugado(tupla1)
            opc = int(stdin.readline().strip())
        elif opc == 7:
            tupla1 = [ float(x) for x in stdin.readline().split(",") ]
            convertor(tupla1)
            opc = int(stdin.readline().strip())
        else:
            print("opcion incorrecta")
            break

        

def main():
    print("1 sumar")
    print("2 restar")
    print("3 multiplicar")
    print("4 dividir")
    print("5 modulo")
    print("6 conjugado")
    print("7 cartesiano a polar")
    print("0 salir")
    menu()

main()
