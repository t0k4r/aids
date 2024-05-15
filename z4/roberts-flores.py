def read_graph():
    # Wczytaj liczbę wierzchołków i krawędzi
    vertices, edges = map(int, input().split())

    # Inicjalizuj macierz sąsiedztwa
    graph = []
    for i in range(vertices):
        row = [0] * vertices
        graph.append(row)

    # Wczytaj krawędzie
    for i in range(edges):
        # Wczytaj parę wierzchołków
        v1, v2 = map(int, input().split())
        # Dodaj krawędź do grafu (graf nieskierowany)
        graph[v1][v2] = 1
        graph[v2][v1] = 1

    return graph


def is_valid(v, k, graph, path):
    #czy krawędź pomiędzy ostatnio dodanym wierzchołkiem, a wierzchołkiem v
    if graph[path[k - 1]][v] == 0:
        return False
    #czy v został już odwiedzony
    if v in path:
        return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    #Czy pos osiągnął koniec ścieżki
    if pos == len(graph):
        #czy istnieje krawędź pomiędzy pierwszym i ostatnim
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, len(graph)):
        if is_valid(v, pos, graph, path):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False

def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not hamiltonian_cycle_util(graph, path, 1):
        # print("NIE MA")
        raise Exception("Graf wejściowy nie zawiera cyklu")
        # return False
    else:
        path.append(path[0])
        # print("Jest", end="")
        # for i in path:
            # print(i, end=" ")
        # print(path[0])
        return list(map(lambda x: x+1, path))

import gen
def gen_graph():
    n,s = 5, 90
    # Wczytaj liczbę wierzchołków i krawędzi
    # vertices, edges = map(int, input().split())
    vertices = n
    # Inicjalizuj macierz sąsiedztwa
    graph = []
    for i in range(n):
        row = [0] * vertices
        graph.append(row)
    G = gen.directed_hamiltonian(n,s)

    # Wczytaj krawędzie
    # for i, j in G.edges:
    edges = []
    edges.append((1,2))
    edges.append((1,4))
    edges.append((2,4))
    edges.append((3,4))
    edges.append((3,5))
    edges.append((5,4))


    for i, j in edges:
        graph[i-1][j-1] = 1
        graph[j-1][i-1] = 1
    #     pass
    # for i in range(edges):
    #     # Wczytaj parę wierzchołków
    #     v1, v2 = map(int, input().split())
    #     # Dodaj krawędź do grafu (graf nieskierowany)
    #     graph[v1][v2] = 1
    #     graph[v2][v1] = 1
    return graph


def read_graph_from_file(filename):
    # Wczytywanie grafu z pliku tekstowego
    with open(filename, 'r') as file:
        num_vertices, num_edges = map(int, file.readline().split())
        graph = []
        for i in range(num_vertices):
            row = [0] * num_vertices
            graph.append(row)
        # Dodawanie krawędzi na podstawie danych z pliku
        for _ in range(num_edges):
            i, j = map(int, file.readline().split())
            graph[i][j] = 1
            graph[j][i] = 1
        return graph


def cyklHamiltona():
    g=gen_graph()
    print(hamiltonian_cycle(g))
    pass
\
if __name__ == "__main__":
    cyklHamiltona()
# Przykładowe użycie
# graph = read_graph()
# cycle = hamiltonian_cycle(graph)
# if cycle:
#     print("Hamiltonian cycle path:", cycle)

