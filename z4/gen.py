import networkx as nx
import random

def directed_hamiltonian(n: int, s: float):
    G = nx.DiGraph()
    for i in range(1,n):
        G.add_edge(i-1, i)
    G.add_edge(n-1,0)
    s/=100
    full = (n*(n-1))/2
    while s > G.number_of_edges()/full:
        G.add_edge(random.randint(0,n-1), random.randint(0,n-1))

    return G

def undirected_hamiltonian(n: int, s: float):
    G = nx.Graph()
    for i in range(1,n):
        G.add_edge(i-1, i)
    G.add_edge(n-1,0)
    s/=100
    full = (n*(n-1))/2
    while s > G.number_of_edges()/full:
        G.add_edge(random.randint(0,n-1), random.randint(0,n-1))

    return G

def directed_eulerian(n:int, s:float):
    G = undirected_hamiltonian(n,s)
    G2 = nx.DiGraph()
    for i, j in nx.eulerian_circuit(nx.eulerize(G)):
        G2.add_edge(i,j)
    print(nx.is_eulerian(G2))

directed_eulerian(10,50)