import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def is_obstaculo(x, y):
        return (x, y) in obstaculos

def criar_grafo_a_partir_da_matriz_com_obstaculos(tamanho, obstaculos):
    # Criar um grafo vazio
    G = nx.Graph()

    # Adicionar nós ao grafo, exceto para os obstáculos
    for i in range(tamanho):
        for j in range(tamanho):
            if not is_obstaculo(i, j):
                G.add_node((i, j))

    # Adicionar arestas com base na vizinhança na matriz, evitando obstáculos
    for i in range(tamanho):
        for j in range(tamanho):
            if is_obstaculo(i, j):
                continue
            current = (i, j)
            # Conectar vizinhos diretamente abaixo e à direita
            if i < tamanho - 1 and not is_obstaculo(i + 1, j):
                G.add_edge(current, (i + 1, j))
            if j < tamanho - 1 and not is_obstaculo(i, j + 1):
                G.add_edge(current, (i, j + 1))
            
            # Conectar vizinhos diagonais
            if i < tamanho - 1 and j < tamanho - 1 and not (is_obstaculo(i + 1, j + 1) or is_obstaculo(i, j)):
                G.add_edge(current, (i + 1, j + 1))
            if i < tamanho - 1 and j > 0 and not (is_obstaculo(i + 1, j - 1) or is_obstaculo(i, j)):
                G.add_edge(current, (i + 1, j - 1))

    return G

def bfs(grafo, pontos_iniciais, objetivos):
    caminhos = {}
    
    for objetivo in objetivos:
        if objetivo not in grafo:
            caminhos[objetivo] = None
            continue
        
        inicio = pontos_iniciais.get(objetivo)
        if inicio is None or inicio not in grafo:
            caminhos[objetivo] = None
            continue
        
        # Inicializa a busca em largura
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
            passo = visitado.get(passo, None)
        caminho.reverse()
        
        caminhos[objetivo] = caminho if caminho[0] == inicio else None
    
    return caminhos

def desenhar_grafo(G, caminhos=None, obstaculos=None):
    pos = { (i, j): (j, -i) for i in range(max(x[0] for x in G.nodes) + 1) for j in range(max(x[1] for x in G.nodes) + 1)}
    
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=False, node_color='skyblue', node_size=50, edge_color='gray')
    
    if caminhos:
        for caminho in caminhos.values():
            if caminho:
                caminho_edges = list(zip(caminho[:-1], caminho[1:]))
                nx.draw_networkx_edges(G, pos, edgelist=caminho_edges, edge_color='r', width=2)
    
    if obstaculos:
        obs_x, obs_y = zip(*obstaculos)
        plt.scatter(obs_y, [-x for x in obs_x], color='black', s=100, marker='x')

    plt.show()

tamanho_matriz = 25

# Definir obstáculos como uma lista de coordenadas
obstaculos = [(7, 7), (8, 7), (9, 7), (7, 8), (8, 8), (9, 8)]  # Exemplo de obstáculos

# Criar o grafo com obstáculos
G = criar_grafo_a_partir_da_matriz_com_obstaculos(tamanho_matriz, obstaculos)

# Definir múltiplos objetivos e seus pontos de início associados
pontos_iniciais = {
    (24, 0): (0, 24),
    (0, 24): (0, 0),
    (0, 0): (24, 24)
}

objetivos = list(pontos_iniciais.keys())

# Realizar a busca em largura para múltiplos objetivos
caminhos = bfs(G, pontos_iniciais, objetivos)

# Imprimir os caminhos
for objetivo, caminho in caminhos.items():
    print(f"Caminho encontrado para {objetivo}: {caminho}")

# Desenhar o grafo com os caminhos e obstáculos destacados
desenhar_grafo(G, caminhos, obstaculos)
