#1. Escribe un programa que pida al usuario que ingrese un número entero positivo. El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno, utilizando un bucle while.
'''
#Solicitar al usuario un número entero positivo
num = int(input("Ingrese un numero entero positivo: "))

#Verificar que el número sea postivo
if num > 0:
    contador = 1 #Iniciamos el contador en 1
    while contador <= num:
        print(contador) #Imprimimos el numero actual
        contador +=1 #Aumentamos el contador en 1
else:
    print("El numero debe ser un entero positivo. ")
'''



#2. Escribe un programa que imprima los números pares entre 1 y 20 (inclusive) utilizando un bucle for.
'''
#Usamos un bucle for para recorrer los numeros del 1 al 20
for num in range(2, 21 ,2): #Inicia en 2, termina en 20, con paso de 2
    print(num)
'''



#3. Solicitar al usuario un numero entero positivo
'''
num = int(input("Ingresa el numero: "))

# Verificar que el nmero sea positivo
if num > 0:
    contador = 0 # Iniciador contador de digitos
    temp = num # Variable temporal para no modificar el numero original

    while temp > 0:
        temp //= 10 # Eliminamos el ultimo digito dividiendo por 10
        contador += 1 # Incrementamos el contador

    print(f"El numero {num} tiene {contador} digitos. ")
else:
    print("Debe ingresar un numero entero positivo")
'''



#4. Escribe un programa que calcule la suma de todos los números enteros del 1 al 100 utilizando un bucle for.
'''
# Iniciamos la variable Suma
Suma = 0

# Recorrer los numeros del 1 al 100
for num in range(1, 101):
    Suma += num # Acomular la suma

# Mostrar el resultado
print(f"La suma de los numeros del 1 al 100 es: {Suma}")
'''



#5. Escribe un programa que pida al usuario un número entero y luego imprima todos los números desde ese número hasta el
#0 en orden descendente utilizando un bucle while.
'''
# Pedir al usuario un numero entero
num = int(input("Ingrese un numero entero: "))

# Bucle while para contar hacia atras hasta 0
while num >= 0:
    print(num)
    num -= 1 # Resta 1 en cada iteracion
'''



#6. Escribe un programa que imprima la tabla de multiplicar de un número dado por el usuario, 
# desde el 1 hasta el 10, utilizando un bucle for.
'''
# Pedir al usuario que ingrese el numero
Num = int(input("Ingresa un numero para su respectiva tabla: "))

#Bucle for para recorrer del 1 al 10 y calcular la multiplicacion
for i in range(1, 11):
    resultado = Num * i
    print(f"{Num} x {i} = {resultado}")
'''



#7. Escribe un programa que pida al usuario un número entero positivo y luego imprima 
# todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.
'''
#Pedir al usuario que ingrese un numero entero positivo
Num = int(input("Ingrese un numero entero: "))

#Inicializar contador en 1 (Primer numero impar)
i = 1

#Buble while para imprimir los numeros impares hasta num
while i <= Num:
    print(i)
    i += 2 #Incrementamos de 2 en 2 para obtener solo impares
'''



#8. Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, 
# donde el valor de n lo ingresa el usuario, utilizando un bucle for.
'''
#Se pide un numero entero positivo al usuario
N = int(input("Ingrese un numero entero positivo: "))

#Se verifica que N sea positivo
if N < 0:
    print("Error")
else:
    #Inicializar los dos primeros terminos de Fiboncci
    a, b = 0, 1

    print("Serie de Fibonancci:")

    #Imprimir la serie hasta N terminos
    for _ in range(N):
        print(a, end=" ") #Imprimir el numero en la misma linea
        a, b = b, a + b #Actualizar los valores del siguiente termino
'''



#9. Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while. 
# El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
'''
#Pedir al usuario un numero entero positivo
N = int(input("Ingrese un numero entero positivo: "))

#Verificar que el numero sea positivo
if N < 0:
    print("El factorial no esta definido para numeros negativos.")
elif N == 0:
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    contador = N #Inicializar el contador en el numero ingresado

    #Calcular el factorial usando un bucle while
    while contador > 1:
        factorial *= contador #Multiplicar el valor actual de factorial por el contador
        contador -=1 #Disminuir el contador en 1

        #Mostrar el resultado
        print(f"El factorial de {N} es: {factorial}")
'''



#10. Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud mientras la contraseña 
# ingresada sea incorrecta. El programa debe continuar hasta que el usuario ingrese la contraseña correcta.

#Definir la contraseña
ContraseñaCorect = "N33ger"


while True: #Bucle infinito para simular un do-While
    #Pedir la contraseña al usuario
    contraseña = input("Ingrese la contraseña: ")

    #Verificar si es correcta
    if contraseña == ContraseñaCorect:
        print("Acceso permitido")
        break
    else:
        print("Contraseña incorrecta. Intente de nuevo")