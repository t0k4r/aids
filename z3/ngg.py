import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_dag(n, edge_density):
    G = nx.DiGraph()
    max_edges = n * (n - 1) // 2
    num_edges = int(edge_density * max_edges)
    
    # Dodajemy wierzchołki
    G.add_nodes_from(range(n))
    
    # Dodajemy krawędzie
    edges_added = 0
    while edges_added < num_edges:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and not G.has_edge(u, v) and not nx.algorithms.dag.descendants(G, u):
            G.add_edge(u, v)
            edges_added += 1
            
    return G

# Zakres wartości n
n_values = list(range(100, 151))

# Współczynnik nasycenia krawędziami (50%)
edge_density = 0.5

# Generowanie grafów dla różnych wartości n
graphs = {}
for n in n_values:
    G = generate_dag(n, edge_density)
    graphs[n] = G

# Rysowanie i zapis grafów
for n, G in graphs.items():
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, arrowsize=10)
    plt.title(f"DAG dla n={n}")
    plt.savefig(f"DAG_n_{n}.png")
    plt.close()

print("Grafy zostały wygenerowane i zapisane.")
