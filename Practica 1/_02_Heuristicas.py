import heapq
#se crea el grafo
grafo = {
    
    'Jalisco': {'Nayarit': 14, 'Zacatecas': 7},
    'Nayarit': {'Jalisco': 11, 'Durango': 10, 'Sinaloa': 1},
    'Zacatecas': {'Jalisco': 5, 'Durango': 2, 'Nuevo Leon': 14, 'Coahuila': 3},
    'Durango': {'Zacatecas': 8, 'Nayarit': 4, 'Coahuila': 15, 'Chihuahua': 6, 'Sinaloa': 12},
    'Coahuila': {'Zacatecas': 9, 'Durango': 13, 'Nuevo Leon': 1, 'Chihuahua': 7},
    'Nuevo Leon': {'Zacatecas': 10, 'Coahuila': 11},
    'Chihuahua': {'Durango': 14, 'Sinaloa': 8, 'Coahuila': 5, 'Sonora': 3},
    'Sinaloa': {'Nayarit': 13, 'Durango': 7, 'Sonora': 9, 'Chihuahua': 15},
    'Sonora': {'Sinaloa': 9, 'Chihuahua': 15, 'Baja California': 10},
    'Baja California': {'Sonora': 2}
}
def busqueda(grafo, inicio, objetivo):  # Se crea un método llamado busqueda
    frontera = []  # Se inicializa una lista vacía llamada frontera
    heapq.heappush(frontera, (0, [inicio]))  # Se inserta el nodo inicial en la frontera con una heurística de 0
    visitados = set()  # Se crea un conjunto vacío para almacenar los nodos visitados

    while frontera:  # Mientras la frontera no esté vacía
        _, camino_actual = heapq.heappop(frontera)  # Se extrae el nodo con menor heurística de la frontera
        nodo_actual = camino_actual[-1]  # Se obtiene el último nodo del camino actual

        if nodo_actual == objetivo:  # Si el nodo actual es el objetivo
            return camino_actual  # Se devuelve el camino actual

        visitados.add(nodo_actual)  # Se añade el nodo actual al conjunto de visitados

        for vecino, peso in grafo[nodo_actual].items():  # Para cada vecino del nodo actual
            if vecino not in visitados:  # Si el vecino no ha sido visitado
                nuevo_camino = list(camino_actual)  # Se crea un nuevo camino copiando el camino actual
                nuevo_camino.append(vecino)  # Se añade el vecino al nuevo camino
                valor_heuristico = peso  # Se asigna el peso como valor heurístico
                heapq.heappush(frontera, (valor_heuristico, nuevo_camino))  # Se inserta el nuevo camino en la frontera

    return None  # Si no se encuentra un camino, se devuelve None

print("Estados: \nJalisco, Nayarit, Zacatecas, Durango, Coahuila, Nuevo Leon, Chihuahua, Sinaloa, Sonora, Baja California")#Se imprime un menu
est_inicio = input("Ingrese el estado de partida: ") #Se solicita una entrada
est_objetivo = input("Ingrese el estado est_objetivo: ") #Se solicita una entrada
ruta = busqueda(grafo, est_inicio, est_objetivo) #se llama a la funcion de busqueda
if ruta: #Si la ruta es verdadera imprimos la ruta
    print(f"Se encontró un ruta de {est_inicio} a {est_objetivo}: {' -> '.join(ruta)}")
else:
    print(f"No se encontró un ruta de {est_inicio} a {est_objetivo}.")#Si no se encuentra la ruta imprime el msg

