# Diferentes operaciones aritmeticas

a = 4 + 4
print(a)
b = 4.6 + 3.5
print(b)
print(a + b)
print(a - b)
print(a/b)
print(a * b)
print(7 % 4)
print(4*6 +2*1+8/2)
type("hola")

print("hola\nmundo")

# Para ver la longitud de una cadena

print(len("hijo de tu puta madre"))


# Para el indexado

miCadena = "Hola Mundo"

print(miCadena[0:6:2])
print(miCadena[-4])
print(miCadena[0:6])
print(len(miCadena))

# Mas indexado

name = "Pam"
ultimas_letras = name[1:]
print("P" + ultimas_letras)


# Concatenacion

a = "Alexander "
b = "Martínez "
c = "Álvarez. "
d = "Edad: "
e = "30 "    # Aqui el numero se pone como string
f = "años"

print(a + b + c + d + e + f)

# Convertir cadena a mayusculas

x = "HolA mUndO"
x = x.upper()
print(x)

#Convertir cadena a minusculas

x = "HolA mUndO"
x = x.lower()
print(x)

y = "mi edad es: 30 anios"
y = y.upper()
print(y)

# Para separar palabras

z = "hola mundo la verdad es un ejemplo clasico"
z = z.split()
print(z)

# Para quitar alguna letra especifica de la cadena por ejemplo la 'o' es asi:

x = "hola mundo"
x = x.split('o') 
print(x)


# Se toma como un espacio si se usa --> '|'

x = "hola mundo"
x = x.split('|') 
print(x)


# Forma de usar el "format()" en cadenas

print("Esta es {} {}".format("una","cadena"))
print("Esta {0} {0} {0}".format("es","una","cadena"))
print("Esta {0} {1} {2}".format("es","una","cadena"))

resultado = 100 / 888
print("El resultado es: {}".format(resultado))
print("Otra forma de resultado es:", resultado)
print("El resultado es: {r:5.5f}".format(r = resultado))


# LISTAS

mi_lista = [1, 2, 3]
print(mi_lista)
mi_lista2 = [1, 2, 3, "cadena", 3.1426]
print(mi_lista2)
print(len(mi_lista2))
print(mi_lista2[0])
print(mi_lista2[-1])
print(mi_lista2[0:3])

otra_lista = [4, 5, 6]     
print(mi_lista + otra_lista)      # Para sumar listas

otra_lista[0] = "Alex"    # Se observa que las lista si son mutables
print(mi_lista + otra_lista)
otra_lista.append("seis")
print(mi_lista + otra_lista)



# Ordenamiento de listas (ascendente y reversa)



lista2 = ['a', 'z', 'x', 'b', 'd']
lista3 = [4, 1, 5, 7, 3]

lista2.sort()        #ascendente
print(lista2)

lista3.sort()
print(lista3)

lista4 = ['alexander', 'alexis', 'alexandro']  # las cadenas de caracteres se ordenan tambien alfabeticamente
lista4.sort()
print(lista4)

lista2.reverse()      # reversa
print(lista2)

lista3.reverse()
print(lista3)



#   DICCIONARIOS


mi_diccionario = {'llave1':'valor1','llave2':'valor2'}
print(mi_diccionario)
print(mi_diccionario['llave1'])  #para imprimir un valor en especifico

mi_diccionario2 = {'agua':'10.0','leche':'17.0','cerveza':'25.0'}
print(mi_diccionario2['leche'])

mi_diccionario3 = {'manzanas':'2.9','panques':['vainilla', 'chocolate'], 'agua': '3.5'}
print(mi_diccionario3['panques'][1])     # para definir listas dentro de diccionarios
print(mi_diccionario3['panques'][1].upper())


mi_diccionario3['gaseosa'] = 5.90    # para agregar mas al diccionario
print(mi_diccionario3)

print(mi_diccionario3.keys())   #para ver las llaves que hay
print(mi_diccionario3.values())  #paraver lo opuesto, ver los valores que hay



#   TUPLAS 


tupla = (1,2,3)
print(type(tupla))

lista5 = [1,2,3]
print(type(lista5))

t = ('c', 'a', 'a')
print(t.count('a'))   # para contar el numero de veces que se repite un elemento de la tupla
print(t.index('a'))  # para ver en que indice se encuentra la "a"

#t = ('a', 'a', 'b') Esto no lo soporta la "tupla"
#t[0] = 'nuevo'



#  SETS



miset = set()
miset.add(1)      #agrega "1 entre" {} al set
miset.add(2)    #se agrega el "2" al set --->{1, 2}
print(miset)

milista = [1,1,1,2,2,2,3,3,3]
print(set(milista))




#  BOOLEANOS


print(type(False))
print(3 < 2)
print(2 == 2)


# Comparadores de operacion y oper. logicos


print("hola" == "bye")
print('2' == '2')
print('2' == 2)


print(1 and 0)
print(1 or 0)
print(not 0 and 1)





