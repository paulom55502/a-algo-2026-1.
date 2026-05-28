# Grafo: (origem, destino, peso)
arestas = [
    (0, 1, 5),
    (1, 2, 3),
    (1, 3, 2),
    (2, 4, 1),
    (4, 3, -1)
]

vertices = 5
origem = 0

# Inicialização
dist = [float('inf')] * vertices
pred = [-1] * vertices

dist[origem] = 0

# Relaxamento
for i in range(vertices - 1):
    print(f"\nIteracao {i+1}")

    for u, v, peso in arestas:
        if dist[u] != float('inf') and dist[u] + peso < dist[v]:
            dist[v] = dist[u] + peso
            pred[v] = u

    # Mostrar tabela
    print("Vertice | Distancia | Predecessor")
    for j in range(vertices):
        print(f"{j:^8} | {dist[j]:^10} | {pred[j]}")

# Verificação de ciclo negativo
ciclo_negativo = False

for u, v, peso in arestas:
    if dist[u] != float('inf') and dist[u] + peso < dist[v]:
        ciclo_negativo = True

if ciclo_negativo:
    print("\nExiste ciclo negativo!")
else:
    print("\nNao existe ciclo negativo.")