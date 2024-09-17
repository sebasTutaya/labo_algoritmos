#promedio de notas
notas = input("ingrese las notas separadas por comas: ")
lista_notas = [float(nota) for nota in notas.split(",")]

promedio = sum(lista_notas)/len(lista_notas)
print("el promedio de las notas es:",promedio)