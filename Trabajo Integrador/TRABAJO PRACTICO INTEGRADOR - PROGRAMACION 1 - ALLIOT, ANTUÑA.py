import random # Para generar datos de prueba
import time

# Definición de la función insertion_sort para ordenar la lista de tareas
def insertion_sort_tareas(lista_tareas):
    # Recorremos la lista desde el segundo elemento (índice 1)
    # ya que el primer elemento se considera la sublista ordenada inicial.
    for i in range(1, len(lista_tareas)):
        # Guardamos el elemento actual que queremos insertar en su posición correcta.
        tarea_actual = lista_tareas[i] 
        # Guardamos la prioridad de la tarea actual para las comparaciones.
        prioridad_actual = tarea_actual['prioridad']    
        
        # Inicializamos j al índice del elemento anterior al actual.
        j = i - 1
        
        # Movemos los elementos de la sublista ordenada (lista_tareas[0...i-1])
        # que tienen una prioridad menor (representada por un número mayor) 
        # que la prioridad_actual, una posición hacia adelante para hacer 
        # espacio para la tarea_actual.
        # Se asume que un menor número de 'prioridad' significa mayor urgencia.
        while j >= 0 and prioridad_actual < lista_tareas[j]['prioridad']:
            lista_tareas[j + 1] = lista_tareas[j]
            j -= 1
        
        # Insertamos la tarea_actual en su posición correcta dentro de la sublista ordenada.
        lista_tareas[j + 1] = tarea_actual
    return lista_tareas


# Función de partición (utilizando el esquema de Lomuto)
def partition(arr, low, high):
    # Se elige el último elemento como pivote. 
    # Mejoras comunes incluyen seleccionar un pivote aleatorio o la mediana de tres 
    # para mitigar el riesgo del peor caso.
    pivot = arr[high]
    i = low - 1  # 'i' es el índice del último elemento que es menor que el pivote.

    # Se recorren los elementos desde 'low' hasta 'high-1'.
    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote.
        if arr[j] <= pivot:
            i += 1 # Se incrementa el índice 'i'.
            arr[i], arr[j] = arr[j], arr[i] # Se intercambia arr[i] con arr[j].
                                         # Esto mueve los elementos menores que el pivote a la izquierda.
    
    # Finalmente, se coloca el pivote en su posición correcta.
    # Se intercambia arr[i+1] (el primer elemento mayor que el pivote) con arr[high] (el pivote).
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 # Se retorna el índice donde el pivote ha sido colocado.

# Función principal de Quick Sort
def quick_sort(arr, low, high):
    if low < high: # Condición base: si hay más de un elemento para ordenar.
        # 'pi' es el índice de partición. arr[pi] está ahora en su lugar definitivo.
        pi = partition(arr, low, high)

        # Se ordenan recursivamente los elementos antes de la partición
        # y después de la partición.
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr # Retorna el arreglo ordenado (la modificación es in-place).


# Función Counting Sort para ordenar edades dentro de un rango conocido
def counting_sort_edades(lista_edades, min_edad, max_edad):
    # El tamaño del array de conteo (count_array) se determina por el rango de edades.
    # rango_edades = max_edad - min_edad + 1
    # count_array[i] almacenará el número de ocurrencias de la edad (min_edad + i).
    count_array = [0] * (max_edad - min_edad + 1)
    
    # El array de salida (output_array) tendrá el mismo tamaño que la lista original.
    output_array = [0] * len(lista_edades)

    # Paso 1: Contar la frecuencia de cada edad.
    # Se itera sobre la lista de edades original.
    for edad in lista_edades:
        # Se verifica que la edad esté dentro del rango esperado.
        if min_edad <= edad <= max_edad:
            # Se incrementa el contador para la edad correspondiente.
            # Se ajusta la edad al índice del count_array restando min_edad.
            count_array[edad - min_edad] += 1
        # else: Aquí se podría manejar edades fuera de rango (e.g., ignorar, registrar error).
    
    # Paso 2: Modificar el count_array para que cada índice
    # almacene la posición acumulada. Es decir, count_array[i] contendrá
    # la suma de las frecuencias de las edades hasta (min_edad + i).
    # Esto indica la posición final (basada en 1) de los elementos con esa edad en el output_array.
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # Paso 3: Construir el array de salida (output_array).
    # Se itera la lista_edades original en orden inverso. Esto es importante
    # para mantener la estabilidad del algoritmo (si hubiera datos asociados a las edades).
    for i in range(len(lista_edades) - 1, -1, -1):
        edad_actual = lista_edades[i]
        if min_edad <= edad_actual <= max_edad:
            # La posición en output_array se determina por count_array[edad_actual - min_edad] - 1
            # (se resta 1 porque las posiciones del array son base 0).
            output_array[count_array[edad_actual - min_edad] - 1] = edad_actual
            # Se decrementa el conteo para la edad actual, para colocar correctamente
            # la próxima ocurrencia de la misma edad (si existe) en la posición anterior.
            count_array[edad_actual - min_edad] -= 1
    
    return output_array

