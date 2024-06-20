#clase 7 C33852
from ColaPrioridad import ColaPrioridad

pq = ColaPrioridad()

pq.push('Tarea 1', 5)
pq.push('Tarea 2', 1)
pq.push('Tarea 3', 3)
pq.push('Tarea 4', 2)

print(pq.pop()) # Imprime 'Tarea 1'
print(pq.pop()) # Imprime 'Tarea 3'
print(pq.pop()) # Imprime 'Tarea 4'
print(pq.pop()) # Imprime 'Tarea 2'
