def busqueda_bidireccional(grafo, inicio, objetivo):#Se define la función de búsqueda bidireccional
    visitados_inicio = set() #Se inicializa un conjunto para los nodos visitados desde el inicio
    visitados_objetivo = set() #Se inicializa un conjunto para los nodos visitados desde el objetivo
    
    frontera_inicio = [inicio] #Se inicializa una lista para los nodos frontera desde el inicio
    frontera_objetivo = [objetivo] #Se inicializa una lista para los nodos frontera desde el objetivo
    
    while frontera_inicio and frontera_objetivo: #Se inicia un bucle mientras haya nodos en ambas fronteras
        actual_inicio = frontera_inicio.pop(0) #Se extrae y se obtiene el primer nodo de la frontera de inicio
        visitados_inicio.add(actual_inicio) #Se añade el nodo actual al conjunto de visitados desde el inicio
        
        if actual_inicio in visitados_objetivo: #Se verifica si el nodo actual ya fue visitado desde el objetivo
            return actual_inicio #Si es así, se retorna el nodo actual como punto de intersección
        
        actual_objetivo = frontera_objetivo.pop(0) #Se extrae y se obtiene el primer nodo de la frontera de objetivo
        visitados_objetivo.add(actual_objetivo) #Se añade el nodo actual al conjunto de visitados desde el objetivo
        
        if actual_objetivo in visitados_inicio: #Se verifica si el nodo actual ya fue visitado desde el inicio
            return actual_objetivo #Si es así, se retorna el nodo actual como punto de intersección
        
        for vecino in grafo[actual_inicio]: #Se itera sobre los vecinos del nodo actual desde el inicio
            if vecino not in visitados_inicio and vecino not in frontera_inicio: #Se verifica que el vecino no esté visitado ni en la frontera
                frontera_inicio.append(vecino) #Se añade el vecino a la frontera de inicio
        
        for vecino in grafo[actual_objetivo]: #Se itera sobre los vecinos del nodo actual desde el objetivo
            if vecino not in visitados_objetivo and vecino not in frontera_objetivo: #Se verifica que el vecino no esté visitado ni en la frontera
                frontera_objetivo.append(vecino) #Se añade el vecino a la frontera de objetivo
    
    return None #Si no se encuentra un punto de intersección, se retorna None


graph = {
    'Jalisco': ['Nayarit', 'Zacatecas'], #Se define una lista de vecinos para el nodo 'Jalisco'
    'Nayarit': ['Jalisco', 'Durango', 'Sinaloa'], #Se define una lista de vecinos para el nodo 'Nayarit'
    'Zacatecas': ['Jalisco', 'Durango', 'Nuevo Leon', 'Coahuila'], #Se define una lista de vecinos para el nodo 'Zacatecas'
    'Durango': ['Zacatecas', 'Nayarit', 'Coahuila', 'Chihuahua', 'Sinaloa'], #Se define una lista de vecinos para el nodo 'Durango'
    'Coahuila': ['Zacatecas', 'Durango', 'Nuevo Leon', 'Chihuahua'], #Se define una lista de vecinos para el nodo 'Coahuila'
    'Nuevo Leon': ['Zacatecas', 'Coahuila'], #Se define una lista de vecinos para el nodo 'Nuevo Leon'
    'Chihuahua': ['Durango', 'Sinaloa', 'Coahuila', 'Sonora'], #Se define una lista de vecinos para el nodo 'Chihuahua'
    'Sinaloa': ['Nayarit', 'Durango', 'Sonora', 'Chihuahua'], #Se define una lista de vecinos para el nodo 'Sinaloa'
    'Sonora': ['Sinaloa', 'Chihuahua', 'Baja California'], #Se define una lista de vecinos para el nodo 'Sonora'
    'Baja California': ['Sonora'] #Se define una lista de vecinos para el nodo 'Baja California'
}

print("Estados: \nJalisco, Nayarit, Zacatecas, Durango, Coahuila, Nuevo Leon, Chihuahua, Sinaloa, Sonora, Baja California")#Se imprime un menu
est_inicio = input("Ingrese el estado de partida: ") #Se solicita una entrada
est_objetivo = input("Ingrese el estado est_objetivo: ") #Se solicita una entrada
print("El nodo de intersección es: ", busqueda_bidireccional(graph, est_inicio, est_objetivo)) #Imprime el nodo de interseccion
