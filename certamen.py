#a)
def ganador(c1,c2,c3,meta):
    if c1==meta:
        return 1
    elif c2==meta:
        return 2
    elif c3==meta:
        return 3
    else:
        return 0
#b)
def contar(palabra):
    contador=0
    cont=0
    while len(palabra)>=contador:
        if palabra[cont]=="a":
            contador+=1
            cont+=1
        elif palabra[cont]=="e":
            contador+=1
            cont+=1
        elif palabra[cont]=="i":
            contador+=1
            cont+=1
        elif palabra[cont]=="o":
            contador+=1
            cont+=1
        elif palabra[cont]=="u":
            contador+=1
            cont+=1
    return contador
print contar ("aeiou")
