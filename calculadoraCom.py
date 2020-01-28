from sys import stdin
import math
tupla1 = [10,0]
tupla2 = [-6.08,-28.56]

vector1 = [[6,3],[0,0],[5,1],[4,0]]
vector2 = [[3,-4.5],[4,6],[0,2]]

mat1 = [ [ [6,3], [3,-4.5] ] , [ [0,0], [4,6] ]  ]
mat2 = [ [ [1,0], [2,-4.5] ] , [ [8,21], [0,8] ] , [ [5,1], [0,2] ] ]

def adicionMatrices(mat1, mat2):
    c = []
    for i in range (len(mat1)):
        if len (mat1[i]) == len (mat2[i]):
            c.append(adicionVectores(mat1[i], mat2[i]))
        else:
            print('suma no posible')

    return c

def inversaMatrices(mat1):
    c = []
    for i in range(len(mat1)):
        c.append(inversaVectores(mat1[i]))
    
    return c

def multiplicacion_escalar_matriz(tupla1, mat1):
    c = []
    for i in range(len(mat1)):
        c.append(multiplicacionEscalar(tupla1, mat1[i]))

    return c

def matTranspuesta (mat1):
    c = []
    for i in range(len(mat1[0])):
        aux = []
        for j in range(len(mat1)):
            aux.append(mat1[j][i])
        c.append(aux)
        
    print(c)
    
            

###### Vectores

def multiplicacionEscalar(tupla1, vector1):
    c = []
    for i in range(len(vector1)):
        c.append(multiplicar(tupla1, vector1[i]))

    return c

def  inversaVectores(vector1):
    c = []
    for i in range(len(vector1)):
        aux = []
        for j in range(len(vector1[i])):
            aux.append(vector1[i][j]*-1)
        c.append(aux)
        
    return c

def adicionVectores(vector1, vector2):
    c = []
    if len(vector1) == len (vector2):
        for i in range(len(vector1)):
            c.append(suma(vector1[i], vector2[i]))
    else:
        print('Esta adicion no es posible de realizar')
    return c

###### Operaciones

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
            suma(tupla1, tupla2)
            opc = int(stdin.readline().strip())
        elif opc == 2:
            resta(tupla1, tupla2)
            opc = int(stdin.readline().strip())
        elif opc == 3:
            multiplicar(tupla1, tupla2)
            opc = int(stdin.readline().strip())
        elif opc == 4:        
            dividir(tupla1, tupla2)
            opc = int(stdin.readline().strip())
        elif opc == 5:
            modulo(tupla1)
            opc = int(stdin.readline().strip())
        elif opc == 6:
            conjugado(tupla1)
            opc = int(stdin.readline().strip())
        elif opc == 7:
            convertor(tupla1)
            opc = int(stdin.readline().strip())
        elif opc == 8:
            adicionVectores(vector1, vector2)
            opc = int(stdin.readline().strip())
        elif opc == 9:
            inversaVectores(vector1)
            opc = int(stdin.readline().strip())
        elif opc == 10:
            multiplicacionEscalar(tupla1,vector1)
            opc = int(stdin.readline().strip())
        elif opc == 11:
            adicionMatrices(mat1,mat2)
            opc = int(stdin.readline().strip())
        elif opc == 12:
            inversaMatrices(mat1)
            opc = int(stdin.readline().strip())
        elif opc == 13:
            multiplicacion_escalar_matriz(tupla1,mat1)
            opc = int(stdin.readline().strip())
        elif opc == 14:
            matTranspuesta(mat2)
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
    print("8 adicion de vectores")
    print("9 inversa del vector")
    print("10 multiplicacion escalar por vector")
    print("11 adicion de matrices")
    print("12 inversa de la matriz")
    print("13 multiplicacion escalar matriz")
    print("14 transpuesta de una matriz")
    print("0 salir")
    menu()

main()
