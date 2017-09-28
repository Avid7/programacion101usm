#Lo que calcula el programa es el mayor alza de precios que hubo en
#algun periodo


ing=float(raw_input("Ingrese el número de días:"))
contador=1
contador2=1
maxima_alza=0
pain=0
pain2=0
while contador<ing+float(1):
    Day=float(raw_input("Dia"+" "+str(contador)+":"))
    if contador==contador2:
        pain=Day
    elif contador!=contador2:
        pain2=Day
        contador2+=1
        if (pain2-pain)>maxima_alza:
            maxima_alza=(pain2-pain)
    contador+=1
if maxima_alza==0:
    print "No hubo alzas"
elif maxima_alza!=0:
    print "La mayor alza fue de $",maxima_alza
    
        
        
    
        
        
    




