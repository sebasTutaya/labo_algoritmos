def orden_alfabetico(palabra1, palabra2):
    if palabra1 < palabra2:
        return f'"{palabra1}" va primero en orden alfabético que "{palabra2}".'
    elif palabra1 > palabra2:
        return f'"{palabra2}" va primero en orden alfabético que "{palabra1}".'
    else:
        return f'Las palabras "{palabra1}" y "{palabra2}" son iguales.'

palabra1 = input("ingrese la primera palabra: ")
palabra2 = input("ingrese la segunda palabra: ")
print(orden_alfabetico(palabra1, palabra2))