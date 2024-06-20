import heapq
# En esta clase se van a encontrar los componentes de un grafo
class Grafo:
    def __init__(self):
        self.nodo = set()
        self.arista = {} # diccionario que mapea cada nodo a una lista de nodos adyacentes
        self.pesos = {} 

    def nuevo_nodo(self, valor):
        self.nodo.add(valor)
        self.arista[valor] = []

    def nueva_arista(self, desde_nodo, a_nodo, peso):
        self.arista[desde_nodo].append(a_nodo)
        self.arista[a_nodo].append(desde_nodo)
        self.pesos[(desde_nodo, a_nodo)] = peso
        self.pesos[(a_nodo, desde_nodo)] = peso

# algoritmo que determina el camino más corto de un nodo a otro 
def dijkstra(grafo, inicial):
    visitado = {inicial: 0} # Funciona eligiendo un nodo como inicial
    ruta = {}

    nodo = set(grafo.nodo)
    pila = [(0, inicial)] # cola de prioridad que almacena los nodos a visitar

    while nodo and pila: # Mientras haya nodos sin visitar y la pila no este vacía
        (costo, min_nodo) = heapq.heappop(pila) # Usa una cola de prioridad
        if min_nodo not in nodo: 
            continue

        nodo.remove(min_nodo)
        for vecino in grafo.arista[min_nodo]:
            if vecino in nodo:
                nuevo_costo = costo + grafo.pesos[(min_nodo, vecino)] # Calculamos el nuevo coste para llegar al vecino
                if nuevo_costo < visitado.get(vecino, float('inf')): # Eso es infinito
                    visitado[vecino] = nuevo_costo
                    heapq.heappush(pila, (nuevo_costo, vecino))
                    ruta[vecino] = min_nodo # actualiza el diccionario 

    return visitado, ruta

def ruta_mas_corta(grafo, origen, destino):
    pesos, ruta = dijkstra(grafo, origen)
    camino = [destino]

    while destino in ruta:
        destino = ruta[destino]
        camino.append(destino)

    camino.reverse()
    return camino
# Crear el grafo
g = Grafo()
nodos = ['A', 'B', 'C', 'D', 'E']
for n in nodos:
    g.nuevo_nodo(n)

aristas = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1),
    ('D', 'E', 3)
]

for arista in aristas:
    g.nueva_arista(*arista)

# Calcular la ruta más corta
origen = 'A'
destino = 'E'
caminito = ruta_mas_corta(g, origen, destino)
print(f"La ruta más corta de {origen} a {destino} es {caminito}")
