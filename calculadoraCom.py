from sys import stdin
import math
##tupla1 = [-2,9]
##tupla2 = [-3,-8]
##
##vector1 = [[1, 5], [5, 1], [-8, 8]]
##vector2 = [[6, -7], [-1, 2], [-1, -2]]
##
##mat1 = [[[3,0],[3,1]],[[3,-1],[2,0]]]
##mat2 = [[[-1, -7], [-10, 1]], [[-8, -7], [-9, -8]]]


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
    return c
    

def matrizProducto(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        c = []
        for i in range(len(mat1[0])):
            aux = []
            for j in range(len(mat2)):
                a = [0,0]
                for k in range(len(mat2[0])):
                    a = suma(multiplicar(mat1[i][k], mat2[k][j]), a)
                aux.append(a)
            c.append(aux)
        return c

def conjugadaMatriz(mat1):
    c = []
    for i in range(len(mat1)):
        c.append(conjugadoVector(mat1[i]))

    return c

def tensorMatriz(mat1, mat2):
    c = []
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            c.append(tensorVector(mat1[i], mat2[j]))
            
    return c

def igualMatriz(mat1, mat2):
    if mat1 == mat2:
        return True
    return False

def adjMatriz(mat1):
    c = conjugadaMatriz(matTranspuesta(mat1))
    return c

def idMatriz(mat1):
    for i in range (len (mat1)):
        for j in range (len (mat1 [0])):
            if mat1[i][i] == [1, 0]:
                return True
            else:
                return False

def unitariaMatriz(mat1):
    if len(mat1) == lent(mat1[0]):
        c = matrizProducto(mat1, adjMatriz(mat1))

        return idMatriz(c)

def hermitianMatriz(mat1):
    if len(mat1) == len(mat1[0]):
        aux = adjMatriz(mat1)

        c = igualMatriz(aux, mat1)

        return c

###### Vectores
def distanciaVector(vector1, vector2):
    if len(vector1) == len(vector2):
        aux = []
        c = 0
        for i in range(len(vector1)):
            aux.append(resta(vector1[i], vector2[i]))
        c += normaVector(aux)
        c = round(c,3)
        return c

def normaVector(vector1):
    c = 0
    aux = 0
    for i in range(len(vector1)):
        for j in range(len(vector1[i])):
            aux = aux + (vector1[i][j])**2
    c = aux**0.5
    c = round(c,3)
    
    return c


def prodInternoVector(vector1, vector2):
    if len(vector1) != len(vector2):
        print("no es posible")
    else:
        c = [0,0]
        cvec = conjugadoVector(vector1)
        for i in range(len(vector1)):
            c = suma(c,multiplicar(cvec[i], vector2[i]))
        return c


def conjugadoVector(vector1):
    c = []
    for i in range(len(vector1)):
        c.append(conjugado(vector1[i]))
    return c
        

def tensorVector(vector1, vector2):
    c = []
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            c.append(multiplicar(vector1[i], vector2[j]))
    return c

def transVector(vector1):
    c = []
    for i in range(len(vector1)):
        aux = []
        aux.append(vector1[i])
        c.append(aux)
    return c

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
def fase(tupla1):
    c = math.atan2(tupla1[1], tupla1[0])
    c = round(c,3)
    return c

def convertor(tupla1):
    la = modulo(tupla1)
    phi = math.degrees(math.atan(tupla1[1]/tupla1[0]))
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

    c = suma**0.5
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
    
    res1 = (tupla1[0] * tupla2[0]) - (tupla1[1] * tupla2[1])
    res2 = (tupla1[0] * tupla2[1]) + (tupla2[0] * tupla1[1])
    c = [res1, res2]

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


##def main():
##    print(hermitianMatriz(mat1))
##    
##main()
