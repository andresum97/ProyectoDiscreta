
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
    print numero
        
        
        
