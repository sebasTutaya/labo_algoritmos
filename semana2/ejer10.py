def cont_vocal(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for x in cadena:
        if x in vocales:
            contador += 1
    return contador

cad_ingresada = input("ingrese una oración o palabra: ")
num_vocal = cont_vocal(cad_ingresada)
print(f"El número de vocales en la cadena es: {num_vocal}")