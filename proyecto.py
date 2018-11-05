import numpy as np
import math 
from conversion_letras import *

archivo = open("frase.txt","r")
contenido = archivo.read()                  #Lectura del archivo
contenido = contenido.upper()               #Convierte su contenido a mayusculas
print contenido
largo =len(contenido)
largo1= int(math.ceil(largo/3.0))
encript = np.zeros((3,largo1))              #Creacion matriz de la llave

diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"

total = len(contenido)
i = 0
numero = ""
letra = ""
temp = 0
f=0
g=0
cont =  1
for i in range(0,total):
    letra = contenido[i]
    temp = diccionario.find(letra)
    numero = numero + str(temp)
    encript[f,g] = temp
    f +=1
    if (cont % 3==0):
        f = 0
        g +=1
    cont +=1

print encript

llave = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])               #Creacion matriz de la llave
i=0
j=0
contador = 1
for m in range(1, 10):
    a = int(raw_input("Ingrese numero de la columna "+str(i+1)+" fila " + str(j+1) + " ")) 
    llave[j,i] = a
    i +=1
    if (contador % 3 == 0):
        i=0
        j+=1
        print " "
    contador +=1

print ' '
print "Su llave queda asi "
print llave
det = round(np.linalg.det(llave))
print "El determinante es "+ str(det)
if(det ==0):
    print "La matriz que ingreso no es invertible por lo que no se puede encriptar"


respuesta = llave.dot(encript)



respuesta = modulo_29(respuesta, largo1)
respuesta = numero_letra(respuesta,largo1)
print "la respuesta es"
print respuesta



