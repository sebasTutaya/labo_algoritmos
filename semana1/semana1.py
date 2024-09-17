#longitud de un nombre

print(len("sebastian"))

#comparar logitud entre nombre y apellido

nombre = len("sebas")
apellido = len("Tutaya")

if nombre > apellido:
    print("tu nombre tiene mas letras que tu apellido")
elif nombre < apellido:
    print("tu apellido tiene mas letras que tu nombre")

#declarar valores a variables
    
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
producto = num_one * num_two
division = num_one / num_two
resto = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("la suma es:", total)
print("la diferencia es:", diff)
print("la multiplicacion es:", producto)
print("la division es:", division)
print("la division de modulo es:", resto)
print("la potencia es:", exp)
print("la division de piso es:", floor_division)

#radio de un círculo de 30 metros
pi = 3.14
radio = 30
area_of_circle = pi*radio**2
print("el area del circulo es:", area_of_circle)

#funcion integrada para obtener el nombre 

name = input("por favor ingrese su nombre:")
last_name = input("ingrese su apellido:")
country = input("ingrese su país:")
age = input("ingrese su edad:")

print(name,last_name, country, age)




