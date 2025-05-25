#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario
def factorial(num):
    if num == 0:
        return 0
    else:
        return num + factorial(num-1)
    
numero = int(input("Ingrese un numero: "))
for i in range(numero):
    print(f"El factorial de {i+1} es: {factorial(i+1)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def mostrar_fibonacci(hasta):
    print(f"Serie de fibonacci hasta la posicion {hasta}")
    for i in range (hasta+1):
        print(fibonacci(i), end=" ")

numero = int(input("Ingresa un numero: "))
mostrar_fibonacci(numero)

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un algoritmo general.
def potencia(base,exp):
    if exp == 0:
        return 1
    elif exp==1:
        return base
    else:
        return base  * potencia(base,exp-1);

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"El resultado es: {potencia(base,exponente)}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
def conversion_dec_bin(decimal):
    if decimal<2:
        return str(round(decimal))
    else:
        return  str(conversion_dec_bin(round(decimal/2))) + str(round(decimal%2))
def conversion_dec_bin_otra_manera(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return conversion_dec_bin_otra_manera(decimal // 2) + str(decimal % 2)

decimal = int(input("Ingrese un numero: "))
print(f"El numero {decimal} en binario es: {conversion_dec_bin(decimal)}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
def es_polindromo(palabra):
    if len(palabra)<=1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_polindromo(palabra[1:-1])

palabra = input("Ingrese una palabra: ")
print(es_polindromo(palabra))

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(numero):
    if numero<10:
        return numero
    else: return numero%10 + suma_digitos(int(numero/10))

numero = int(input("Ingrese un numero: "))
print(f"La suma de los digitos de {numero} es: {suma_digitos(numero)}")

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
    
bloques = int(input("Ingrese un numero: "))
print(f"El numero de bloques necesario es: {contar_bloques(bloques)}")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese un digito: "))
print(f"El digito({digito}) aparece: {contar_digito(numero, digito)} veces")