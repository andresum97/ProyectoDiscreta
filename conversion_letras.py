
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


def modulo_29(matriz,largo):
    numero = 0
    valor29 = 0
    for j in range(0,largo):
        for i in range(0,3):
            numero = matriz[i][j]
            valor29 = numero % 29
            matriz[i][j] = valor29
    return matriz

def numero_letra(matriz,l):
    valor = 0
    palabra = ""
    letra = ""
    largo = int(l)
    for j in range(0,largo):
        for i in range(0,3):
            valor = matriz[i][j]
            letra = diccionario[int(valor)]
            palabra += letra
    return palabra
