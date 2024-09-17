l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)] 
l2 = [("one", 1), ("two", 2), ("six", 6)]
#crear conjuntos
s1 = set(l1)
print("primer conjunto:",s1)
s2 = set(l2)
print("segundo conjunto:", s2)

interseccion = s1.intersection(s2)
union = s1.union(s2)

#elementos comunes a s1 y s2
s3 = union - interseccion
print("los elementos comunes entre s1 y s2 son:", s3)
#elementos unicos entre s1 y s2
s4 = interseccion
print("los elementos unicos entre s1 y s2 son:", s4)
#nueva lista
l3 = list(s3.union(s4))
l3.sort(key=lambda x: x[1])
print("lista", l3)

