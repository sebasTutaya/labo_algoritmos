n = int(input("ingrese un número: "))
if n < 2:
    print("ingrese un numero mayor o igual a 2")
else:
    suma = 0
    num = 2

    while num <= n:
        suma = suma + num
        num = num + 2

    print(f"la suma de los numeros pares desde el 2 hasta {n} es {suma}")