'''
diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"

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
        
        
'''
diccionario = " ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"

def letra_numero(palabra):
    palabra = palabra.upper()
    total = len(palabra)
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
        numero = numero + numl
    return numero


