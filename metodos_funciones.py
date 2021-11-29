# Funciones

def decir_hola():
    print("Hola, como estas?")

decir_hola()    # Asi llamamos a la funcion



def suma(num1, num2):
    total = num1 + num2
    print(total)

suma(-13, 45)




## Logica de funciones

def chequear_numero_par_en_lista(num_list):

    for number in num_list:
        if number % 2 == 0:
            print("Verdadero")
            return True
        else:
            pass
    print("Falso")
    return False

chequear_numero_par_en_lista([1, 3, 5])
chequear_numero_par_en_lista([1, 3, 8])




# *args y **kwargs

def sumas(*args):
    print(args)

sumas(23, 4, 56)



# Lambda

square = lambda num: num**8

print(square(2))