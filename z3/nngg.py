import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_dag(n, edge_density):
    G = nx.DiGraph()
    max_edges = n * (n - 1) // 2
    num_edges = int(edge_density * max_edges)
    
    # Add vertices
    G.add_nodes_from(range(n))
    
    # Add edges
    edges_added = 0
    while edges_added < num_edges:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and not G.has_edge(u, v) and not nx.algorithms.dag.descendants(G, u):
            G.add_edge(u, v)
            edges_added += 1
            
    return G

# Range of n values
n_values = list(range(100, 151))

# Edge density (50%)
edge_density = 0.5

# Generate graphs for different n values
graphs = {}
for n in n_values:
    G = generate_dag(n, edge_density)
    graphs[n] = G