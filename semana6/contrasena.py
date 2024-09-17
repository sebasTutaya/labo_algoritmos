import random
import string
def generar_contraseña(longitud):
   
    
    while True:
        caracteres= string.ascii_letters + string.digits + string.punctuation
        contraseña= "".join(random.choice(caracteres) for i in range(longitud))
        if (any(c.islower() for c in contraseña) and 
            any(c.isupper() for c in contraseña) and 
            any(c.isdigit() for c in contraseña) and 
            any(c in string.punctuation for c in contraseña)):
            return contraseña
        
           
   
if __name__ == "__main__":
    longitud_deseada = int(input("Ingrese la longitud deseada: "))
    if longitud_deseada < 8:
        print("La contraseña debe tener al menos 8 caráctares")
    else:
        contraseña_generada = generar_contraseña(longitud_deseada)
        print("Contraseña generada:", contraseña_generada)