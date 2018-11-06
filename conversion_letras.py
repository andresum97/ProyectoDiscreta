import numpy as np
import math as m
#Constante donde estan los valores del abecedario
diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"
"""
def letra_numero(palabra):
    palabra = palabra.upper()
    total = len(palabra)
    i = 0
    numero = ""
    letra = ""
    temp = 0
    for i in range(0,total):
        letra = palabra[i]
        temp = diccionario.find(letra)
        numero = numero + str(temp)
    return numero
        """
        
#Transforma la palabra entera en valores de numeros
def letra_numero(palabra):
    palabra = palabra.upper()   #Todo lo pasa a mayuscular
    total = len(palabra)        #Largo de la palabra
    resultado=[ ]               #Lista donde se guardan los numeros
    i = 0
    numero = ""                 #Variables donde se va a guardar todas las palabras
    letra = ""
    temp = 0
    numl = ""
    for i in range(0,total):    #Ciclo para recorrer la palabra y cambiar
        letra = palabra[i]      #de una a numeros
        temp = diccionario.find(letra)
        #numl = str(temp)
        if((temp>=0)and(temp<=9)):  #En caso que el numero es de 1 digito, lo vuelve
            numl = "0"+str(temp)    #de 2
        else:
            numl = str(temp)
        numero = numl
        resultado.append(numero)
    return resultado                #Devuelve el valor en numeros, por medio de una lista

#Convierte una matriz normal, en un matriz con valores de mod 29
def modulo_29(matriz,largo):    
    numero = 0
    valor29 = 0
    for j in range(0,largo):    #Ciclos para recorrer la matriz para obtener valores por columna
        for i in range(0,3):
            numero = matriz[i,j]    #Guarda valor original en variable
            valor29 = numero % 29   #Calcula el mod 29 del valor de la matriz y guarda en variable
            matriz[i,j] = valor29   #Vuelve a guardar en la matriz el valor con mod 29
    return matriz                   #devuelve la matriz con mod 29

#Convierte el valor de numero a letras para mostrar la encripcion
def numero_letra(matriz,l):
    valor = 0                #Variables para utilizar y guardar datos temporales
    palabra = ""
    letra = ""
    largo = int(l)          #Cantidad de columnas de la matriz
    for j in range(0,largo):    #Ciclos para recorrer la matriz
        for i in range(0,3):
            valor = matriz[i,j]     #Obtiene el valor de la matriz ya calculada
            letra = diccionario[int(valor)]   #Convierte el numero en letra ya encriptada
            palabra += letra                  #Concatena las letras resultantes
    return palabra                  #Devuelve la palabra ya encriptada

###======================== DESENCRIPCION ===============================
##Codigo obtenido de: https://stackoverflow.com/questions/4287721/easiest-way-to-perform-modular-matrix-inversion-with-python
##Todo este codigo es para poder utilizar la variable de desencripcion en modulo 29, para calcular con la matriz de datos
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
