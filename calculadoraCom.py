from sys import stdin
import math
tupla1 = [0.7071067811865475,0]
tupla2 = [0.7071067811865475,0]

vector1 = [[6,3],[0,0],[5,1],[4,0]]
vector2 = [[3,-4.5],[4,6],[0,2]]

c = [ [[1,0],[0,0]], [[0,0],[0,0]]]
mat1 = [ [[1/(2**0.5),0],[1/(2**0.5),0]], [[1/(2**0.5),0],[-1/(2**0.5),0]] ]
mat2 = [ [[0,0],[1,0]], [[1,0],[0,0]] ]

def tensorMatriz(mat1, mat2):
    c = []
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            c.append(tensorVector(mat1[i], mat2[j]))
    print(c)
    return c

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

###### Vectores

def tensorVector(vector1, vector2):
    c = []
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            c.append(multiplicar(vector1[i], vector2[j]))
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

def convertor(tupla1):
    la = modulo(tupla1)
    phi = math.atan2(tupla1[1]/tupla1[0])
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


def main():
    
    m1 = tensorMatriz(mat1, mat1)
    m2 = tensorMatriz(mat1, mat2)

    matm1 = matrizProducto(m2, m1)
    matm2 = matrizProducto(matm1, c)
main()
