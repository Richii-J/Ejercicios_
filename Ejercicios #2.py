#Número positivo, negativo o cero

'''
num = float(input("Ingrese un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
'''


#Número par o impar

'''
num = int(input("Ingrese un número entero: "))

if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
'''


#Mayor de edad

'''
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
'''


#Múltiplo de 5

'''
num = int(input("Ingrese un número: "))

if num % 5 == 0:
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo de 5")
'''


#Calificación aprobatoria

'''
calificacion = int(input("Ingrese la calificación: "))

if calificacion >= 60:
    print("Aprobaste. ¡Felicidades!")
else:
    print("Reprobaste. Sigue esforzándote.")
'''


#Día de la semana

'''
num = int(input("Ingrese un número del 1 al 7: "))

if num == 1:
    print("Lunes")
elif num == 2:
    print("Martes")
elif num == 3:
    print("Miércoles")
elif num == 4:
    print("Jueves")
elif num == 5:
    print("Viernes")
elif num == 6:
    print("Sábado")
elif num == 7:
    print("Domingo")
else:
    print("Número inválido. Debe estar entre 1 y 7.")
'''


#Número mayor entre dos

'''
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
elif num1 < num2:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
'''


#Mayor entre tres números

'''
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")
'''


#Clasificación de ángulos

'''
angulo = float(input("Ingrese el valor del ángulo en grados: "))

if angulo < 90:
    print("El ángulo es agudo.")
elif angulo == 90:
    print("El ángulo es recto.")
elif angulo > 90 and angulo < 180:
    print("El ángulo es obtuso.")
elif angulo == 180:
    print("El ángulo es llano.")
else:
    print("El valor ingresado no es válido para esta clasificación.")
'''


#Cálculo de impuestos

'''
salario = float(input("Ingrese su salario mensual: "))

if salario < 10000:
    impuesto = 0
elif salario <= 30000:
    impuesto = salario * 0.10
else:
    impuesto = salario * 0.20

print(f"El impuesto a pagar es: ${impuesto:.2f}")
'''


#Clasificación de números

'''
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 > 0 and num2 > 0 and num3 > 0:
    print("Todos los números son positivos.")
elif num1 < 0 and num2 < 0 and num3 < 0:
    print("Todos los números son negativos.")
elif num1 == 0 or num2 == 0 or num3 == 0:
    print("Al menos uno de los números es cero.")
else:
    print("Los números son mixtos (positivos y negativos).")
'''


#Verificación de año bisiesto

'''
año = int(input("Ingrese un año: "))

# Determinar si es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
'''


#Conversión de calificaciones

'''
calificacion = int(input("Ingrese la calificación: "))

if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion <= 89:
    letra = "B"
elif 70 <= calificacion <= 79:
    letra = "C"
elif 60 <= calificacion <= 69:
    letra = "D"
elif 0 <= calificacion <= 59:
    letra = "F"
else:
    letra = "Calificación inválida"

print(f"La calificación en letra es: {letra}")
'''


#Comparación de tres longitudes

'''
lado1 = float(input("Ingrese la primera longitud: "))
lado2 = float(input("Ingrese la segunda longitud: "))
lado3 = float(input("Ingrese la tercera longitud: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Las longitudes pueden formar un triángulo.")
else:
    print("Las longitudes NO pueden formar un triángulo.")
'''


#Calculadora de descuentos

'''
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if temperatura < 0:
    mensaje = "Hace mucho frío"
elif 0 <= temperatura <= 20:
    mensaje = "Clima fresco"
elif 21 <= temperatura <= 30:
    mensaje = "Clima agradable"
else:
    mensaje = "Hace mucho calor"

print(mensaje)
'''


#Conversión de horas a turnos

'''
hora = int(input("Ingrese la hora (0-23): "))

if 6 <= hora <= 11:
    momento = "Mañana"
elif 12 <= hora <= 17:
    momento = "Tarde"
elif 18 <= hora <= 23:
    momento = "Noche"
elif 0 <= hora <= 5:
    momento = "Madrugada"
else:
    momento = "Hora inválida. Debe estar entre 0 y 23."

print(momento)
'''


#Clasificación de IMC

'''
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc <= 24.9:
    clasificacion = "Normal"
elif 25 <= imc <= 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Su IMC es: {imc:.2f}")
print(f"Clasificación: {clasificacion}")
'''