cadena = input("ingrese una cadena: ").lower()
prefijo = cadena[0]
sufijo = cadena[-1]
#prefijo especifico = h
#sufijo especifico = s
if prefijo == "h" and sufijo == "s":
    print("la cadena si cumple con el prefijo y sufijo específico!")
else:
    print("la cadena no cumple con el prefijo y sufijo específico!")
