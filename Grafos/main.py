import heapq

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}  # Diccionario que mapea cada nodo a una lista de nodos adyacentes
        self.pesos = {}    # Diccionario que mapea cada par de nodos a su peso

    def agregar_nodo(self, valor):
        self.nodos.add(valor)
        self.aristas[valor] = []

    def agregar_arista(self, desde_nodo, a_nodo, peso):
        self.aristas[desde_nodo].append(a_nodo)
        self.aristas[a_nodo].append(desde_nodo)
        self.pesos[(desde_nodo, a_nodo)] = peso
        self.pesos[(a_nodo, desde_nodo)] = peso
        
    # algoritmo que determina el camino más corto de un nodo a otro 
    def dijkstra(self, inicial):
        visitado = {inicial: 0} # Funciona eligiendo un nodo como inicial
        ruta = {}
        nodos_pendientes = set(self.nodos)
        cola_prioridad = [(0, inicial)] # cola de prioridad que almacena los nodos a visitar

        while nodos_pendientes and cola_prioridad: # Mientras haya nodos sin visitar y la pila no este vacía
            costo_actual, nodo_actual = heapq.heappop(cola_prioridad) # Usa una cola de prioridad
            if nodo_actual not in nodos_pendientes:
                continue

            nodos_pendientes.remove(nodo_actual)
            for vecino in self.aristas[nodo_actual]:
                if vecino in nodos_pendientes:
                    nuevo_costo = costo_actual + self.pesos[(nodo_actual, vecino)] # Calculamos el nuevo coste para llegar al vecino
                    if nuevo_costo < visitado.get(vecino, float('inf')):
                        visitado[vecino] = nuevo_costo
                        heapq.heappush(cola_prioridad, (nuevo_costo, vecino))
                        ruta[vecino] = nodo_actual

        return visitado, ruta

    def ruta_mas_corta(self, origen, destino):
        pesos, ruta = self.dijkstra(origen)
        camino = [destino]

        while destino in ruta:
            destino = ruta[destino]
            camino.append(destino)

        camino.reverse()
        return camino


# Crear el grafo
g = Grafo()
nodos = ['A', 'B', 'C', 'D', 'E']
for nodo in nodos:
    g.agregar_nodo(nodo)

aristas = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1),
    ('D', 'E', 3)
]

for arista in aristas:
    g.agregar_arista(*arista)

# Calcular la ruta más corta
origen = 'A'
destino = 'E'
camino = g.ruta_mas_corta(origen, destino)
print(f"La ruta más corta de {origen} a {destino} es {camino}")

