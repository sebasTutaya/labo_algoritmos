#contar vocales
frase = input("ingrese la frase: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in frase:
    if letra in vocales:
        contador = contador + 1

print(f"hay {contador} vocales en la frase '{frase}':")

