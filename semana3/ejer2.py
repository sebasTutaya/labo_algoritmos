def clas_triangulos(longitud1,longitud2,longitud3):
    if longitud1 == longitud2 == longitud3:
        return("equilatero")
    if longitud1 != longitud2 and longitud1 != longitud3 and longitud2 != longitud3:
        return("escaleno")
    else:
        return("isosceles")

longitud_1 = int(input("ingrese la primera longitud: "))
longitud_2 = int(input("ingrese la segunda longitud: "))
longitud_3 = int(input("ingrese la tercera longitud: "))

print(clas_triangulos(longitud_1,longitud_2,longitud_3))