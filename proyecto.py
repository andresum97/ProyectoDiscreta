import numpy as np
import math as m
from conversion_letras import *

archivo = open("frase.txt","r")
contenido = archivo.read()                  #Lectura del archivo
contenido = contenido.upper()               #Convierte su contenido a mayusculas
print contenido
#mensaje = letra_numero(contenido)           #Funcion para pasar a numeros (arreglar numeros del 00-09)
#print mensaje

largo =len(contenido)
largo= int(m.ceil(largo/3))
print largo
encript = np.zeros((3,largo))              #Creacion matriz de la llave

diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"

total = len(contenido)
i = 0
numero = ""
letra = ""
temp = 0
f=0
g=0
cont = 1 
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

    

print encript
    
respuesta = llave.dot(encript)
print "la respuesta es"
print respuesta



