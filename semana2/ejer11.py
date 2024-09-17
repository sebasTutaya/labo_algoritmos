cadena = (input("ingrese el palindromo: ")).lower().replace(" ","")
cad_inv = cadena[::-1]
for x in cadena:
    if cadena != cad_inv:
        print("no es un palindromo")
else:
    print("si es un palindromo")

