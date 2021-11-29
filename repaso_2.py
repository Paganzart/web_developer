a = 1234
print(type(a))
b = "123"
print(type(b))
c = 'elemento'
print(type(c))

d = 45.34 / 45.1
print(d)

e = 'Hola como has estado, '
print(len(e))             # Cuenta el numero de letras en una cadena, incluyendo los espacios

f = 'hoy hasta ahora he estudiado de HTML. '
print(len(f))

g = 'Ahora me encuentro estudiando de Python!'
print(len(g))
print(g[0:45:3])
print(g[18:])
print(e + f + g)

print("\n")

e = e.upper()
print(e)
f = f.upper()
print(f)
g = g.upper()
print(g)

print(e + f + g)

g = g.split('S')
print(g)


lista = [1, 23, -34, 567.95, "eres", "azucar amargo"]
print(lista)
print(len(lista))
print(lista[3:])

lista2 = [0, 21, "malo"]
print(lista + lista2)
print(len(lista + lista2))

lista[3] = "tu"
print(lista + lista2)
lista2.append("ejemplo")
print(lista2)

lista3 = [23, 45, -12, 67.56, 100000, 45000, 4/3]
lista3.sort()
print(lista3)

lista4 = ["123", "u", "t", "b", "a", "1", "-2"]
lista4.sort()
print(lista4)

lista5 = ['eres', 'magia', 'a','mi','corazon']
lista5.sort()
print(lista5)

lista6 = [1, 3, 4.6, 5, 8.1]
lista6.reverse()
print(lista6)


diccionario = {'agua':12.5, 'refresco':15.0, 'pay':17.5}
print(diccionario)
print(len(diccionario))
print(diccionario.keys())
print(diccionario.values())

tupla = 'e', 'r', 'e', 'e', 'e', 't'
print(tupla.count('e'))
print(type(tupla))


hambre = True
sed = False

if (hambre):
    print("Tenemos hambre!")

if(hambre and sed):
    print("Tenemos hambre y sed")
else:
    print("Solo tenemos hambre")

x = 5
y = 0
if(y > x):
    print(y,"es mayor que", x)
else:
    print(x, "es mayor que", y)


lista10 = [1,3,4,'eje',9.23,10]
for num in lista10:
    print(num)

lista11 = [1,2,3,4,5,6,7,8,9]
for num in lista11:
    print(num)

for num in lista11:
    print('hola')

for letter in "Hola este es un ejemplo":
    print(letter)

print("\n")

x = 0
while x <= 10:
    print(x)
    x += 1
    if(x == 6):
        pass
print("Conteo  incremental exitoso!")

print("\n")
y = 10
while y > 0:
    print(y)
    y -= 1
print("Cuenta regresiva exitosa!")


for num in range(10):
    print(num)

print("\n")
for num in range(21):
    print(num)

print("\n")
for num in range(0,21,2):
    print(num)