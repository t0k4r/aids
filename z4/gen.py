import re
import networkx as nx
import random

from networkx import is_eulerian

def directed_hamiltonian(n: int, s: float):
    G = nx.DiGraph()
    for i in range(1,n):
        G.add_edge(i-1, i)
    G.add_edge(n-1,0)
    s/=100
    full = (n*(n-1))/2
    while s > G.number_of_edges()/full:
        i,j = random.randint(0,n-1), random.randint(0,n-1)
        if not G.has_edge(i,j):
            G.add_edge(i,j)
    # print(nx.tournament.hamiltonian_path(G))
    return G

import mg
def directed_acy(n: int, s: float):
    G = nx.DiGraph()
    for i in range(1,n):
        G.add_edge(i-1, i)
    # G.add_edge(n-1,0)
    s/=100
    full = (n*(n-1))/2
    while s > G.number_of_edges()/full:
        i,j = random.randint(0,n-1), random.randint(0,n-1)
        if not G.has_edge(i,j):
            G.add_edge(i,j)
            try:
                print(nx.tournament.hamiltonian_path(G))
                if not nx.algorithms.is_directed_acyclic_graph(G):
                    print("rm")
                    G.remove_edge(i,j)
                else:
                    print("no")
            except:
                pass
    # print(nx.tournament.hamiltonian_path(G))
    return G



def undirected_hamiltonian(n: int, s: float):
    G = nx.Graph()
    for i in range(1,n):
        G.add_edge(i-1, i)
    G.add_edge(n-1,0)
    s/=100
    full = (n*(n-1))/2
    while s > G.number_of_edges()/full:
        i,j = random.randint(0,n-1), random.randint(0,n-1)
        if not G.has_edge(i,j):
            G.add_edge(i,j)

    return G

def directed_eulerian(n:int, s:float):
    
    G = undirected_hamiltonian(n,s)
    # print(nx.is_eulerian(G))
    # G = directed_hamiltonian(n,  s)
    # G.add_edge(3,5)
    # G.add_edge(5,8)  
    # G.add_edge(8,3)
    # print(nx.is_eulerian(G))
    # return
    # G = nx.complete_graph(n, nx.DiGraph())
    # s/=100
    # full = (n*(n-1))/2
    # while s < G.number_of_edges()/full:
    #     i,j = random.randint(0,n-1), random.randint(0,n-1)
    #     if not G.has_edge(i,j):
    #         G.add_edge(i,j)
    #     pass
    # while not nx.is_eulerian(G):
    #     i,j = random.randint(0,n-1), random.randint(0,n-1)
    #     if not G.has_edge(i,j):
    #         G.remove_edge(i,j)
    #         G.remove_edge(j,i)
    #         if not nx.is_eulerian(G):
    #             G.add_edge(i,j)
    #         else:
    #             print("norm")
    # return G
    G2 = nx.DiGraph()
    for i, j in nx.eulerian_circuit(nx.eulerize(G)):
        G2.add_edge(i,j)
        # pass
    return G2
    if not nx.is_eulerian(G2):
        print("true")
        print(G2)
        return directed_eulerian(n,s)
    return G2
# 
# directed_eulerian(10,90)
