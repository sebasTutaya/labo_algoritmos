#987 654 3210
numero = input("ingrese un numero de 10 digitos: ")
codigo = numero[:3]
seg = numero[3:6]
ter = numero[6:]
print(f"({codigo}) {seg}-{ter}")
