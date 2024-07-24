import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo simples
G = nx.Graph()

# Adicionando nós
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Adicionando arestas
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# Desenhando o grafo
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, font_size=15, font_color='black', font_weight='bold')
plt.show()
