def cont_palabras(cadena):
    palabras = cadena.split()
    num_palabras = len(palabras)
    return num_palabras
oracion = input("ingrese una oracion: ")
print("El número de palabras es:", cont_palabras(oracion))