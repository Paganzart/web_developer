print("Hola, como estas?")
print(34%3)
print(type(34))
print(type('34'))
print("Hola\nmundo")


print(len('Hola mi amor'))

cadena = "Hola mundo"
print(cadena[0:10:2])
print(cadena[1:2])

cadena1 = 'ejemplo'
print(cadena1[0:3:2])

cadena2 = 'raro'
print(cadena2[0:4:2])

print(len(cadena2))
print(cadena2[-3])
print(cadena2[0:])

name = "Alex"
print(name + "ander" )    # Concatenación

x = "Alexander"
x = x.upper()
print(x)
x = x.lower()
print(x)

y = "AsTeRisCo"
y = y.upper()
print(y)
y = y.lower()
print(y)
y = y.split()           # Funcion "split()"
print(y)

z = "Este es otro ejemplo"
z = z.split('t')
print(z)


print("Esta es {} {}".format("una","cadena"))                     # format
print("Esta {0} {0} {0}".format("es","una","cadena"))
print("Esta {0} {1} {2}".format("es","una","cadena"))

print("Un ejemplo {0} {1} {2}".format("para","entender","mejor."))


resultado = 100 / 888
print("El resultado es: ", resultado)

print("\n")
mi_lista = [0, 4, -23, "cierto", 45.23]                    # Listas
print(mi_lista)
print(mi_lista[3:])
print(len(mi_lista))
print(mi_lista[0:4:2])

mi_lista2 = ["never", 3, 1000]
mi_lista2[2] = "Alex"                 # Las listas son mutables 

print(mi_lista + mi_lista2)

mi_lista3 = [0, -78, 4, 45.3, 45.301]
mi_lista3.sort()
print(mi_lista3)
mi_lista3.reverse()
print(mi_lista3)




mi_diccionario = {'llave1':'valor1','llave2':'valor2'}           # Diccionarios
print(mi_diccionario)
mi_diccionario2 = {'Agua':'12.00', 'Leche':'19.00', 'Cerveza':'23.00'}
print(mi_diccionario2)
print(mi_diccionario2['Leche'])
print(mi_diccionario2.keys())
print(mi_diccionario2.values())



tuplaa = (1, 5, 7, 4, 8, 3, 9, 2,6 ,3 ,8 ,6 ,89, 12,3,3,3,3)            # Tuplas
print(tuplaa.count(9))
print(tuplaa.index(3))



miset = set()
miset.add(1)
print(miset)