import random #para poder hacer el ejercicio 6
from statistics import mode, median, mean #para poder hacer el ejercicio 6


#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingrese un numero par: "))
if numero%2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#otra manera:
numero = int(input("Ingresar un numero par: "))
while(numero%2!=0):
    numero = int(input("Ingrese un numero par: "))
if numero%2 == 0:
    print("Ha ingresado un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años
edad = int(input("Ingrese su edad: "))
while(edad<0 or edad>150):
    edad = int(input("Ingrese una edad valida: "))
if edad<12:
    print("Niño/a")
elif edad>=12 and edad<18:
    print("Adolescente")
elif edad>=18 and edad<30:
    print("Adulto/a joven")
else:
    print("Adulto/a mayor")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string
password = input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")
while not(len(password)>=8 and len(password)<=14):
    password = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(password)>=8 and len(password)<=14:
    print("Ha ingresado una contraseña correcta")

#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#mean = promedio de los datos.
#median = valor central (mediana) de los datos
#mode = valor mas comun (moda unica) de datos discretos o nominales
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
if mean(numeros_aleatorios)>median(numeros_aleatorios) and median(numeros_aleatorios)>mode(numeros_aleatorios):
    print(f"{numeros_aleatorios} \nSesgo positivo o a la derecha")
elif mean(numeros_aleatorios)<median(numeros_aleatorios) and median(numeros_aleatorios)<mode(numeros_aleatorios):
    print(f"{numeros_aleatorios} \nSesgo negativo o a la izquierda")
else:
    print(f"{numeros_aleatorios} \nSin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
string = input("Ingrese una frase o palabra: ")
if string[-1]=='a' or string[-1]=='e' or string[-1]=='i' or string[-1]=='o' or string[-1]=='u':
    print(f"{string}!")
else:
    print(f"{string}")

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ")
print("\nDada las siguientes opciones:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula\n")
opcion = int(input("Ingrese la opcion que desee: "))
match opcion:
        case 1:
            print(nombre.upper())  # Convierte todo a mayúsculas
        case 2:
            print(nombre.lower())  # Convierte todo a minúsculas
        case 3:
            print(nombre.title())  # Convierte la primera letra en mayúscula
        case _:
            print("Opción no válida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = int(input("Ingrese la magnitud del terremoto: "))
if magnitud<3:
    print("Muy leve")
elif magnitud>=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud<6:
    print("Fuerte")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte")
elif magnitud>=7:
    print("Extremo")

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ")
mes = int(input("Ingrese el numero del mes en el que se encuentra: "))
dia = int(input("Ingrese el numero del dia en el que se encuentra: "))

if ((hemisferio=='n' or hemisferio=='N') and ((mes==12 and dia>=21) or ((mes>=1 and mes<=3) and (dia>=1 and dia<=20)))) or ((hemisferio=='s' or hemisferio=='S') and ((mes==6 and dia>=21) or ((mes>=7 and mes<=9) and (dia>=1 and dia<=20)))):
    print("Invierno")
elif ((hemisferio=='n' or hemisferio=='N') and ((mes==3 and dia>=21) or ((mes>=4 and mes<=6) and (dia>=1 and dia<=20)))) or ((hemisferio=='s' or hemisferio=='S') and ((mes==9 and dia>=21) or ((mes>=9 and mes<=11) and (dia>=1 and dia<=20)))):
    print("Primavera")
elif ((hemisferio=='n' or hemisferio=='N') and ((mes==6 and dia>=21) or ((mes>=6 and mes<=8) and (dia>=1 and dia<=20)))) or ((hemisferio=='s' or hemisferio=='S') and ((mes==11 and dia>=21) or ((mes>=11 and mes<=12 or mes==1) and (dia>=1 and dia<=20)))):
    print("Verano")
else:
    print("Otoño")