# Adaptación de insertion_sort para listas de enteros
def insertion_sort_enteros(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# Adaptación de quick_sort para listas de diccionarios por clave 'prioridad'
def quick_sort_tareas(arr, low, high):
    def partition_tareas(arr, low, high):
        pivot = arr[high]['prioridad']
        i = low - 1
        for j in range(low, high):
            if arr[j]['prioridad'] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    if low < high:
        pi = partition_tareas(arr, low, high)
        quick_sort_tareas(arr, low, pi - 1)
        quick_sort_tareas(arr, pi + 1, high)
    return arr

# Adaptación de counting_sort para listas de diccionarios por clave 'prioridad'
def counting_sort_tareas(lista_tareas, min_prioridad, max_prioridad):
    count_array = [[] for _ in range(max_prioridad - min_prioridad + 1)]
    for tarea in lista_tareas:
        idx = tarea['prioridad'] - min_prioridad
        count_array[idx].append(tarea)
    output = []
    for bucket in count_array:
        output.extend(bucket)
    return output




# --- Ejemplo de uso con tareas (diccionarios) ---
print("Ejemplo de uso para los tres algoritmos con tareas (diccionarios):")
tareas = [
    {'descripcion': 'Preparar presentación para reunión', 'prioridad': 1},
    {'descripcion': 'Analizar resultados trimestrales', 'prioridad': 1},
    {'descripcion': 'Llamar a proveedor de insumos', 'prioridad': 1},
    {'descripcion': 'Reunión con el equipo de ventas', 'prioridad': 1},
    {'descripcion': 'Responder consultas de soporte', 'prioridad': 1},
    {'descripcion': 'Revisar contratos legales', 'prioridad': 1},
    {'descripcion': 'Enviar informe mensual', 'prioridad': 2},
    {'descripcion': 'Actualizar base de datos de clientes', 'prioridad': 2},
    {'descripcion': 'Realizar backup del sistema', 'prioridad': 2},
    {'descripcion': 'Revisar presupuesto anual', 'prioridad': 2},
    {'descripcion': 'Enviar cotización a cliente', 'prioridad': 2},
    {'descripcion': 'Solicitar materiales de oficina', 'prioridad': 2},
    {'descripcion': 'Planificar campaña de marketing', 'prioridad': 2},
    {'descripcion': 'Actualizar inventario', 'prioridad': 2},
    {'descripcion': 'Auditoría interna de procesos', 'prioridad': 3},
    {'descripcion': 'Capacitación del nuevo empleado', 'prioridad': 3},
    {'descripcion': 'Actualizar página web', 'prioridad': 3},
    {'descripcion': 'Organizar archivos del proyecto', 'prioridad': 3},
    {'descripcion': 'Revisar correos pendientes', 'prioridad': 3},
    {'descripcion': 'Coordinar evento corporativo', 'prioridad': 3},
]
nueva_tarea = {'descripcion': 'Agendar revisión de proyecto alfa', 'prioridad': 1}
tareas.append(nueva_tarea)

print("Lista de tareas antes de ordenar:")
for tarea in tareas:
    print(f"  - {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")

# Insertion Sort
tareas1 = [t.copy() for t in tareas]
start_time = time.time()
insertion_sort_tareas(tareas1)
elapsed_insertion = time.time() - start_time

# Quick Sort
tareas2 = [t.copy() for t in tareas]
start_time = time.time()
quick_sort_tareas(tareas2, 0, len(tareas2) - 1)
elapsed_quick = time.time() - start_time

# Counting Sort
tareas3 = [t.copy() for t in tareas]
start_time = time.time()
tareas3 = counting_sort_tareas(tareas3, 1, 3)
elapsed_counting = time.time() - start_time

print("\nComparación de tiempos de ordenamiento para tareas:")
print(f"Insertion Sort: {elapsed_insertion:.6f} segundos")
print(f"Quick Sort:     {elapsed_quick:.6f} segundos")
print(f"Counting Sort:  {elapsed_counting:.6f} segundos\n")
print("Resultado ordenado (Insertion Sort):")
for tarea in tareas3:
    print(f"  - {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")

# --- Ejemplo de uso con IDs de productos (enteros) ---
print("\nEjemplo de uso para los tres algoritmos con IDs de productos (enteros):")
product_ids = [random.randint(10000, 99999) for _ in range(20)]
print("Lista de IDs de productos antes de ordenar:")
print(product_ids[:20])

# Insertion Sort
ids1 = product_ids[:]
start_time = time.time()
insertion_sort_enteros(ids1)
elapsed_insertion = time.time() - start_time

# Quick Sort
ids2 = product_ids[:]
start_time = time.time()
quick_sort(ids2, 0, len(ids2) - 1)
elapsed_quick = time.time() - start_time

# Counting Sort
ids3 = product_ids[:]
min_id = min(ids3)
max_id = max(ids3)
start_time = time.time()
ids3 = counting_sort_edades(ids3, min_id, max_id)
elapsed_counting = time.time() - start_time

print("\nComparación de tiempos de ordenamiento para IDs de productos:")
print(f"Insertion Sort: {elapsed_insertion:.6f} segundos")
print(f"Quick Sort:     {elapsed_quick:.6f} segundos")
print(f"Counting Sort:  {elapsed_counting:.6f} segundos\n")
print("Resultado ordenado (Quick Sort):")
print(ids3[:20])

# --- Ejemplo de uso con edades (enteros) ---
print("\nEjemplo de uso para los tres algoritmos con edades de encuestados (enteros):")
edades_encuestados = [random.randint(18, 99) for _ in range(9999)]
print("Lista de edades antes de ordenar:")
print(edades_encuestados[:20])

# Insertion Sort
edades1 = edades_encuestados[:]
start_time = time.time()
insertion_sort_enteros(edades1)
elapsed_insertion = time.time() - start_time

# Quick Sort
edades2 = edades_encuestados[:]
start_time = time.time()
quick_sort(edades2, 0, len(edades2) - 1)
elapsed_quick = time.time() - start_time

# Counting Sort
edades3 = edades_encuestados[:]
min_rango_edad = 18
max_rango_edad = 99
start_time = time.time()
edades3 = counting_sort_edades(edades3, min_rango_edad, max_rango_edad)
elapsed_counting = time.time() - start_time

print("\nComparación de tiempos de ordenamiento para edades:")
print(f"Insertion Sort: {elapsed_insertion:.6f} segundos")
print(f"Quick Sort:     {elapsed_quick:.6f} segundos")
print(f"Counting Sort:  {elapsed_counting:.6f} segundos\n")
print("Resultado ordenado (Counting Sort):")
print(edades3[:20])




def encontrar_error_en_logs(logs, codigo_error):
    """
    Encuentra un código de error en una lista de logs no ordenada.
    """
    for i in range(len(logs)):
        # Revisa cada log para ver si contiene el código de error.
        if codigo_error in logs[i]:
            return i # Retorna el índice del primer log con el error.
    return -1 # Retorna -1 si no se encuentra.

# --- Ejemplo de uso ---
log_stream = [
    "INFO: User logged in",
    "DEBUG: Cache updated",
    "WARN: Disk space low",
    "ERROR-500: Database connection failed",
    "INFO: Process completed"
]
codigo_a_buscar = "ERROR-500"
indice = encontrar_error_en_logs(log_stream, codigo_a_buscar)

if indice != -1:
    print(f"\nCódigo '{codigo_a_buscar}' encontrado en el log {indice}.\n")
else:
    print(f"\nCódigo '{codigo_a_buscar}' no encontrado.\n")


def buscar_en_diccionario(palabras, palabra_buscada):
    """
    Busca una palabra en una lista ordenada alfabéticamente.
    """
    bajo, alto = 0, len(palabras) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        palabra_media = palabras[medio]
        
        if palabra_media == palabra_buscada:
            return True # Palabra encontrada
        elif palabra_media < palabra_buscada:
            bajo = medio + 1 # Buscar en la mitad derecha
        else:
            alto = medio - 1 # Buscar en la mitad izquierda
            
    return False # Palabra no encontrada

# --- Ejemplo de uso ---
# (Una pequeña muestra de un diccionario ordenado)
diccionario = ["algoritmo", "binario", "compilador", "debugging", "estructura"]
palabra = "debugging"

if buscar_en_diccionario(diccionario, palabra):
    print(f"La palabra '{palabra}' está en el diccionario.")
else:
    print(f"La palabra '{palabra}' no está en el diccionario.")