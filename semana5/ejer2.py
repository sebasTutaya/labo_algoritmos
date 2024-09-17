# “Soy profesor y me encanta inspirar y enseñar a la gente”. ¿Cuántas palabras únicas se han
# utilizado en la frase? Usa los métodos de split y sets para obtener las palabras únicas.

frase = "Soy profesor y me encanta inspirar y enseñar a la gente"
palabras = frase.split()
palabras1 = frase.split()

#palabras unicas
set1 = set(palabras)
pal_uni = len(set1)
print(f"hay {pal_uni} palabras unicas y son: {set1} ")

