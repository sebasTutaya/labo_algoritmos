lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [5,6,7,8,9,10,11,12,13,14,15]
lista3 = [10,11,12,13,14,15,16,17,18,19,20]

#convertir listas a conjuntos

set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)
#B
interseccion = set1.intersection(set2, set3)
print("interseccion:", interseccion)
#C
union = set1.union(set2, set3)
print("union:", union)
#D
diferencia = set1.difference(set3)
print("diferencia:", diferencia)
#Convertir a Tupla
tupla1 = tuple(interseccion)
tupla2 = tuple(union)
tupla3 = tuple(diferencia)
#suma del primer y ultiumo elemento
#primera tupla
elemento1 = tupla1[0]
print("la suma del primer y ultimo elemento de la primera tupla es:", elemento1)
#segunda tupla
prim_elem = tupla2[0]
ult_elem = tupla2[-1]
print("la suma del primer y ultimo elemento de la segunda tupla es:", prim_elem + ult_elem)
#tercera tupla
ele_prim = tupla3[0]
ele_ult = tupla3[-1]
print("la suma del primer y ultimo elemento de la tercera tupla es:", ele_prim + ele_ult)

