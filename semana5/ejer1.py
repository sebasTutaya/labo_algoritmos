#La siguiente es una lista de las edades de 10 estudiantes: 
#edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] (4ptos)
#a. Ordena la lista y encuentra la edad mínima y máxima
#b. Añade de nuevo la edad mínima y máxima a la lista
#c. Encuentra la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
#d. Encuentra la edad promedio (suma de todos los elementos divididos por su número)
#e. Encuentra el rango de las edades (máximo menos mínimo)
#f. Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs() 

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades1 = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
edad_min = min(edades)
edad_max = max(edades)
print(f"la edad minima es: {edad_min} y la edad maxima es: {edad_max}")
edades.append(edad_min)
edades.append(edad_max)
print("agregadas", edades)
#edad mediana
elem = int(len(edades1)/2)
edad_mediana = edades1[elem]/2
print(f"la edad mediana es {edad_mediana}")
#promedio
promedio = sum(edades1)/len(edades1)
print(f"el promedio de edades es {promedio}")
#rango de edades
rango = edad_max - edad_min
print(f"el rango de edades es de {rango}")
#comparar valores
min_dif = abs(edad_min - promedio)
max_dif = abs(edad_max - promedio)

print(f"Mínimo: {edad_min}, Promedio: {promedio}, Máximo: {edad_max}")
print(f"|Mínimo - Promedio|: {min_dif}")
print(f"|Máximo - Promedio|: {max_dif}")

if min_dif < max_dif:
    print("la diferencia maxima es mayor")
elif min_dif > max_dif:
    print("la diferencia minima es mayor")
else:
    print("ambas diferencias son iguales")