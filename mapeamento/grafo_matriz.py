import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo_a_partir_da_matriz(tamanho):
    # Passo 1: Criar uma matriz de tamanho x tamanho com todos os elementos 0
    matriz = np.zeros((tamanho, tamanho), dtype=int)

    # Passo 2: Criar um grafo vazio
    G = nx.Graph()

    # Passo 3: Adicionar nós ao grafo
    for i in range(tamanho):
        for j in range(tamanho):
            G.add_node((i, j))

    # Passo 4: Adicionar arestas com base na vizinhança na matriz
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

def desenhar_grafo(G, tamanho):
    # Posiciona os nós em uma grade
    pos = {(i, j): (j, -i) for i in range(tamanho) for j in range(tamanho)}

    # Desenhar o grafo
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=50, font_size=8, font_color='black', font_weight='bold', edge_color='gray')
    plt.show()

# Definir o tamanho da matriz
tamanho_matriz = 15

# Criar o grafo
G = criar_grafo_a_partir_da_matriz(tamanho_matriz)

# Desenhar o grafo
desenhar_grafo(G, tamanho_matriz)
