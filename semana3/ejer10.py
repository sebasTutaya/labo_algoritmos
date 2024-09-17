lon_metros = float(input("ingrese la longitud en metros: "))
conv = input("ingrese la unidad a la que desea convertir: 'pies', 'pulgadas' o 'yardas'")
if conv == "pies":
 conversion = lon_metros * 3.28
 print(conversion)
elif conv == "pulgadas":
 conversion = lon_metros * 39.3701
 print(conversion)
elif conv == "yardas":
 conversion = lon_metros * 1.09361
 print(conversion)