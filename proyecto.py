#Universidad del Valle de Guatemala
#Matematica Discreta I Seccion 10
#Proyecto de encriptacion/desencriptacion con cifrado Hill
#===============================================================================================================================
#Este programa por medio de calculos matriciales, uso de modulos y un diccionario utilizado para transformar de letras a numero
#permite encriptar o desencriptar, depende que necesite el usuario, por medio de cifrado Hill una oracion en un archivo de texto
#===============================================================================================================================
#Gustavo de Leon |Carnet: 17085
#Andres Urizar   |Carnet: 17632
#===============================================================================================================================


import numpy as np                          #Librerias utilizadas, numpy para calculo de matrices
import math                                 #math para utilizacion de operaciones matematicas
from conversion_letras import *             #Modulo con metodos para encripcion y desencripcion

archivo = open("frase.txt","r")             #Para poder leer la frase u oracion en el archivo de texto
contenido = archivo.read()                  
contenido = contenido.upper()               #Convierte su contenido a mayusculas
print contenido                             #Muestra la oracion
largo =len(contenido)                       #Largo de oracion a encriptar/desencriptar
largo1= int(math.ceil(largo/3.0))           #Variable en la que se guarda el largo de la matriz

opcion = 0
while(opcion != 3):                         #Menu de opciones, para encriptar, desencriptar o salir del programa
    print ("1. Encriptar")
    print ("2. Desencriptar")
    print ("3. Salir")
    opcion = int(input("Introduce un numero : "))

    if(opcion == 1):                        #Opcion 1: Encriptacion
        
        encript = np.zeros((3,largo1))              #Creacion matriz de la llave
        diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?" #Metodo para convertir a numeros la oracion (Documentacion en modulo 
        total = len(contenido)                        #conversion_letras, en el metodo letras_numero())
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
        print "-------------------------------------------------------------------------------"
        print "El mensaje encriptado en Matriz es: "
        print encript
        print "-------------------------------------------------------------------------------"
        llave = np.array([[0, 0, 0],                
                          [0, 0, 0],
                          [0, 0, 0]])               #Creacion matriz de la llave
        i=0
        j=0
        contador = 1
        for m in range(1, 10):     #Ciclo para ingresar los datos de la llave matriz, y guardarlos en la matriz llava
            a = int(raw_input("Ingrese numero de la columna "+str(i+1)+" fila " + str(j+1) + " ")) 
            llave[j,i] = a
            i +=1
            if (contador % 3 == 0):
                i=0
                j+=1
                print " "
            contador +=1
        print "-------------------------------------------------------------------------------" #Impresion de llave
        print "Su llave queda asi: "
        print llave
        print "-------------------------------------------------------------------------------"
        det = round(np.linalg.det(llave))                                                       #Aproximacion de determinante a entero
        print "El determinante es "+ str(det)
        if(det ==0):                                                                            #Verificicion del determinante, para saber
            print "La matriz que ingreso no es invertible por lo que no se puede encriptar"     #si la matriz llave posee inverso
            print "-------------------------------------------------------------------------------"
            
        else:
            print "Se puede invertir"
            print "-------------------------------------------------------------------------------"
            respuesta = llave.dot(encript)                   #Multplicacion de matriz llave con la matriz de encript
            respuesta = modulo_29(respuesta, largo1)         #Conversion de matriz respuesta a matriz con modulo 29
            respuesta = numero_letra(respuesta,largo1)       #Convierte los valores de la matriz en letras
            print "La respuesta es"
            print respuesta
            print "-------------------------------------------------------------------------------"

        
    if (opcion == 2):                                  #Opcion 2: Desencripcion
        print "Desencriptar"
        llaveD = np.array([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]])               #Creacion matriz de la llave
        i=0
        j=0
        contador = 1
        for m in range(1, 10):                     #Ciclo para ingreso de la matriz llave
            a = int(raw_input("Ingrese numero de la columna "+str(i+1)+" fila " + str(j+1) + " ")) 
            llaveD[j,i] = a
            i +=1
            if (contador % 3 == 0):
                i=0
                j+=1
                print " "
            contador +=1
        print "-------------------------------------------------------------------------------"
        print "Su llave queda asi: "
        print llaveD
        print "-------------------------------------------------------------------------------"
        llaveD = inversematrix(llaveD)   #Se le saca la matriz inversa con modulo 29 a la matriz llave
        print "Su llave invertida mod 29 queda asi: "
        print llaveD
        print "-------------------------------------------------------------------------------"

        desencript = np.zeros((3,largo1))              #Creacion matriz de la llave
        diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"  #Constante de diccionario
        total = len(contenido)                         #Mismo procedimiento de convertir a numeros la oracion
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
            desencript[f,g] = temp
            f +=1
            if (cont % 3==0):
                f = 0
                g +=1
            cont +=1
        print "-------------------------------------------------------------------------------"
        print "El mensaje encriptado en Matriz es: "
        print desencript                         #Muestra matriz de desencripcion
        print "-------------------------------------------------------------------------------"
        mensaje = llaveD.dot(desencript)         #Realiza la multiplicacion producto cruz entre la llave inversa y matriz de desencriptado
        print "La multiplicacion de las matrices es: "
        print mensaje
        print "-------------------------------------------------------------------------------"
        mensaje = modulo_29(mensaje,largo1)     #Saca modulo 29 a matriz resultante
        mensaje = numero_letra(mensaje,largo1)  #Conversion de los valores de la matriz a letras
        print "Final essss: "
        print mensaje                           #Impresion de mensaje final
        print "-------------------------------------------------------------------------------"

        
        
        
    if (opcion == 3):                        #Opcion 3: Finalizacion de programa
        print "!CLXEE (Adios Encriptado :v)"



