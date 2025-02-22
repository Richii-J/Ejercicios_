#Escribe un programa que pida al usuario dos números y determine si el primero es mayor que el segundo.
'''
Num1 = int((input("Escribe el primer numero: ")))
Num2 = int((input("Escribe el segundo numero: ")))

if Num1 > Num2:
    print(f"{Num1} es mayor que {Num2}")
else:
    print("No se cumple la condicion")

'''


#Pide al usuario dos números y muestra en pantalla si el primer número es menor que el segundo.
'''
Num1 = int((input("Escribe el primer numero: ")))
Num2 = int((input("Escribe el segundo numero: ")))

if Num1 < Num2:
    print(f"{Num1} es menor que {Num2}")
else:
    print("No se cumple la condicion")
'''


#Solicita al usuario que ingrese su edad y verifica si tiene exactamente 18 años.
'''
User = int(input("Ingresa tu edad: "))

if User == 18:
    print("Exactamente crack, tienes 18 años")
else:
    print("No cumples con la edad correcta...")
'''


#Pide al usuario un número y verifica si es diferente de 10.
'''
Num1 = int(input("Ingresa un numero: "))
Num2 = 10

if Num1 != Num2:
    print(f"{Num1} es diferente que {Num2}")
else:
    print("XD")
'''


#Pregunta al usuario su calificación en un examen y determina si aprobó (considerando que la nota mínima para aprobar es 70).
'''
Calif = int(input("Ingresa tu calificacion: "))
Calif_Min = 70

if Calif >= Calif_Min:
    print("Has aprobado")
else:
    print("Reprobado...")
'''


#Escribe un programa que pida la edad del usuario y verifique si es menor o igual a 12 años para determinar si puede acceder a una entrada infantil en el cine.
'''
User3 = int((input("Ingrese su edad: ")))
Edad_Lim = (12)

if User3 <= Edad_Lim:
    print("Puedes entrar")
else:
    print("No puedes ingresar")
'''


#Pide al usuario que ingrese dos palabras y verifica si son iguales.
'''
Pal_1 = input("Ingresa una palabra: ")
Pal_2 = input("Ingresa otra palabra: ")

if Pal_1 == Pal_2:
    print("La primera palabra es similar a la segunda palabra")
else:
    print("No son iguales")
'''

#Crea dos listas con elementos predefinidos y compara si tienen la misma cantidad de elementos.
'''
Lista1 = list(range(1, 11))
Lista2 = list(range(1, 11))

if len(Lista1) == len(Lista2):
    print("Tienen la misma cantidad de elementos")
else:
    print("Son distintos")
'''


#Pide al usuario un número y verifica si está entre 1 y 100 (incluyendo los extremos).
'''
User4 = int(input("Ingresa un numero: "))

for i in range(1, 101):
    if User4 == i:
        print(f"El {User4} esta en el rango")
        break
else:
    print(f"El {User4} no esta en el rango")
'''


#Pregunta la edad del usuario y muestra un mensaje indicando si tiene la edad suficiente para votar (18 años o más).
'''
User5 = int(input("Ingresa tu edad: "))
Edad  = (18)

if User5 >= Edad:
    print("Puedes votar")
else:
    print("No puedes votar")
'''