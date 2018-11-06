import numpy as np
import math as m
#Constante donde estan los valores del abecedario
diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"

#Transforma la palabra entera en valores de numeros
def letra_numero(palabra):
    palabra = palabra.upper()   #Todo lo pasa a mayuscular
    total = len(palabra)        #Largo de la palabra
    resultado=[ ]               #Lista donde se guardan los numeros
    i = 0
    numero = ""
    letra = ""
    temp = 0
    numl = ""
    for i in range(0,total):
        letra = palabra[i]
        temp = diccionario.find(letra)
        #numl = str(temp)
        if((temp>=0)and(temp<=9)):
            numl = "0"+str(temp)
        else:
            numl = str(temp)
        numero = numl
        resultado.append(numero)
    return resultado


def modulo_29(matriz,largo):
    numero = 0
    valor29 = 0
    for j in range(0,largo):
        for i in range(0,3):
            numero = matriz[i,j]
            valor29 = numero % 29
            matriz[i,j] = valor29
    return matriz

def numero_letra(matriz,l):
    valor = 0
    palabra = ""
    letra = ""
    largo = int(l)
    for j in range(0,largo):
        for i in range(0,3):
            valor = matriz[i,j]
            letra = diccionario[int(valor)]
            palabra += letra
    return palabra

###======================== DESENCRIPCION ===============================
def generalizedEuclidianAlgorithm(a, b):
    if b > a:
        return generalizedEuclidianAlgorithm(b,a);
    elif b == 0:
        return (1, 0);
    else:
        (x, y) = generalizedEuclidianAlgorithm(b, a % b);
        return (y, x - (a / b) * y)

def inversemodp(a, p):
    a = a % p
    if (a == 0):
        print "a is 0 mod p"
        return None
    if a > 1 and p % a == 0:
        return None
    (x,y) = generalizedEuclidianAlgorithm(p, a % p);
    inv = y % p
    assert (inv * a) % p == 1
    return inv

def identitymatrix(n):
    return [[long(x == y) for x in range(0, n)] for y in range(0, n)]

def inversematrix(matrix):
    q = 29
    n = len(matrix)
    A = np.matrix([[ matrix[j, i] for i in range(0,n)] for j in range(0, n)])
    Ainv = np.matrix(identitymatrix(n))
    for i in range(0, n):
        factor = inversemodp(A[i,i], q)
        if factor is None:
             raise ValueError("TODO: deal with this case")
        A[i] = A[i] * factor % q
        Ainv[i] = Ainv[i] * factor % q
        for j in range(0, n):
            if (i != j):
                factor = A[j, i]
                A[j] = (A[j] - factor * A[i]) % q
                Ainv[j] = (Ainv[j] - factor * Ainv[i]) % q
    return Ainv
