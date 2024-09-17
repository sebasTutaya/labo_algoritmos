oper = input("que operación desea realizar: ").lower()
num1 = int(input("ingrese el primer número: "))
num2 = int(input("ingrese el segundo número: "))
if oper == "suma":
    print("el resultado es:", num1 + num2)
elif oper == "resta":
    print("el resultado es:", num1 - num2)
elif oper == "multiplicacion" or "multiplicación":
    print("el resultado es:", num1 * num2)
elif oper == "division":
    print("el resultado es:", num1 / num2)

