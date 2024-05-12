import networkx as nx
import random

def generate_graph(n, saturation, directed=False, cyclic=False):
    if directed:
        G = nx.DiGraph()
        edges = (n * (n - 1)) // 100 * saturation
    else:
        G = nx.Graph()
        edges = (n * (n - 1) // 2) // 100 * saturation
    
    if cyclic and not directed:
        G = nx.cycle_graph(n)
        edges -= n
    
    while G.number_of_edges() < edges:
        u, v = random.sample(range(1, n + 1), 2)
        if not G.has_edge(u, v):
            G.add_edge(u, v)
    
    return G


n_values = [10, 15, 20] 
s_values = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for n in n_values:
    for s in s_values:
        cyclic_undirected = generate_graph(n, s, cyclic=True)

        cyclic_directed = generate_graph(n, s, directed=True, cyclic=True)
        for f, t in cyclic_directed.edges:
            print(f,t)
        break
    break

def generate_eulerian_digraph(n, saturation):
    G = nx.DiGraph()
    edges = (n * (n - 1)) // 100 * saturation

    for i in range(1, n + 1):
        G.add_node(i)

    for i in range(1, n + 1):
        G.add_edge(i, (i % n) + 1)

    edges -= n
    
    while G.number_of_edges() < edges:
        u, v = random.sample(range(1, n + 1), 2)
        if not G.has_edge(u, v) and u != v:
            G.add_edge(u, v)
    
    return G


def generate_eulerian_digraph2(n, saturation):
    G = nx.DiGraph()
    edges = (n * (n - 1)) // 100 * saturation

    for i in range(1, n + 1):
        G.add_node(i)

    for i in range(1, n + 1):
        G.add_edge(i, (i % n) + 1)

    edges -= n

    while G.number_of_edges() < edges:
        u, v = random.sample(range(1, n + 1), 2)
        if not G.has_edge(u, v) and u != v:
            G.add_edge(u, v)
    
    if not nx.is_strongly_connected(G):
        raise ValueError("The generated graph is not strongly connected.")
    
    # Ensure each node has equal in-degree and out-degree
    for node in G.nodes:
        if G.in_degree(node) != G.out_degree(node):
            if abs(G.in_degree(node) - G.out_degree(node)) > 2:
                raise ValueError("The generated graph is not Eulerian.")
            elif G.in_degree(node) < G.out_degree(node):
                while G.in_degree(node) < G.out_degree(node):
                    u = random.choice(list(G.nodes - {node}))
                    if not G.has_edge(u, node):
                        G.add_edge(u, node)
            else:
                while G.out_degree(node) < G.in_degree(node):
                    v = random.choice(list(G.nodes - {node}))
                    if not G.has_edge(node, v):
                        G.add_edge(node, v)

    return G


def generate_eulerian_digraph3(n, saturation):
    G = nx.DiGraph()
    edges = (n * (n - 1)) // 100 * saturation

    for i in range(1, n + 1):
        G.add_node(i)

    for i in range(1, n + 1):
        G.add_edge(i, (i % n) + 1)

    edges -= n
    
    while G.number_of_edges() < edges:
        u, v = random.sample(range(1, n + 1), 2)
        if not G.has_edge(u, v) and u != v:
            G.add_edge(u, v)
    
    # Ensure each node has equal in-degree and out-degree
    for node in G.nodes:
        while G.in_degree(node) < G.out_degree(node):
            v = random.choice(list(G.nodes - {node}))
            if not G.has_edge(node, v):
                G.add_edge(node, v)
        while G.out_degree(node) < G.in_degree(node):
            u = random.choice(list(G.nodes - {node}))
            if not G.has_edge(u, node):
                G.add_edge(u, node)

    return G


def generate_eulerian_digraph4(num_vertices, edge_density):
    # Utwórz pusty skierowany graf
    G = nx.DiGraph()

    # Dodaj wierzchołki do grafu
    G.add_nodes_from(range(num_vertices))

    # Oblicz maksymalną liczbę krawędzi dla danego grafu skierowanego
    max_edges = num_vertices * (num_vertices - 1)

    # Oblicz ilość krawędzi do dodania
    num_edges = int(edge_density * max_edges)

    # Dodaj krawędzie do grafu
    while G.number_of_edges() < num_edges:
        # Losowo wybierz dwa wierzchołki, które nie mają krawędzi między nimi
        u, v = random.sample(list(G.nodes()), 2)
        if not G.has_edge(u, v):
            G.add_edge(u, v)

    return G

# num_vertices = 10  # Liczba wierzchołków
# edge_density = 0.5  # Nasycenie krawędziami (zakres od 0 do 1)
# digraph = generate_eulerian_digraph4(num_vertices, edge_density)
# print("Liczba krawędzi w skierowanym grafie:", digraph.number_of_edges())
# print("Czy graf jest eulerowski?", nx.is_eulerian(digraph))

def generate_eulerian_digraph5(num_vertices):
    # Utwórz pusty skierowany graf
    G = nx.DiGraph()

    # Dodaj wierzchołki do grafu
    G.add_nodes_from(range(num_vertices))

    # Dodaj krawędzie do grafu
    for u in range(num_vertices):
        for v in range(u+1, num_vertices):
            if random.random() < 0.5:
                G.add_edge(u, v)
            else:
                G.add_edge(v, u)

    # Uzyskaj listę wierzchołków o stopniu nieparzystym
    odd_degree_nodes = [node for node, degree in G.in_degree() if degree % 2 != 0]

    # Dopóki istnieją wierzchołki o stopniu nieparzystym, dodaj dodatkową krawędź
    while odd_degree_nodes:
        u = random.choice(odd_degree_nodes)
        v_candidates = list(set(range(num_vertices)) - set(G[u]))  # Wybierz spośród wierzchołków niepołączonych z u
        if v_candidates:
            v = random.choice(v_candidates)
            G.add_edge(u, v)
        odd_degree_nodes = [node for node, degree in G.in_degree() if degree % 2 != 0]

    return G

# # Przykładowe użycie
# num_vertices = 10  # Liczba wierzchołków
# digraph = generate_eulerian_digraph5(num_vertices)
# print("Liczba krawędzi w skierowanym grafie:", digraph.number_of_edges())
# print("Czy graf jest eulerowski?", nx.is_eulerian(digraph))

def generate_eulerian_directed_graph6(n, saturation):
    # Sprawdź, czy podane nasycenie jest możliwe
    max_possible_edges = n * (n - 1)
    if saturation > 1:
        raise ValueError("Nasycenie musi być mniejsze lub równe 1")

    # Oblicz liczbę krawędzi
    m = int(max_possible_edges * saturation)

    # Wygeneruj sekwencję stopni wychodzących
    out_deg_sequence = [random.randint(0, n-1) for _ in range(n)]

    # Wygeneruj graf Havel-Hakimi
    G = nx.directed_havel_hakimi_graph(out_deg_sequence, seed=42)

    # Sprawdź, czy graf jest eulerowski
    if not nx.is_eulerian(G):
        raise ValueError("Graf nie jest eulerowski")

    # Dodaj brakujące krawędzie
    while G.number_of_edges() < m:
        u, v = random.sample(G.nodes(), 2)
        if not G.has_edge(u, v):
            G.add_edge(u, v)

    return G

# # Przykładowe użycie
# n = 10  # liczba wierzchołków
# saturation = 0.5  # nasycenie
# G = generate_eulerian_directed_graph6(n, saturation)
# print("Liczba krawędzi w grafie:", G.number_of_edges())
# print("Czy graf jest eulerowski?", nx.is_eulerian(G))