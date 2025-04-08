#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i);

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
n = int(input("Ingrese un numero entero: "))
cont=1
while(n>=10):
    cont+=1
    n/=10
print(f"Su numero contiene {cont} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
n1=int(input("Ingrese el primer numero entero: "))
n2=int(input("Ingrese el primer numero entero: "))
cont=0;
for i in range(n1+1,n2):
    cont+=i;
print(f"La suma de todos los numeros comprendidos entre {n1} y {n2} es de: {cont}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
cont=0;
n=int(input("Ingrese un numero entero distinto de 0: "))
while(n!=0):
    cont+=n;
    n=int(input("Ingrese un numero entero: "));
print(f"La suma de todos los numeros ingresados es de: {cont}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random;
r=random.randint(0, 9)
cont=1
n=int(input("Ingrese un numero entero del 0 al 9: "))
while(n!=r):
    cont+=1
    n=int(input("Ingrese un numero entero del 0 al 9: "))
print(f"Felicidades, el numero era: {r}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100,-1,-2):
    print(i);

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
n=int(input("Ingrese un numero entero: "))
suma=0;
for i in range(0,n+1):
    suma+=i;
print(f"La suma de todos los numeros comprendidos entre 0 y {n} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares=0
impares=0
positivos=0
negativos=0
for i in range (100):
    n=int(input("Ingresar un numero entero: "))
    if(n%2==0):
        pares+=1
    else:
        impares+=1
    if(n>=0):
        positivos+=1
    else:
        negativos+=1
print(f"Hay {pares} numeros pares, {impares} numeros impares, {positivos} son positivos y {negativos} son numeros negativos.")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
from statistics import mean
numeros=[]
for i in range(100):
    n=int(input(f"Ingrese el {i+1} numero entero: "))
    numeros.append(n)
print(f"La media de todos los numeros ingresados es: {mean(numeros)}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
dig=0
inv=0
n=int(input("Ingrese un numero entero: "))
while(n!=0):
    dig=n%10
    n=int(n/10)
    inv=inv*10+dig
print(f"El inverso del numero es: {inv}")