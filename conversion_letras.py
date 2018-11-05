import numpy as np
import math as m
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
        
#diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"

def letra_numero(palabra):
    palabra = palabra.upper()
    total = len(palabra)
    resultado=[ ]
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
    #largo = len(palabra)
    #largo = int(m.ceil(largo/3))
    #np.zeros((3,largo))
    #c = np.asarray(resultado)
    #print c
    #for i in range(0,len(resultado)):
     #   print resultado[i]
        #numero = numero + numl
    #print numero
        

