import heapq

class Grafo: #inciamos una clase de Grafos que contiene los metodos necesarios para trabajar
    def __init__(self): #constructor de la clase
        self.vertices = {} #incializamos los el diccionario para vertices y aristas

    def add_vertice(self, vertice): #funcion para agregar vertices a nuestro diccionario
        if vertice not in self.vertices: #condicion que verifica que el vertice no exista en el diccionario
            self.vertices[vertice] = [] #agrega el vertice


    def add_arista(self, inicio, fin, costo): #función para agregar aristas a nuestro diccionario
        self.add_vertice(inicio) #llama a la función para agregar el vértice de inicio si aún no existe
        self.add_vertice(fin) #llama a la función para agregar el vértice de fin si aún no existe
        self.vertices[inicio][fin] = costo #establece el costo de la arista del inicio al finError
        
        self.vertices[fin][inicio] = costo #establece el costo de la arista del fin al inicio, ya que el grafo es no dirigido

    def costo_uniforme(self, inicio, destino): #función para calcular el camino de costo mínimo desde un vértice de inicio a un destino
        cola_prioridad = [(0, inicio)] #inicializa la cola de prioridad con el vértice de inicio y un costo inicial de 0
        visitados = set() #crea un conjunto para llevar un registro de los vértices visitados

        while cola_prioridad: #bucle que se ejecuta mientras haya elementos en la cola de prioridad
            costo, nodo = heapq.heappop(cola_prioridad) #obtiene el nodo con el menor costo de la cola de prioridad
            if nodo not in visitados: #verifica si el nodo no ha sido visitado
                visitados.add(nodo) #agrega el nodo al conjunto de visitados
                if nodo == destino: #verifica si el nodo actual es el destino
                    return costo #devuelve el costo acumulado hasta el nodo destino
                for vecino, costo_arista in self.vertices[nodo].items(): #itera sobre los vecinos del nodo actual
                    if vecino not in visitados: #verifica si el vecino no ha sido visitado
                        new_cost = costo + costo_arista #calcula el nuevo costo acumulado
                        heapq.heappush(cola_prioridad, (new_cost, vecino)) #agrega el vecino a la cola de prioridad con el nuevo costo

        return float('inf') #devuelve infinito si no se encuentra un camino al destino


grafo = Grafo()
grafo.add_arista('Jalisco', 'Nayarit', 1) # Agregamos las aristas de los vertices
grafo.add_arista('Jalisco', 'Zacatecas', 2) # Agregamos las aristas de los vertices
grafo.add_arista('Zacatecas', 'Durango', 3) # Agregamos las aristas de los vertices
grafo.add_arista('Zacatecas', 'Nuevo Leon', 4) # Agregamos las aristas de los vertices
grafo.add_arista('Zacatecas', 'Coahuila', 5) # Agregamos las aristas de los vertices
grafo.add_arista('Nayarit', 'Durango', 6) # Agregamos las aristas de los vertices
grafo.add_arista('Nayarit', 'Sinaloa', 7) # Agregamos las aristas de los vertices
grafo.add_arista('Durango', 'Coahuila', 8) # Agregamos las aristas de los vertices
grafo.add_arista('Durango', 'Chihuahua', 9) # Agregamos las aristas de los vertices
grafo.add_arista('Durango', 'Sinaloa', 10) # Agregamos las aristas de los vertices
grafo.add_arista('Sinaloa', 'Sonora', 1) # Agregamos las aristas de los vertices
grafo.add_arista('Sinaloa', 'Chihuahua', 2) # Agregamos las aristas de los vertices
grafo.add_arista('Coahuila', 'Nuevo Leon', 3) # Agregamos las aristas de los vertices
grafo.add_arista('Coahuila', 'Chihuahua', 4) # Agregamos las aristas de los vertices
grafo.add_arista('Chihuahua', 'Sonora', 5) # Agregamos las aristas de los vertices
grafo.add_arista('Sonora', 'Baja California', 6) # Agregamos las aristas de los vertices


print("Estados: \nJalisco, Nayarit, Zacatecas, Durango, Coahuila, Nuevo Leon, Chihuahua, Sinaloa, Sonora, Baja California")#imprime un menu
est_inicio = input("Ingrese el estado de partida: ")#solicita una entrada
est_objetivo = input("Ingrese el estado est_objetivo: ")#solicita una entrada
costo = grafo.costo_uniforme(est_inicio, est_objetivo)#llama a la funcion costo uniforme de la clase grafos
print(f"El costo minimo de {est_inicio} a {est_objetivo}: {' -> '.join(str(costo))}")#Imprime el costo minimo de la ruta