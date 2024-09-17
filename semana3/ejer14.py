import random
juego = ["piedra", "papel", "tijera"]
comp = random.choice(juego)
usuario = input("eliga piedra, papel o tijera: ").lower()
print("la computadora eligió", comp)
if usuario == comp:
    print("empate")
elif (comp == "piedra" and usuario == "tijera") or \
    (comp == "papel" and usuario == "piedra") or \
    (comp == "tijera" and usuario == "papel"):
    print("gano la computadora")
else:
    print("ganaste")