#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario(input("Ingrese su nombre: "))

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(input("Ingrese su nombre: "),input("Ingrese su apellido: "),input("Ingrese su edad: "),input("Ingrese su lugar de residencia: "))

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math
def calcular_area_circulo(radio):
    a = float (math.pi*(radio**2))
    return round(a,2)

def calcular_perimetro_circulo(radio):
    p = float (2*math.pi*radio)
    return round(p,2)

r = float(input("Ingresar el radio del circulo: "))
a = calcular_area_circulo(r)
p = calcular_perimetro_circulo(r)
print(f"El area del circulo es: {a} y el perimetro es: {p}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

print(f"Esa cantidad de segundos son: {segundos_a_horas(float(input("Ingrese la cantidad de segundos: ")))} horas")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range (10):
        print(f"{numero}x{i+1} = {numero*(i+1)}")

tabla_multiplicar(int(input("Ingrese un numero entero: ")))

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    mutiplicacion = a*b
    division = a/b
    return (suma, resta, mutiplicacion, division)

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a,b)

print(f"La suma de los numeros es: {resultados[0]}, la resta del primero con el segundo es: {resultados[1]}, la multiplicacion de los numeros es: {resultados[2]} y la division del primero sobre el segundo es: {resultados[3]}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return round(imc,2)

print(f"Su IMC es de: {calcular_imc(float(input("Ingrese su peso en kilogramos: ")),float(input("Ingrese su altura en metros: ")))}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius):
    f = celsius*1.8+32
    return f

print(f"Esa temperatura son {celsius_a_fahrenheit(float(input("Ingrese la temperatura en grados Celsius: ")))} grados Fahrenheit")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
#Para este ejercicio ya existe una funcion que es mean() dentro de la biblioteca de statistics
def calcular_promedio(a, b, c):
    promedio = float((a+b+c)/3)
    return promedio

print(f"El promedio de los 3 numeros es de: {calcular_promedio(int(input("Ingrese el primero numero: ")),int(input("Ingrese el segundo numero: ")),int(input("Ingrese el tercer numero: ")))}")