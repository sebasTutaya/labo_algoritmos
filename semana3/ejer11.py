alt = float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kilogramos: "))
IMC = int(peso / (alt*alt))
if IMC < 18.5:
    print("IMC =", IMC, "usted tiene bajo peso")
elif 18.5 < IMC < 24.9:
    print("IMC =", IMC, "usted tiene un peso normal.")
elif 25.0 < IMC < 29.9:
    print("IMC =", IMC, "usted tiene sobrepeso.")
elif IMC > 30:
    print("IMC =", IMC, "usted tiene obesidad.")