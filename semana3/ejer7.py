precio = float(input("ingrese el precio original del producto: "))
categoria = input("ingrese si es 'estudiante', 'jubilado', 'empleado' u 'otro': ")
if categoria == "jubilado":
    descuento = precio - (precio * 0.15)
    print("se le aplicará un descuento del 15%, pague:", descuento, "soles.")
elif categoria == "estudiante":
    descuento = precio - (precio * 0.10)
    print("se le aplicará un descuento del 10%, pague:", descuento, "soles.")
elif categoria == "empleado":
    descuento = precio * (precio * 0.05)
    print("se le aplicará un descuento del 5%, pague:", descuento, "soles.")
else:
    print("usted no recibe ningun descuento, pague: ", precio)
