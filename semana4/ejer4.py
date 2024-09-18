num = int(input("ingrese un numero entero positivo: "))
if num < 0:
    print("no es un numero entero positivo.")
else:
    for i in range(1, num+1):
        for j in range(i):
            print("*", end="")
        print()    
