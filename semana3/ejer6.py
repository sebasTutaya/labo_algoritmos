numeros = input("ingrese 3 numeros separados por comas: ")
listnum = [int(num) for num in numeros.split(",")]
num1 = listnum[0]
num2 = listnum[1]
num3 = listnum[2]
if num1 > num2 and num1 > num3:
    print(num1, "es el número mayor.")
elif num2 > num3:
    print(num2, "es el número mayor.")
else:
    print(num3, "es el número mayor.")

