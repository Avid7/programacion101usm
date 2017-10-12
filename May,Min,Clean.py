#Mayusculizador
variable=raw_input("Ingrese una frase de cualquier indole:")
var=int(raw_input("Para Mayusculizar, presione 1.Para Minusculizar,presione 2.Para limpiar el contenido,presione 3"))
if var==1:
    print variable.upper()
elif var==2:
    print variable.lower()
else:
    variable=" "
    print variable

    

