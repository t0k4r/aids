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
        print("NIE MA")
        return False
    else:
        print("Jest", end="")
        for i in path:
            print(i, end=" ")
        print(path[0])
        return path



# Przykładowe użycie
graph = read_graph()
cycle = hamiltonian_cycle(graph)
if cycle:
    print("Hamiltonian cycle path:", cycle)
