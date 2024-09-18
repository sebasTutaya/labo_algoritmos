#multiplicacion utilizando for

numero = int(input("ingrese un numero entero positivo: "))

if numero <= 0:
    print(f"el numero ingresado debe ser entero positivo.")
else:
    print(f"tabla de multiplicar del numero {numero}")
    for x in range(0, 11):
        resultado = numero * x
        print(f"{numero} * {x} = {resultado}")


