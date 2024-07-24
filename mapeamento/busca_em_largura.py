import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def criar_grafo_a_partir_da_matriz(tamanho):
    # Criar uma matriz de tamanho x tamanho com todos os elementos 0
    matriz = np.zeros((tamanho, tamanho), dtype=int)

    # Criar um grafo vazio
    G = nx.Graph()

    # Adicionar nós ao grafo
    for i in range(tamanho):
        for j in range(tamanho):
            G.add_node((i, j))

    # Adicionar arestas com base na vizinhança na matriz
    for i in range(tamanho):
        for j in range(tamanho):
            # Conectar vizinhos diretamente abaixo
            if i < tamanho - 1:
                G.add_edge((i, j), (i + 1, j))
            # Conectar vizinhos à direita
            if j < tamanho - 1:
                G.add_edge((i, j), (i, j + 1))
            # Conectar vizinhos diagonais inferiores à direita
            if i < tamanho - 1 and j < tamanho - 1:
                G.add_edge((i, j), (i + 1, j + 1))
            # Conectar vizinhos diagonais inferiores à esquerda
            if i < tamanho - 1 and j > 0:
                G.add_edge((i, j), (i + 1, j - 1))

    return G

def bfs(grafo, inicio, objetivo):
    # Verifica se o nó de início e objetivo estão no grafo
    if inicio not in grafo or objetivo not in grafo:
        return None
    
    # Inicializa a fila e o conjunto de visitados
    fila = deque([inicio])
    visitado = {inicio: None}
    
    while fila:
        nodo_atual = fila.popleft()
        
        if nodo_atual == objetivo:
            break
        
        for vizinho in grafo.neighbors(nodo_atual):
            if vizinho not in visitado:
                fila.append(vizinho)
                visitado[vizinho] = nodo_atual
    
    # Reconstruir o caminho
    caminho = []
    passo = objetivo
    while passo is not None:
        caminho.append(passo)
        passo = visitado[passo]
    caminho.reverse()
    
    return caminho

def desenhar_grafo(G, caminho=None):
    # Posiciona os nós em uma grade
    tamanho = max(max(G.nodes)) + 1
    pos = {(i, j): (j, -i) for i in range(tamanho) for j in range(tamanho)}

    # Desenhar o grafo
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=50, font_size=8, font_color='black', font_weight='bold', edge_color='gray')
    
    # Se um caminho for fornecido, destacar o caminho
    if caminho:
        caminho_edges = list(zip(caminho[:-1], caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=caminho_edges, edge_color='r', width=2)

    plt.show()

# Definir o tamanho da matriz
tamanho_matriz = 15

# Criar o grafo
G = criar_grafo_a_partir_da_matriz(tamanho_matriz)

# Definir o ponto de início e objetivo
inicio = (0, 0)
objetivo = (14,14)

# Realizar a busca em largura
caminho = bfs(G, inicio, objetivo)

# Imprimir o caminho
print("Caminho encontrado:", caminho)

# Desenhar o grafo com o caminho destacado
desenhar_grafo(G, caminho)
