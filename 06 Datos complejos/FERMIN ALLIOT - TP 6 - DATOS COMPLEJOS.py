#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melon"]=2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
lista_frutas= list(precios_frutas.keys())
print(lista_frutas)

#4) Crear una clase llamada Persona que contenga un método __init__ con los atributos\ nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

Fermin = Persona("Fermin","Argentina",24)
Fermin.saludar()

#5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
#Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return round(float(math.pi*(self.radio**2)),2)

    def calcular_perimetro(self):
        return round(float (2*math.pi*self.radio),2)

circulo1 = Circulo(3)
print(f"El area del circulo1 es: {circulo1.calcular_area()} y el perimetro del mismo es: {circulo1.calcular_perimetro()}")

#6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.
def esta_balanceado(texto):
    pila1 = Pila()
    for caracter in texto:
        if (caracter=="{" or caracter=="[" or caracter=="("):
            pila1.apilar(caracter)
        elif (caracter=="}" or caracter=="]" or caracter==")"):
            if(pila1.esta_vacia()):
                return False
            else:
                ultimo = pila1.desapilar()
                if((ultimo=="{" and caracter=="}") or (ultimo=="[" and caracter=="]") or (ultimo=="(" and caracter==")")):
                    pass
                else: return False
    if (pila1.esta_vacia()):
        return True
    else:
        return False

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else "La pila esta vacia"
    
    def ver_tope(self):
        return self.elementos[-1] if not self.esta_vacia() else "La pila esta vacia"

cadena = "{[()]}"
cadena1 = "([]){}"
cadena2 = "([)]"
cadena3 = "((("
print(esta_balanceado(cadena2))

#7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
# Agregar clientes (encolar).
# Atender clientes (desencolar).
# Mostrar el siguiente cliente en la fila.
from collections import deque
class Cola:
    def __init__(self):
        self.elementos = deque()

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def desencolar(self):
        return self.elementos.popleft() if not self.esta_vacia() else "La cola esta vacia"
    
    def ver_frente(self):
        return self.elementos[0] if not self.esta_vacia() else "La cola esta vacia"
    
    def mostrar_cola(self):
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            print("Contenido de la cola:")
            for elemento in self.elementos:
                print(f"{elemento}")


cola1 = Cola()
print("La cola1 es: ")
cola1.mostrar_cola()

cola1.encolar(1)
cola1.encolar(2)
cola1.encolar(3)
print("La cola1 despues de encolar el 1, 2 y 3: ")
cola1.mostrar_cola()

cola1.desencolar()
print("La cola1 despues de desencolar: ")
cola1.mostrar_cola()

#8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados.
#y
#9) Dada una lista enlazada, implementa una función para invertirla.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato) #se crea el nuevo nodo (3)      // se crea el nuevo nodo (2)    // se crea el nuevo nodo (1)
        nuevo_nodo.siguiente = self.cabeza #el puntero -> None  // el puntero -> 3              // el puntero -> 2
        self.cabeza = nuevo_nodo #Cabeza(None) = 3              // cabeza(3) = 2                // cabeza(2) = 1

    def mostrar(self):
        actual = self.cabeza
        while (actual):
            print(actual.dato, end= " -> ")
            actual = actual.siguiente
        print("None")

    def invertir_lista(self):
        actual = self.cabeza
        siguiente = actual.siguiente
        anterior = None
        while(actual):
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior


lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
lista.mostrar()
lista.invertir_lista()
lista.mostrar()