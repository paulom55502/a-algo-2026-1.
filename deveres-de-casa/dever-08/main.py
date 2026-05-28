import heapq

# Grafo das cidades
grafo = {
    'A': [('B', 4), ('C', 4)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 5), ('E', 6)],
    'D': [('B', 5), ('C', 5), ('E', 3), ('F', 4)],
    'E': [('C', 6), ('D', 3), ('F', 2)],
    'F': [('D', 4), ('E', 2)]
}

def prim(grafo, inicio):
    visitados = set()
    min_heap = [(0, inicio, None)]

    custo_total = 0
    mst = []

    while min_heap:
        custo, cidade, origem = heapq.heappop(min_heap)

        if cidade in visitados:
            continue

        visitados.add(cidade)
        custo_total += custo

        if origem is not None:
            mst.append((origem, cidade, custo))

        for vizinho, peso in grafo[cidade]:
            if vizinho not in visitados:
                heapq.heappush(min_heap, (peso, vizinho, cidade))

    return mst, custo_total


# Executando o algoritmo
mst, custo = prim(grafo, 'A')

print("Cabos instalados:")
for origem, destino, peso in mst:
    print(f"{origem} -> {destino} : {peso} km")

print(f"\nTotal minimo de cabos: {custo} km")