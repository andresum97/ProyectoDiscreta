import numpy as np
from conversion_letras import *


archivo = open("frase.txt","r")
contenido = archivo.read()                  #Lectura del archivo
contenido = contenido.upper()               #Convierte su contenido a mayusculas
print contenido                     
letra_numero(contenido)                     #Funcion para pasar a numeros (arreglar numeros del 00-09)

llave = np.array([[1, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])               #Creacion matriz de la llave


i=0
j=0
contador = 0
                                            #Ciclo para rellenar matriz
while contador < 9:
    if(contador<3):
        a = int(raw_input("Ingrese numero de la columna "+str(i+1)+" fila " + str(j+1) + " ")) 
        llave[j,i] = a
        i +=1
        if(contador==2):
            j=1
            i=0
            print ' '
        
    if(contador>=3 and contador<6):
        b = int(raw_input("Ingrese numero de la columna "+str(i+1)+" fila " + str(j+1) + " ")) 
        llave[j,i] = b
        i +=1
        if(contador==5):
            j=2
            i=-1
            print ' '
        
    if(contador>=6 and contador<9):        
        c = int(raw_input("Ingrese numero de la columna "+str(i+2)+" fila " + str(j+1) + " ")) 
        i +=1
        llave[j,i] = c

    contador += 1
print ' '
print "Su llave queda asi "
print llave

det = round(np.linalg.det(llave))
print "El determinante es "+ str(det)

